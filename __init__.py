import traceback
import sys


try:
    from .complex_plugin_action import ComplexPluginAction # Note the relative import!

    ComplexPluginAction().register() # Instantiate and register to Pcbnew

except (Exception, ArithmeticError) as e:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(e).__name__, e.args)
    print (message)

    exc_type, exc_value, exc_tb = sys.exc_info()

    stack_summary = traceback.extract_tb(exc_tb)
    end = stack_summary[-1]

    err_type = type(exc_value).__name__
    err_msg = str(exc_value)

    print(f"\n{err_type}")
    print(f"{err_msg}.")
    print(f"file: {end.filename}")
    print(f"method: {end.name}")
    print(f"linenr: {end.lineno}")
    print(f"{end.line!r}")

