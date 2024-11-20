import unittest
from parameterized import parameterized
from main import part_one, part_two

class TestMain(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  @parameterized.expand([
    ("(())", 0),
    ("()()", 0),
    ("(((", 3),
    ("(()(()(", 3),
    ("))(((((", 3),
    ("())", -1),
    ("))(", -1),
    (")))", -3),
    (")())())", -3)
  ])
  def test_part_one(self, input: str, expected: int):
    self.assertEqual(part_one(input), expected)

  @parameterized.expand([
    (")", 1),
    ("()())", 5)
  ])
  def test_part_two(self, input: str, expected: int):
    self.assertEqual(part_two(input), expected)

if __name__ == "__main__":
  unittest.main()