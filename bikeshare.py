import time
import pandas as pd
import numpy as np

# picking up the data in csv files saved in the same folder as the python script.

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def takerequest():
    # Asks the user to specify a city, month and day to analyze.
    # Returns:
    # City - name of the city to analyze
    # Month - name of the month or all months to analyze
    # Day - name of the day or all days to analyze
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('\nHey...Let\'s explore US BikeShare data\n')
    while True:
        city = input('Select a city to explore data: chicago/new york city/washington:').lower()
        print(CITY_DATA[city])
        if city not in CITY_DATA:
            print('Please select a city from the list chicago/new york city/washington')
        else:
            break

    while True:
        month = input('Select a month from january/february/march/april/may/june OR "all" to get data for all months:').lower()
        print(month)
        if month != 'all' and month not in months:
            print('Please select a month from: january / february / march / april / may / june / all')
        else:
            break

    while True:
        day = input('Select a week sunday / monday / tuesday / wednesday / thursday / friday / saturday / all -> to get data for all days: ').lower()
        print(day)
        if day != 'all' and day not in days:
            print('please select a day from sunday / monday / tuesday / wednesday / thursday / friday / saturday / all')
        else:
            break
    return city, month, day


def loaddata(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def showdata(city):
    # Displays 5 records from the selected city."""
    # Asks user to type 'yes' or 'no' if user wants to see more record or not"""

    df = pd.read_csv(CITY_DATA[city])
    answers = ['yes', 'no']
    user_input = ''

    i = 0

    while user_input not in answers:
        print("\nshow first 5 data records : yes/no?")
        user_input = input().lower()

        if user_input == "yes":
            print(df.head())
        elif user_input not in answers:
            print("\ntype yes/no")

    while user_input == 'yes':
        print("\nshow more data?\n")
        i += 5
        user_input = input().lower()
        if user_input == "yes":
            print(df[i:i + 5])
        elif user_input != "yes":
            break


def showstats_time(city):
    # Displays stats on the most frequent times of travel"""

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Displays stats on the most popular month"""

    popularmonth = df['month'].mode()[0]
    print('Most popular month:', popularmonth)

    # Displays stats on the most popular day of the week"""

    popularday = df['day_of_week'].mode()[0]
    print('Most popular day of the week:', popularday)

    # Displays stats on the most popular hour of the day"""

    df['hour'] = df['Start Time'].dt.hour
    popularhour = df['hour'].mode()[0]
    print('Most popular hour of the day:', popularhour)

    print('\n')

def showstats_station(city):
    # Displays stats on the most popular stations and trip"""

    df = pd.read_csv(CITY_DATA[city])

    # Displays stats on the most popular start station"""

    popularstartStatn = df['Start Station'].mode()[0]
    print('Most popular station to start:', popularstartStatn)

    # Displays stats on the most popular end station"""

    popularendStatn = df['End Station'].mode()[0]
    print('most popular station to end:', popularendStatn)

    # Displays stats on the most popular trip from start to end station"""

    popular_start_and_end_Statn = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print('Most popular trip from start to end stations:', popular_start_and_end_Statn)

def showstats_tripduration(city):
    # Displays stats on the total and average trip duration"""

    df = pd.read_csv(CITY_DATA[city])

    # Displays stats on the total travel time for the trip"""

    total_time = df['Trip Duration'].sum()
    print('\nTotal Travel Time:',total_time / 3600, ' hours')

    # Displays stats on the average travel time for the trip"""

    avg_time = df['Trip Duration'].mean()
    print('Average Travel time:',  avg_time / 3600, ' hours')

    print('\n')

def showstats_user(city):
    # Displays stats on Bike share users

    df = pd.read_csv(CITY_DATA[city])

    # Displays count of users by type

    print('Count of users by type:\n', df['User Type'].value_counts());

    # Displays count of users by gender

    if 'Gender' in df:
        print('Counts of users by gender:\n', df['Gender'].value_counts())

    # Displays earliest birth year, recent birth year and popular birth year"""

    if 'Birth Year' in df:
        earliestbirthyear = int(df['Birth Year'].min())
        print('\n Earliest birth year :\n', earliestbirthyear)
        recentbirthyear = int(df['Birth Year'].max())
        print('\n most recent birth year:\n', recentbirthyear)
        popularbirthyear = int(df['Birth Year'].mode()[0])
        print('\n Most common year of birth:\n', popularbirthyear)

def bikeshare_stats():
    while True:
        city, month, day = takerequest ()
        df = loaddata (city, month, day)
        showdata (city)
        showstats_time (city)
        showstats_station (city)
        showstats_tripduration(city)
        showstats_user (city)
# Asks user if user wants to start analysis again?"""
        repeat = input('\nRepeat analysis again?: yes or no:\n')
        if repeat.lower() == 'no':
            break

bikeshare_stats()