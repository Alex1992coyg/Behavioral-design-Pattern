#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod
import time

class InterfaceCommand(metaclass=ABCMeta):
    @abstractmethod
    def execute():
        pass
class Switch:
    ''' invoker class'''
    def __init__(self):
        self._commands = {}
        self._history = []

    @property
    def history(self):
        return self._history

    def register(self, command_name, command):
        self._commands[command_name] = command
    # 
    # def execute(self, command_name):
    #     if command_name in command_name.keys():
    #         self._history.append((time.time(),command_name))
    #         self._commands[command_name].execute()
    #     else:
    #         print(f"Command [{command_name}] not recognised")

class Light:
    '''the receiver'''
    def turn_on(self):
        print("Light turned ON")
    def turn_off(self):
        print("Light turned OFF")

class SwitchOnCommand(InterfaceCommand):
    """ A command object, which impliments the interface command """

    def __init__(self,light):
        self._light = light
    def execute(self):
        self._light.turn_on()
class SwitchOffCommand(InterfaceCommand):
    """ A command object, which impliments the interface command """

    def __init__(self,light):
        self._light = light
    def execute(self):
        self._light.turn_off()

if __name__ == "__main__":
    # The Client is the main python app

    # The Light is the Reciever
    LIGHT = Light()

    # Create Commands
    SWITCH_ON = SwitchOnCommand(LIGHT)
    SWITCH_OFF = SwitchOffCommand(LIGHT)

    # Register the commands with the invoker (Switch)
    SWITCH = Switch()
    SWITCH.register("ON", SWITCH_ON)
    SWITCH.register("OFF", SWITCH_OFF)

    # Execute the commands that are registered on the Invoker
    SWITCH.execute("ON")
    SWITCH.execute("OFF")
    SWITCH.execute("ON")
    SWITCH.execute("OFF")

    # For fun, we can see the history
    print(SWITCH.history)
