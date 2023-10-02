import os
import fnmatch
import csv
import calendar
from datetime import datetime


class FileHandler:
    def __init__(self):
        '''
            @param :none
            @desc: this is a constructor  clled when obj is created 
            @return: none
        '''
        # self.directory_path = directory_path
        # self.options = options

    def convert_date_format(self, date_str):
        '''
            @param date_str (str): A date string in the 'YYYY-MM-DD' format.
            @desc: Convert a date string from 'YYYY-MM-DD' format to 'Month Day' format.
            @return formatted_date: The formatted date string in 'Month Day' format, e.g., 'January 01'.
        '''
        
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%B %d')

        return formatted_date
    
    
    def get_file_name(self, directory_path, options):
        '''
            @param directory_path, options: the directory path and options 
            @desc: It will search the given file in a specified directory 
            @return matches_file: it will have the files specified in options 
        '''

        # checking if the directory exist
        if not os.path.exists(directory_path):
            print(f"Directory '{directory_path}' does not exist.")
            return None

        matching_files = []

        for option, value in options.items():
            # Extract the year and month from the option value
            year, month = map(int, value.split('/'))

            # Triming the month number to a three-letter month abbreviation
            month_abbr = calendar.month_abbr[month][:3]

            # Generate a pattern for the filename based on the year and month abbreviation
            filename_pattern = f'Murree_weather_{year}_{month_abbr}.txt'

            # Search for files in the directory that match the pattern
            for root, _, files in os.walk(directory_path):
                for filename in fnmatch.filter(files, filename_pattern):
                    matching_files.append(os.path.join(root, filename))

        return matching_files


    def read_file(self, file_name_list):
        '''
            @param file_name_list: it will have the name of the files to read data from 
            @desc: It will read data from the files or file and store it in a list as object 
            @return weather_data_list: it will have the list of list that has the object
                        of data fro the files 
        '''
        
        weather_data_list = []

        for file_name in file_name_list:
            weather_daily_data = []  # Initialize a list for data from each file
            try:
                with open(file_name, 'r') as file:
                    csvreader = csv.DictReader(file)
                    for row in csvreader:
                        try:
                            # Check if any of the required fields are empty and skip the row if any are empty
                            if (
                                row['PKT'] and
                                row['Max TemperatureC'] and
                                row['Mean TemperatureC'] and
                                row['Min TemperatureC'] and
                                row['Max Humidity'] and
                                row[' Mean Humidity'].strip() and
                                row[' Min Humidity'].strip()
                            ):
                                selected_data = {
                                    'PKT': row['PKT'],
                                    'max_temperatureC': row['Max TemperatureC'],
                                    'mean_temperatureC': row['Mean TemperatureC'],
                                    'min_temperatureC': row['Min TemperatureC'],
                                    'max_humidity': row['Max Humidity'],
                                    'mean_humidity': row[' Mean Humidity'].strip(),
                                    'min_humidity': row[' Min Humidity'].strip()
                                }
                                weather_daily_data.append(selected_data)
                        except KeyError as e:
                            print(f'Error reading row in file {file_name}: {e}')
            except FileNotFoundError as e:
                print('\n\nerror\n\n\n')
                print(f'Error opening file {file_name}: {e}')

            weather_data_list.append(weather_daily_data)  # Append the daily data list to the main list

        return weather_data_list


    def run_reading_file(self, directory_path, options):
        '''
            @param directory_path, options: the directory path and options 
            @desc: It will call the get file name function and get the file
                    name and read data from files 
            @return weather_data: weather data from the file
        '''

        weather_data = []
        # getting file name
        file_name_list = self.get_file_name(directory_path, options)
        weather_data = self.read_file(file_name_list)

        return weather_data
    
    
    def create_avg_report(self, calculations):
        '''
            @param calculations: calculations contain average highest, lowest temperature and humidity
            @desc: It will open the file and write the calculation 
            @return: none 
        '''
        
        try:        
            with open('reports/average_reports.txt', 'a') as file:
                file.write('Report for average highest temperature, lowest temperature, and  mean humidity.\n')
                file.write(f'Highest Average: {calculations[0]}C\n')
                file.write(f'Lowest Average {calculations[1]}C\n')
                file.write(f'Average Mean Humidity: {calculations[2]}%\n\n')
                
        except FileNotFoundError as e:
            print('\n\nerror\n\n\n')
                
            
    
    def create_highest_lowest_report(self, calculations):
        '''
            @param calculations: calculations contain highest, lowest temperature and humidity
            @desc: It will open the file and write the calculation 
            @return: none 
        '''
        
        try:        
            with open('reports/highest_lowest_reports.txt', 'a') as file:
                file.write('Report for highest temperature, lowest temperature and humidity.\n')
                for calculation in calculations:
                    if 'highest_temp' in calculation:
                        file.write(f"Highest: {calculation['highest_temp']}C on {self.convert_date_format(calculation['date'])}\n")
                    elif 'lowest_temp' in calculation:
                        file.write(f"Lowest: {calculation['lowest_temp']}C on {self.convert_date_format(calculation['date'])}\n")
                    elif 'highest_humidity' in calculation:
                        file.write(f"Humidity: {calculation['highest_humidity']}% on {self.convert_date_format(calculation['date'])}\n\n")
                        
        except FileNotFoundError as e:
            print('\n\nerror\n\n\n')
                    
                    
    def create_chart_report(self, weather_data):
        '''
            @param weather_data: data from specific file 
            @desc: It will create the chart and then write the chart to the file 
            @return: none 
        '''        
        
        # Extract the month and year from the weather data
        month = int(weather_data[0][0]['PKT'].split('-')[1])
        year = int(weather_data[0][0]['PKT'].split('-')[0])


        try:
            with open('reports/chart_reports.txt', 'a') as file:
                
                file.write(f'Report for Month : {calendar.month_name[month]} {year}\n')
                # Iterate through the days and print the chart
                for day_data in weather_data[0]:
                    day = int(day_data['PKT'].split('-')[2])
                    highest_temp = int(day_data['max_temperatureC'])
                    lowest_temp = int(day_data['min_temperatureC'])

                    # Generate the bar chart for highest and lowest temperatures
                    highest_chart = f'{"+" * highest_temp}'
                    lowest_chart = f'{"-" * lowest_temp}'

                    # Print the chart for the day
                    file.write(f'{day:02d} {highest_chart} {highest_temp}C\n')
                    file.write(f'{day:02d} {lowest_chart} {lowest_temp}C\n')
                
                file.write('\n')
        except FileNotFoundError as e:
            print('\n\nerror\n\n\n')

            
