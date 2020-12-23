import abc
import random
import matplotlib.pyplot as plt


class BaseGame(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self):
        """"Main method to run the game."""
        pass

    @abc.abstractmethod
    def _input_check(self):
        """Check user input."""
        pass


class DiceRolling(BaseGame):
    """Rolling a dice."""

    REROLL = 1
    STOP = 0
    BAD_INPUT = -1
    MAX = 12
    MIN = 1

    def run(self):
        """"Main method to run the game."""

        while True:
            choice = input('Roll dice? (y/n): ')
            action = self._input_check(choice)

            if action == DiceRolling.REROLL:
                print(f'You got {self._random_number()}')

            elif action == DiceRolling.STOP:
                return 0

            else:
                print("You must type 'y' or 'n'! Try again...")

    def _input_check(self, choice):
        """Check user input."""
        if choice == 'y':
            return DiceRolling.REROLL

        elif choice == 'n':
            return DiceRolling.STOP

        else:
            return DiceRolling.BAD_INPUT

    def _random_number(self):
        return random.randint(DiceRolling.MIN, DiceRolling.MAX)


class GuessingGame(BaseGame):
    """Guess a number between 1 and 99."""

    VALID_INPUT = 1
    BAD_INPUT = 0
    LOW = 0
    HIGH = 1
    EQUAL = -1

    def __init__(self):
        self.__true_value = random.randint(1, 99)
        self.__guesses = []
        self.__choice = 0

    def run(self):
        """"Main method to run the game."""

        while True:
            self.__choice = input('Enter an integer from 1 to 99: ')
            action = self._input_check()

            if action == GuessingGame.VALID_INPUT:
                self.__guesses.append(self.__choice)
                guess = self._input_compare()

                if guess == GuessingGame.LOW:
                    print('Your guess is low!')

                elif guess == GuessingGame.HIGH:
                    print('Your guess is high!')

                else:
                    print('You guessed it!')
                    self._plot_guesses()
                    break


            elif action == GuessingGame.BAD_INPUT:
                print('Your guess must be within 1 and 99! Try again...')

    def _input_check(self):
        """Check user input."""
        if self.__choice.isdigit():
            self.__choice = int(self.__choice)
            if 1 <= self.__choice <= 99:
                return GuessingGame.VALID_INPUT

        return GuessingGame.BAD_INPUT

    def _input_compare(self):
        """Compares user input to true value."""
        if self.__choice > self.__true_value:
            return GuessingGame.HIGH

        elif self.__choice < self.__true_value:
            return GuessingGame.LOW

        else:
            return GuessingGame.EQUAL

    def _plot_guesses(self):
        """Plot guesses and the true value."""

        plt.figure()
        plt.style.use('ggplot')
        plt.xlabel('Attempts')
        plt.plot(self.__guesses, label='guesses', linestyle='-', marker='o', color='#4c72b0')
        plt.axhline(y=self.__true_value, color='g', linestyle='-', label='true value')
        plt.legend()
        plt.show()
