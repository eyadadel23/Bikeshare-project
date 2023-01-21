import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a whilechosen_city = input( loop to handle invalid inputs)

    city = input("Please Choose a City To Start,(Chicago,New york city,Washington)>: ").lower()
    while city not in CITY_DATA.keys():
        print("Invalid City, Please Check The Name And Try Again", "\U0001F605")
        city = input("Please Choose a City to Start,(Chicago,New york city,Washington)>: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april", "may", "june", "all"]
    month = input(
        "Please Choose a Month To Continue, You Can chose from:(January,february,march,april,may,june,all)>: ").lower()
    while month not in months:
        print("Iinvalid Month,Please Check The Name And Try Again", "\U0001F605")
        month = input(
            "Please Choose a Month To Continue, You Can chose from:(January,february,march,april,may,june,all)>: ").lower()
    else:
        print("Good choise!", "\U0001F600")
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

        days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]
        while True:
            day = input(
                "Please Choose a Day Name  To Continue, You Can Chose From(sunday,monday,tuesday,wednesday,thursday,friday,saturday,all)>: ").lower()
            if day in days:
                print("Good Choise!", "\U0001F600")
                break
            else:
                print("Invalid Day,Please Check The Name And True Again", "\U0001F605")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
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

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    df["start hour"] = df["Start Time"].dt.hour

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df["month"] == month]

    if day != "all":
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ["january", "february", "march", "april", "may", "june"]
    common_month = df["month"].mode()[0]
    print(f"The Most Common Month Is: {months[common_month - 1]}")

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print(f"The Most common Day Is: {common_day}")

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print(f"The Most Common Start Hour Is: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df["Start Station"].mode()[0]
    print(f"The Most Popular (Start) Station Is: {popular_start}")

    # TO DO: display most commonly used end station
    popular_end = df["End Station"].mode()[0]
    print(f"The Most Popular (End) Station Is: {popular_end}")

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end = df["Start Station"] + " To " + df["End Station"]
    print(f"The Most Frequent (Start And End Station) Is: from {popular_start_end.mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df["Trip Duration"].sum().round()
    print(f"The Total Travel Time Is: {total_travel}")

    # TO DO: display mean travel time
    avg_travel = df["Trip Duration"].mean().round()

    print(f"The Average Travel Time Is: {avg_travel}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The Count Of User Types: ", df["User Type"].value_counts())

    # TO DO: Display counts of gender
    if "Gender" in df:
        print("The Count Of Gender Is: ", df["Gender"].value_counts())
    else:
        print("No Gender Or Birth Year Information For The City Of (Washington)")

        # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_year = int(df["Birth Year"].min())
        print(f"The (Earliest) Year Of Birth Is: {earliest_year}")
        recent_year = int(df["Birth Year"].max())
        print(f"The Most (Recent) Year Of Birth Is: {recent_year}")
        mcommon_year = int(df["Birth Year"].mode()[0])
        print(f"The Most (Common) Year Of Birth Is: {mcommon_year}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df):
    # ASKING THE USER IF HE WANTS TO DISPLAY 5 ROWS OF THE DATA AND THEN PRINT 5 ROWS AT TIME.
    s = 0

    # user_answer = input("Do You Like To Display 5 Rows Of DATA: Yes / No: ").lower()
    pd.set_option("display.max_columns", None)

    while True:
        user_answer = input("Do You Like To Display 5 Rows Of DATA: Yes / No:> ").lower()
        if user_answer not in ["yes", "no"]:
            print("Invalid Answer,Please Type: Yes / No")
        elif user_answer == "yes":
            print(df[s:s + 5])
            s += 5
        elif user_answer == "no":
            print("Thank You For Your Time, And Have A Nice Day", "\U0001f600")
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
