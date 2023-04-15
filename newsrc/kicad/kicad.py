import pcbnew
import os

UNIT_MM = 1
UNIT_MIL = 5
UNIT_IN = 0

class Kicad_utils:
    def __init__(self):
        pass

    def update(self):
        self.version = pcbnew.Version()

    def get_units(self):
        units = pcbnew.GetUserUnits()

        if units == -1:
            units = UNIT_MM

        return units


    def to_unit(self, units, value):
        if units == UNIT_MM:
            return pcbnew.ToMM(value)
        elif units == UNIT_MIL:
            return pcbnew.ToMils(value)
        elif units == UNIT_IN:
            return pcbnew.ToMils(value) / 1000
        else:
            assert 0, "invalid unit " + str(units)


    def from_unit(self, units, value):
        if units == UNIT_MM:
            return pcbnew.FromMM(value)
        elif units == UNIT_MIL:
            return pcbnew.FromMils(value)
        elif units == UNIT_IN:
            return pcbnew.FromMils(value * 1000)
        else:
            assert 0, "invalid unit " + str(units)


    def get_layers(self):
        layers = []
        pcb = self.get_board()

        for i in pcb.GetEnabledLayers().UIOrder():
            layers.append(pcbnew.LayerName(i))

        return layers


    def get_board(self):
        if config.test_mode:
            return pcbnew.LoadBoard(os.path.dirname(__file__) + "/" + "../../" + config.board_file)
        else:
            return pcbnew.GetBoard()


    def get_copper_layers(self):
        layers = []
        pcb = self.get_board()

        for i in pcb.GetEnabledLayers().CuStack():
            layers += pcbnew.LayerName(i)

        return layers


    def get_layer_id(self, layer_name):
        pcb = self.get_board()

        for layer_id in pcb.GetEnabledLayers().UIOrder():
            if pcbnew.LayerName(layer_id) == layer_name:
                return layer_id

        assert 0, "Error, layer " + layer_name + " does not exist"

kicad_utils = Kicad_utils()

