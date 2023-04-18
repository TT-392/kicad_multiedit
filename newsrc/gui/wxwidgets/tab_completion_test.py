import wx

completions = ["footprint", "trace", "via", "polygon", "pretzel", "postit"]

class MyFrame(wx.Frame):
    def __init__(self, parent, title):

        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        panel = wx.Panel(self)
        self.input_ctrl1 = wx.TextCtrl(panel)
        self.input_ctrl2 = wx.TextCtrl(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.input_ctrl1, 0, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.AddSpacer(10)
        vbox.Add(self.input_ctrl2, 0, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)

        self.input_ctrl1.Bind(wx.EVT_CHAR, self.__on_input)
        self.Centre()

    # TESTABLE:
    def __get_suggestions(self, string):
        retval = []

        for completion in completions:
            if string == completion[:len(string)]:
                retval.append(completion[len(string):])

        return retval


    # TESTABLE:
    def __cursor_in_valid_location_for_completion(self, inp, cursor_position):
        if (cursor_position != 0):
            char_before_cursor = inp[cursor_position - 1]
        else:
            char_before_cursor = None


        if cursor_position < len(inp):
            char_after_cursor = inp[cursor_position]
        else:
            char_after_cursor = '\0'

        chars_at_end_of_completable_term = \
        [' ', '\n', '\t', '\r', '\v', '\f', '\0', '+', '-', '*', '/', '%', '&', '|', '^', ',', ';', ':', ']', ')', '}', '<', '>', '=', '@', '#', '~']

        return char_after_cursor in chars_at_end_of_completable_term and not char_before_cursor in chars_at_end_of_completable_term


    #TESTABLE:
    def __extract_beginning_of_word(self, inp, cursor_position):
        chars_at_start_of_completable_term = \
        [' ', '\n', '\t', '\r', '\v', '\f', '\0', '+', '-', '*', '/', '%', '&', '|', '^', ',', ';', ':', ']', ')', '}', '<', '>', '=', '@', '#', '~', '(', '[', '{', None]

        retval = inp[:cursor_position]

        for i in range(len(retval) - 1, -1, -1):
            if retval[i] in chars_at_start_of_completable_term:
                retval = retval[i + 1:]
                break

        return retval


    class __Contents:
        def __init__(self, contents, cursor_pos):
            self.contents = contents
            self.cursor_pos = cursor_pos

        def get(self, insert_string):
            return_string = self.contents[:self.cursor_pos] + insert_string + self.contents[self.cursor_pos:]
            return_cursor_pos = self.cursor_pos + len(insert_string)
            return return_string, return_cursor_pos


    __completion_active = False

    def __on_input(self, event):
        if event.GetKeyCode() == wx.WXK_TAB:
            if not self.__completion_active:
                self.input = self.input_ctrl1.GetValue()
                self.cursor_position = self.input_ctrl1.GetInsertionPoint()

                if self.__cursor_in_valid_location_for_completion(self.input, self.cursor_position):
                    self.__suggestions = self.__get_suggestions(self.__extract_beginning_of_word(self.input, self.cursor_position))

                    if len(self.__suggestions) != 0:
                        self.__completion_active = True
                        self.__contents = self.__Contents(self.input, self.cursor_position)
                        self.__index = 0
                else:
                    event.Skip()

            
            if self.__completion_active:
                new_string, new_cursor_pos = self.__contents.get(self.__suggestions[self.__index])

                self.__index += 1
                if self.__index == len(self.__suggestions):
                    self.__index = 0

                self.input_ctrl1.SetValue(new_string)
                self.input_ctrl1.SetInsertionPoint(new_cursor_pos)

        elif event.GetKeyCode() == wx.WXK_ESCAPE:
            self.input_ctrl1.SetValue(self.input)
            self.input_ctrl1.SetInsertionPoint(self.cursor_position)

        else:
            self.__completion_active = False
            event.Skip()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, "Two TextCtrl Boxes")
    frame.Show()
    app.MainLoop()

