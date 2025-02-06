import unittest
from two_stack import evaluate_expression

class TestDijkstraEvaluator(unittest.TestCase):
    def test_parentheses(self):
        self.assertEqual(evaluate_expression("( 1 + 2 )"), 3)
        self.assertEqual(evaluate_expression("( ( 1 + 2 ) * ( 3 + 4 ) )"), 21)

    def test_nested_expressions(self):
        self.assertEqual(evaluate_expression("( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )"), 101)
        self.assertEqual(evaluate_expression("( 3 + ( 6 * 2 ) )"), 15)

if __name__ == "__main__":
    unittest.main()