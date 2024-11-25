import unittest
from ex2_smelly import Shape, Circle, Rectangle, Triangle # Adjust if the class is in another file

class TestShape(unittest.TestCase):

    def test_calculate_area_circle(self):
        # Test for a circle with radius 5
        result = Circle(radius=5).calculate_area()
        self.assertAlmostEqual(result, 78.5, places=2)

    def test_calculate_area_rectangle(self):
        # Test for a rectangle with length 4 and width 6
        result = Rectangle(length=4, width=6).calculate_area()
        self.assertEqual(result, 24)

    def test_calculate_area_triangle(self):
        # Test for a triangle with base 10 and height 8
        result = Triangle(base=10, height=8).calculate_area()
        self.assertEqual(result, 40)


if __name__ == '__main__':
    unittest.main()
