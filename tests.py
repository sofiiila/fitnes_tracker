import unittest
from unittest import TestCase
from fitnes_tracker import read_package, Running, SportsWalking, Swimming

class ReadPackageTestCase(unittest.TestCase):
    def test_read_package_run(self):
        workout_type = "RUN"
        data = [15000, 1, 75]
        expected = Running(15000, 1, 75)

        result = read_package(workout_type, data)

        self.assertIsInstance(result, Running)
        self.assertEqual(result.action, expected.action)
        self.assertEqual(result.duration, expected.duration)
        self.assertEqual(result.weight, expected.weight)

    def test_read_package_swm(self):
        workout_type = "SWM"
        data = [720, 1, 80, 25, 40]
        expected = Swimming(720, 1, 80, 25, 40)

        result = read_package(workout_type, data)

        self.assertIsInstance(result, Swimming)
        self.assertEqual(result.action, expected.action)
        self.assertEqual(result.duration, expected.duration)
        self.assertEqual(result.weight, expected.weight)
        self.assertEqual(result.length_pool, expected.length_pool)
        self.assertEqual(result.count_pool, expected.count_pool)

    def test_read_package_wlk(self):
        workout_type = "WLK"
        data = [9000, 1, 75, 180]
        expected = SportsWalking(9000, 1, 75, 180)

        result = read_package(workout_type, data)

        self.assertIsInstance(result, SportsWalking)
        self.assertEqual(result.action, expected.action)
        self.assertEqual(result.duration, expected.duration)
        self.assertEqual(result.weight, expected.weight)
        self.assertEqual(result.height, expected.height)

    if __name__ == "__main__":
        unittest.main()        

