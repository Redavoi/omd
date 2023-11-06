import unittest
from typing import List, Tuple


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b)
                        for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class TestFitTransform(unittest.TestCase):
    def test_four_categories(self):
        actual = fit_transform('a', 'b', 'c', 'd')
        expected = [('a', [0, 0, 0, 1]),
                    ('b', [0, 0, 1, 0]),
                    ('c', [0, 1, 0, 0]),
                    ('d', [1, 0, 0, 0])]
        self.assertEqual(actual, expected)

    def test_four_repeated_categories(self):
        actual = fit_transform('a', 'b', 'c', 'd', 'a', 'b', 'c', 'd')
        expected = [('a', [0, 0, 0, 1]),
                    ('b', [0, 0, 1, 0]),
                    ('c', [0, 1, 0, 0]),
                    ('d', [1, 0, 0, 0]),
                    ('a', [0, 0, 0, 1]),
                    ('b', [0, 0, 1, 0]),
                    ('c', [0, 1, 0, 0]),
                    ('d', [1, 0, 0, 0])]
        self.assertEqual(actual, expected)

    def test_empty_iterable(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_one_category(self):
        actual = fit_transform('a')
        self.assertNotIn(('a', [0]), actual)
