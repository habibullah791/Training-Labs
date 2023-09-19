import argparse
from calculations import *


class WeatherApp:
    def __init__(self, directory_path, options):
        self.directory_path = directory_path
        self.options = options


    # running app calling calculations class
    def run_app(self):
        Cal = Calculations(directory_path, options)
        Cal.run_calculations()


if __name__ == "__main__":
    
    """
        Weather Man Application provide the following functionality

        Arguments:
            file_path (str): Path to the weather data directory.
            -e, --highest_lowest (str): Year for generating the highest and lowest temperature report.
            -a, --average (str): Month for generating the average temperature and humidity report.
            -c, --chart (str): Month for generating a temperature chart.
    """

    parser = argparse.ArgumentParser(description="Weather Man Application")
    parser.add_argument("file_path", help="Path to the weather data directory")
    parser.add_argument("-e", "--highest_lowest", type=str, help="Year for highest and lowest temperature report")
    parser.add_argument("-a", "--average", type=str, help="Month for average temperature and humidity report")
    parser.add_argument("-c", "--chart", type=str, help="Month for temperature chart")

    args = parser.parse_args()
    directory_path = args.file_path

    options = {}

    if args.highest_lowest:
        options['highest_lowest'] = args.highest_lowest

    if args.average:
        options['average'] = args.average

    if args.chart:
        options['chart'] = args.chart



# main class instance 
    app = WeatherApp(directory_path, options)
    app.run_app()
