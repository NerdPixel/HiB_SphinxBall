# simple_device.py

from state import InitialState
import logging

class SimpleDevice(object):
    def __init__(self):
        print("Initializing state machine")

        # Start with a default state.
        self.state = InitialState()

    def on_event(self, event):
        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)