from filehandler import *
from datetime import datetime


class Calculations:
    def __init__(self, directory_path, options):
        '''
            @param directory_path, options: the directory path and options 
            @desc: this constructor will assign value to the object instance 
            @return: none
        '''
        self.directory_path = directory_path
        self.options = options

    def convert_date_format(self, date_str):
        '''
            @param date_str (str): A date string in the 'YYYY-MM-DD' format.
            @desc: Convert a date string from 'YYYY-MM-DD' format to 'Month Day' format.
            @return formatted_date: The formatted date string in 'Month Day' format, e.g., 'January 01'.
        '''
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%B %d')

        return formatted_date


    def print_highest_lowest(self, calculations):
        '''
            @param calculations: calculations contain highest, lowest temperature and humidity
            @desc: This function will print out the highest, lowest temperature and humidity
            @return: none
        '''                
        print('\n==========================================')
        print('Highest, Lowest, Temperature and Humidity')
        print('==========================================')
        for calculation in calculations:
            if 'highest_temp' in calculation:
                print(f"Highest: {calculation['highest_temp']}C on {self.convert_date_format(calculation['date'])}")
            elif 'lowest_temp' in calculation:
                print(f"Lowest: {calculation['lowest_temp']}C on {self.convert_date_format(calculation['date'])}")
            elif 'highest_humidity' in calculation:
                print(f"Humidity: {calculation['highest_humidity']}% on {self.convert_date_format(calculation['date'])}")


    def print_avg_highest_lowest(self, calculations):
        '''
            @param calculations: calculations contain average highest, lowest temperature and humidity
            @desc: This function will print out the average highest, lowest temperature and humidity
            @return: none
        '''                
        
        print('\n====================================================')
        print('Average of Highest, Lowest, Temperature and Humidity')
        print('====================================================')
        print(f'Highest Average: {calculations[0]}C')
        print(f'Highest Average {calculations[1]}C')
        print(f'Average Mean Humidity: {calculations[2]}%')
    
    
    
    def cal_highest_lowest(self, weather_data):
        '''
            @param weather_data: It as the data related to certain file 
            @desc: This function will calculate the highest, lowest temperature and humidity
            @return calculations: it has highest, lowest temperature and humidity
        '''                

        highest_temp = {'highest_temp': 0, 'date': ''}
        lowest_temp = {'lowest_temp': 1000, 'date': ''}
        highest_humidity = {'highest_humidity': 0, 'date': ''}
        

        for list in weather_data:
            for data in list:
                max_temp = data['max_temperatureC']
                min_temp = data['min_temperatureC']
                max_humidity = data['max_humidity']
                date = data['PKT']

                if max_temp:
                    max_temp = int(max_temp)
                    if max_temp > highest_temp['highest_temp']:
                        highest_temp['highest_temp'] = max_temp
                        highest_temp['date'] = date

                if min_temp:
                    min_temp = int(min_temp)
                    if min_temp < lowest_temp['lowest_temp']:
                        lowest_temp['lowest_temp'] = min_temp
                        lowest_temp['date'] = date

                if max_humidity:
                    max_humidity = int(max_humidity)
                    if max_humidity > highest_humidity['highest_humidity']:
                        highest_humidity['highest_humidity'] = max_humidity
                        highest_humidity['date'] = date

        calculations = [highest_temp, lowest_temp, highest_humidity]
        return calculations

    def cal_average_highest_lowest(self, weather_data):
        '''
            @param weather_data: It as the data related to certain file 
            @desc: This function will calculate the average  highest, lowest temperature and mean  humidity
            @return calculations: it has average highest, lowest temperature and mean humidity
        '''                
        
        highest_temp = 0
        lowest_temp = 0
        mean_humidity = 0
        
        count = 0
    
        for list in weather_data:
            count += 1
            for data in list:
                max_temp = data['max_temperatureC']
                min_temp = data['min_temperatureC']
                mean_humid = data['mean_humidity']
                
                highest_temp += int(max_temp)
                lowest_temp += int(min_temp)
                mean_humidity += int(mean_humid)
                count += 1
        
        avg_highest_temp = int(highest_temp / count)
        avg_lowest_temp = int(lowest_temp /count)
        avg_mean_humidity = int(mean_humidity /count)
        
        calculations = [avg_highest_temp, avg_lowest_temp, avg_mean_humidity]
        
        return calculations
                

    def draw_highest_lowest_chart(self, weather_data):
        '''
            @param weather_data: It as the data related to certain file 
            @desc: This function will draw the chart for the highest lowest temperaature
                    the highest temp will be red color and lowest will be blue color
            @return calculations: it has average highest, lowest temperature and mean humidity
        '''                

        # Define ANSI escape codes for red and blue text
        RED = '\033[91m'
        BLUE = '\033[94m'
        RESET = '\033[0m'

        # Extract the month and year from the weather data
        month = int(weather_data[0][0]['PKT'].split('-')[1])
        year = int(weather_data[0][0]['PKT'].split('-')[0])

        print('\n=======================================')
        print('Chart for Highest, Lowest, Temperature')
        print('=======================================')
        # Print the month and year
        print(f'{calendar.month_name[month]} {year}')

        # Iterate through the days and print the chart
        for day_data in weather_data[0]:
            day = int(day_data['PKT'].split('-')[2])
            highest_temp = int(day_data['max_temperatureC'])
            lowest_temp = int(day_data['min_temperatureC'])

            # Generate the bar chart for highest and lowest temperatures
            highest_chart = f'{RED}{"+" * highest_temp}{RESET}'
            lowest_chart = f'{BLUE}{"-" * lowest_temp}{RESET}'

            # Print the chart for the day
            print(f'{day:02d} {highest_chart} {highest_temp}C')
            print(f'{day:02d} {lowest_chart} {lowest_temp}C')


    def multiple_opt(self, directory_path, options):
        '''
            @param directory_path, options: directry path to the directory where are files
                                and options will ave multiples option to perform 
            @desc: This function will cal the multiple functions on the basis 
                                of the option because it has multiple options 
            @return: none
        '''                

        # reading file from FileHandler class
        file_data = FileHandler()
        weather_data = file_data.run_reading_file(directory_path, options)

        if 'highest_lowest' in options:
            high_low_data = []
            high_low_data.append(weather_data[0])
            calculations = self.cal_highest_lowest(high_low_data)
            self.print_highest_lowest(calculations)
            file_data.create_highest_lowest_report(calculations)
            
        if 'average' in options:
            avg_data = []
            avg_data.append(weather_data[1])
            calculations = self.cal_average_highest_lowest(avg_data)
            self.print_avg_highest_lowest(calculations)
            file_data.create_avg_report(calculations)
            
        if 'chart' in options:
            char_data = []
            char_data.append(weather_data[2])
            self.draw_highest_lowest_chart(char_data)
            file_data.create_chart_report(char_data)

    # run the calculations
    def run_calculations(self):
        '''
            @param: none 
            @desc: This function will cal the function base on the optons i.efor hifgest_lowest temp
                    average highest lowest temp, chart  or multiple options 
            @return: none
        '''                
        if self.options:
            if len(self.options) > 1:
                self.multiple_opt(self.directory_path, self.options)

            else:
                # reading file from FileHandler class
                file_data = FileHandler()
                weather_data = file_data.run_reading_file(self.directory_path, self.options)
                
                if 'highest_lowest' in self.options:
                    
                    # calculate, print to console and creating report 
                    calculations = self.cal_highest_lowest(weather_data)
                    self.print_highest_lowest(calculations)
                    file_data.create_highest_lowest_report(calculations)

                elif 'average' in self.options:
                    
                    # calculate, print to console and creating report 
                    calculations = self.cal_average_highest_lowest(weather_data)
                    self.print_avg_highest_lowest(calculations)
                    file_data.create_avg_report(calculations)

                elif 'chart' in self.options:

                    # Drawing chart and creating report
                    self.draw_highest_lowest_chart(weather_data)
                    file_data.create_chart_report(weather_data)
