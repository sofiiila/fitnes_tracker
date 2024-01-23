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

    def test_read_package_run_invalid_data(self):
        """Тестирование функции read_package для типа "RUN" 
           с некорректными данными"""    
        workout_type = "RUN"
        data = ["invalid data"]
        with self.assertRaises(ValueError):
            read_package(workout_type, data)

    def test_read_package_swm_invalid_data(self):
        """Тестирование функции read_package для типа "SWM" 
           с некорректными данными"""
        workout_type = "SWM"
        data = ["invalid data"]
        with self.assertRaises(ValueError):
            read_package(workout_type, data)
        
    def test_read_package_wlk_invalid_data(self):
        """Тестирование функции read_package для типа "WLK" 
           с некорректными данными"""
        workout_type = "WLK"
        data = ["invalid data"]
        with self.assertRaises(ValueError):
            read_package(workout_type, data)
    
    def test_read_package_unknown_type(self):
        """Тестирование функции read_package для неизвестного типа тренировки"""
        workout_type = "UNKNOWN"
        data = ["invalid data"]
        with self.assertRaises(ValueError):
            read_package(workout_type, data)

class TestRunning(unittest.TestCase):
    """Тестирование класса Running"""
    def test_get_spent_calories(self):
        running = Running(15000, 1, 75)
        expected_calories = 699.75
        self.assertAlmostEqual(running.get_spent_calories, expected_calories)

    def test_show_training_info(self):
        running = Running(15000, 1, 75)
        expected_message = "Тип тренировки: Running; Длительность: 1.000 ч.; Дистанция: 9.750 км; Ср. скорость: 9.750 км/ч; Потрачено ккал: 699.750."
        self.assertEqual(str(running.show_training_info().get_message()), expected_message)

class TestSportsWalking(unittest.TestCase):
    """Тестирование класса SportsWalking"""
    def test_get_spent_calories(self):
        sports_walking = SportsWalking(9000, 1, 75, 180)
        expected_calories = 157.5
        self.assertAlmostEqual(sports_walking.get_spent_calories, expected_calories)

    def test_show_training_info(self):
        sports_walking = SportsWalking(9000, 1, 75, 180)
        expected_message = "Тип тренировки: SportsWalking; Длительность: 1.000 ч.; Дистанция: 5.850 км; Ср. скорость: 5.850 км/ч; Потрачено ккал: 157.500."
        self.assertEqual(str(sports_walking.show_training_info().get_message()), expected_message)

class TestSwimming(unittest.TestCase):
    """Тестирование класса Swimming"""
    def test_get_spent_calories(self):
        swimming = Swimming(150, 1, 70, 25, 40)
        expected_calories = 156
        self.assertAlmostEqual(swimming.get_spent_calories(), expected_calories)

    def test_show_training_info(self):
        swimming = Swimming(150, 1, 70, 25, 40)
        expected_message = "Тип тренировки: Swimming; Длительность: 1.000 ч.; Дистанция: 1.000 км; Ср. скорость: 1.000 км/ч; Потрачено ккал: 156.000."
        self.assertAlmostEqual(swimming.show_training_info().get_message(), expected_message)


    if __name__ == "__main__":
        unittest.main()        

