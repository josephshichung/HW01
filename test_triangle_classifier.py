import unittest
from triangle_classifier import classify_triangle

class TestTriangleClassifier(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 4), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")

    def test_isosceles_and_right_triangle(self):
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene and Right")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Not a valid triangle")

if __name__ == '__main__':
    unittest.main()
