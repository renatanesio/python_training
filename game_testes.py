import unittest

from game import DiceRolling, GuessingGame


class GameTestes(unittest.TestCase):

    def setUp(self):
        self.dice_rolling = DiceRolling()
        self.guessing_game = GuessingGame()

    def test_input_check_dice_rolling_reroll(self):
        """Testando _input_check de Dice Rolling para dar REROLL"""
        self.assertEqual(
            self.dice_rolling._input_check('y'),
            DiceRolling.REROLL
        )

    def test_input_check_dice_rolling_bad_input(self):
        """Testando _input_check de Dice Rolling com BAD INPUT"""
        self.assertEqual(
            self.dice_rolling._input_check('h'),
            DiceRolling.BAD_INPUT
        )

    def test_input_check_dice_rolling_stop(self):
        """Testando _input_check de Dice Rolling para dar STOP"""
        self.assertEqual(
            self.dice_rolling._input_check('n'),
            DiceRolling.STOP
        )

    def test_input_check_guessing_game_bad_input_letter(self):
        """Testando _input_check de Guessing Game com LETRA como BAD INPUT"""
        self.guessing_game._GuessingGame__choice = 'h'
        self.assertEqual(
            self.guessing_game._input_check(),
            GuessingGame.BAD_INPUT
        )

    def test_input_check_guessing_game_bad_input_number(self):
        """Testando _input_check de Guessing Game com NÚMERO como BAD INPUT"""
        self.guessing_game._GuessingGame__choice = '100'
        self.assertEqual(
            self.guessing_game._input_check(),
            GuessingGame.BAD_INPUT
        )

    def test_input_check_guessing_game_valid_input(self):
        """Testando _input_check de Guessing Game com NÚMERO como BAD INPUT"""
        self.guessing_game._GuessingGame__choice = '50'
        self.assertEqual(
            self.guessing_game._input_check(),
            GuessingGame.VALID_INPUT
        )

    def test_input_compare_high(self):
        """Testando _input_compare com palpite acima do valor real"""
        self.guessing_game._GuessingGame__true_value = '50'
        self.guessing_game._GuessingGame__choice = '70'
        self.assertEqual(
            self.guessing_game._input_compare(),
            GuessingGame.HIGH
        )

    def test_input_compare_low(self):
        """Testando _input_compare com palpite abaixo do valor real"""
        self.guessing_game._GuessingGame__true_value = '50'
        self.guessing_game._GuessingGame__choice = '40'
        self.assertEqual(
            self.guessing_game._input_compare(),
            GuessingGame.LOW
        )

    def test_input_compare_equal(self):
        """Testando _input_compare com palpite igual ao valor real"""
        self.guessing_game._GuessingGame__true_value = '50'
        self.guessing_game._GuessingGame__choice = '50'
        self.assertEqual(
            self.guessing_game._input_compare(),
            GuessingGame.EQUAL
        )


if __name__ == '__main__':
    unittest.main()
