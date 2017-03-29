# vim: set fileencoding=utf-8 :
from abc import ABCMeta, abstractmethod

class AbstractRuntime(metaclass=ABCMeta):

    @abstractmethod
    def evaluate(self, script, team_puzzle_data, user_puzzle_data, team_data, user_data):
        pass

    @abstractmethod
    # TODO: Consider changing to allow returning a result and unlock hints for this puzzle.
    def validate_guess(self, validator, guess, team_puzzle_data, team_data):
        pass