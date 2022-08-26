try:
    from .complex_plugin_action import ComplexPluginAction # Note the relative import!

    ComplexPluginAction().register() # Instantiate and register to Pcbnew
except (Exception, ArithmeticError) as e:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(e).__name__, e.args)
    print (message)

