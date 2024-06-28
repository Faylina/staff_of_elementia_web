#---------------------------------------#
#---------- DEBUG FUNCTIONS ------------#
#---------------------------------------#

#---------- IMPORTS -----------#
import inspect
from debugging.config import DEBUG

#---------- DEBUG FUNCTIONS ------------#

def debugMethod(self) -> None:
    """ DEBUG: Calling the method 'method-name' of the class 'class-name'. """
    if DEBUG:
        print(f"\nDEBUG: Calling the method '{inspect.stack()[1].function}' of the class '{type(self).__name__}'.")

def debugClass(self) -> None:
    """ DEBUG: 'Class-name' object is being created. """
    if DEBUG:
        print(f"\nDEBUG: {type(self).__name__} object is being created.")

def debugVariable(variable_name: str, variable) -> None:
    """ DEBUG: 'Variable name' = variable """
    if DEBUG:
        print(f"\nDEBUG: '{variable_name}' = {variable}")

def debugProcess(process: str) -> None:
    """ DEBUG: 'Process' has been started."""
    if DEBUG:
        print(f"\nDEBUG: '{process}' has been started.")