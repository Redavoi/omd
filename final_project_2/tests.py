import unittest

from telegram import InlineKeyboardButton

from main import generate_keyboard, get_default_state, won


class TestTicTacToeBot(unittest.TestCase):
    def setUp(self):
        self.default_state = [['.', '.', '.'],
                              ['.', '.', '.'],
                              ['.', '.', '.']]

    def test_default_state(self):
        self.assertEqual(get_default_state(), self.default_state)

    def test_won(self):
        self.assertTrue(won([['X', 'X', 'X'],
                             ['.', '.', '.'],
                             ['.', '.', '.']]))
        self.assertTrue(won([['.', '.', '.'],
                             ['O', 'O', 'O'],
                             ['.', '.', '.']]))
        self.assertTrue(won([['X', '.', '.'],
                             ['X', '.', '.'],
                             ['X', '.', '.']]))
        self.assertTrue(won([['.', '.', 'O'],
                             ['.', '.', 'O'],
                             ['.', '.', 'O']]))
        self.assertTrue(won([['X', '.', '.'],
                             ['.', 'X', '.'],
                             ['.', '.', 'X']]))
        self.assertTrue(won([['.', '.', 'O'],
                             ['.', 'O', '.'],
                             ['O', '.', '.']]))
        self.assertFalse(won([['X', 'O', 'X'],
                              ['X', 'O', 'O'],
                              ['O', 'X', 'X']]))

    def test_generate_keyboard(self):
        keyboard = generate_keyboard(self.default_state)
        for row in keyboard:
            for button in row:
                self.assertIsInstance(button, InlineKeyboardButton)
                self.assertIn(button.text, ['.', 'X', 'O'])
                self.assertIn(button.callback_data, ['00', '01', '02', '10',
                                                     '11', '12', '20', '21',
                                                     '22'])
