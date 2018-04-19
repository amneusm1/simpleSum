import unittest
import simpleSum


class SumTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(simpleSum.sum([1,2,3,4,5,6,7,8,9,0]), 45.0)

    def test_float(self):
        self.assertEqual(simpleSum.sum([1.2, 3.4, 5.5]), 10.1)

    def test_floor(self):
        self.assertEqual(simpleSum.floorSum([1.2, 3.4, 5.5]), 9.0)


if __name__ == '__main__':
    unittest.main()