import unittest
from calculations import Calculations
from filehandler import FileHandler


class Test_ConvertDateFormat(unittest.TestCase):

    date_format = Calculations('/path/to', {'key', 'value'})

    def test_valid_date(self):
        input_date = '2023-09-19'
        expected_date = 'September 19'
        self.assertEqual(self.date_format.convert_date_format(
            input_date), expected_date)

    def test_invalid_date(self):
        input_date = '09-19-2023'
        with self.assertRaises(ValueError):
            self.date_format.convert_date_format(input_date)

    def test_random_date(self):
        input_date = '2023-01-01'
        expected_date = 'January 01'
        self.assertEqual(self.date_format.convert_date_format(
            input_date), expected_date)


class Test_CalculateHighestLowestTemp(unittest.TestCase):

    cal_high_low_temp = Calculations('/path/to', {'key', 'value'})
    file_handler = FileHandler()
    file = ['data/weatherfiles\\Murree_weather_2011_Jul.txt']

    input_data = file_handler.read_file(file)

    def test_valid_cal(self):
        excepted_data = [{'date': '2011-7-5', 'highest_temp': 25},
                         {'date': '2011-7-1', 'lowest_temp': 14},
                         {'date': '2011-7-25', 'highest_humidity': 100}]
        self.assertEqual(self.cal_high_low_temp.cal_highest_lowest(self.input_data), excepted_data)

    def test_invalid_cal(self):
        input_data = [[{'PK2': '2011-7-1', 'temperatureC': '22', 
                        'temperatureC': '18', 'min_temperatureC': '14',
                        'max_humidity': '86', 'mean_humidity': '74', 
                        'min_humidity': '51'}]]        
        with self.assertRaises(KeyError):
            self.cal_high_low_temp.cal_highest_lowest(input_data)
    

class Test_CalculateAverageHighestLowest(unittest.TestCase):
    
    avg_high_low_temp = Calculations('/path/to', {'key', 'value'})
    file_handler = FileHandler()
    file = ['data/weatherfiles\\Murree_weather_2011_Jul.txt']
    
    input_data = file_handler.read_file(file)
    
    
    def test_valid_avg(self):
        expected_data = [21,16, 77]
        self.assertEqual(self.avg_high_low_temp.cal_average_highest_lowest(self.input_data), expected_data)
    
    
    def test_invalid_avg(self):
        input_data = [[{'PK2': '2011-7-1', 'temperatureC': '22', 
                        'temperatureC': '18', 'min_temperatureC': '14',
                        'max_humidity': '86', 'mean_humidity': '74', 
                        'min_humidity': '51'}]] 
        with self.assertRaises(KeyError):
            self.avg_high_low_temp.cal_average_highest_lowest(input_data)
            

class Test_GetFileName(unittest.TestCase):
    
    file_handler = FileHandler()
    
    def test_valid_file(self):
        input_dir = 'data/weatherfiles'
        input_option ={'highest_lowest': '2011/7'}
        excepted_data = ['data/weatherfiles\\Murree_weather_2011_Jul.txt']
        
        self.assertEqual(self.file_handler.get_file_name(input_dir, input_option), excepted_data)
        
        
    def test_invalid_file(self):
        input_dir = 'data/weatherfiles'
        input_option ={'highest_lowest': '2011/7'}
        excepted_data = ['data/weatherfiles\\Murree_weather_2013_Jul.txt']
        self.assertNotEqual(self.file_handler.get_file_name(input_dir, input_option), excepted_data)
        
    
    def test_invalid_file(self):
        input_dir = 'data/weatherfiles'
        input_option = {'highest_lowest': '2011/7', 'average': '2011/7'}
        excepted_data = ['data/weatherfiles\\Murree_weather_2011_Jul.txt', 'data/weatherfiles\\Murree_weather_2011_Jul.txt']
        self.assertEqual(self.file_handler.get_file_name(input_dir, input_option), excepted_data)
        
    

class Test_ReadFile(unittest.TestCase):
    file_handler = FileHandler()
    
    def test_valid_read_file(self):
        input_data = ['data/weatherfiles\\Murree_weather_2011_Jul.txt']
        expected_data =self.file_handler.read_file(input_data)
        self.assertEqual(self.file_handler.read_file(input_data), expected_data)
        
    
    def test_invalid_read_file(self):
        input_data = ['data/weatherfiles\\Murree_weather_1999_Aug.txt']
        with self.assertRaises(FileExistsError):
            self.file_handler.read_file(input_data)
    
    def test_invalid_read_file(self):
        input_data = ['data/weatherfiles\\Murree_weather_2011_Aug.txt']
        expected_data =self.file_handler.read_file(input_data)
        
        self.assertEqual(self.file_handler.read_file(input_data), expected_data)
               
    
        
if __name__ == '__main__':
    unittest.main()