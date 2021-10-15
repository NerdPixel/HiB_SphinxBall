# state.py

import logging

class State(object):
    def __init__(self):
        print('Processing current state:', str(self))
    
    def on_event(self, event):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

# Start of our states
class InitialState(State):
    def on_event(self, event):
        if event == 'one_questions_answered':
            return EasyQuestionsState()
        return self

class EasyQuestionsState(State):
    def on_event(self, event):
        if event == 'easy_questions_answered':
            return MediumQuestionsState()
        return self

class MediumQuestionsState(State):
    def on_event(self, event):
        if event == 'medium_questions_answered':
            return HardQuestionsState()
        return self

class HardQuestionsState(State):
    def on_event(self, event):
        if event == 'hard_questions_answered':
            return FinalState()
        return self

class FinalState(State):
    def on_event(self, event):
        if event == 'all_questions_answered':
            return InitialState()
        return self
# End of our states.