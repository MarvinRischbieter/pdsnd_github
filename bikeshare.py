import pandas as pd
import time

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
monthtuple = ["all", "January", "February","March","April","May","June","July","August","September","October","November","December"]
daytuple = ["all","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
citytuple=['chicago','new york city','washington']

monthtuple1 = ["all", "january", "february","march","april","may","june","july","august","september","october","november","december"]
daytuple1 = ["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:

        for x in citytuple:
            print(x)
        g1 = input("Enter for city : ")
        if g1.lower() in citytuple: # Check the file name
            break
        print("Invalid City")

    while True:

        for x in monthtuple:
            print(x)
        g2 = input("Enter for Month : ")
        if g2.lower() in monthtuple1: # Check the file name
            break
        print("Invalid Month")

    while True:

        for x in daytuple:

            print(x)
        g3 = input("Enter for Day of week : ")
        if g3.lower() in daytuple1: # Check the file name
            break
        print("Invalid Day of Week")
    result = [g1, g2, g3]
    return result
def load_data(rcity, rmonth, rday):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if rcity=="chicago":
        filepath="chicago.csv"
    elif rcity=="new york city":
        filepath="new york city.csv"
    elif rcity=="washington":
        filepath="washington.csv"
    else:
        print("Invalid City")
        return
    df = pd.read_csv(filepath, parse_dates=['StartTime'])
    df['Month'] = df['StartTime'].dt.month
    df['week'] = df['StartTime'].dt.dayofweek

    if ((monthtuple1.index(rmonth) >0) & (daytuple1.index(rday) >0)):
        rmonth = monthtuple1.index(rmonth)
        rday = daytuple.index(rday)-1
        df = df[(df['Month'] == rmonth) & (df['week'] == rday)]
        print("Empty Database")


    elif ((monthtuple1.index(rmonth)== 0) & (daytuple1.index(rday)>0)):
        rday = daytuple1.index(rday)-1

        df = df.loc[df.week == rday]

        print("Empty Database")


    elif((monthtuple1.index(rmonth)>0)&(daytuple1.index(rday)==0)):
        rmonth = monthtuple1.index(rmonth)

        df = df.loc[df.Month == rmonth]

        print("Empty Database")


    elif ((monthtuple1.index(rmonth) == 0) & (daytuple1.index(rday) == 0)):
        #df = df.drop(columns=['Month', 'day-of-week'])

        df=df


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    try:
        monthnumber=df['Month'].value_counts().idxmax()
        print(monthtuple[monthnumber])
    except:
        print("Empty Data")
        exit()

    # TO DO: display the most common day of week
    daynumber = df['week'].value_counts().idxmax()
    print(daytuple[daynumber])

    # TO DO: display the most common start hour
    starthour = df['StartTime'].value_counts().idxmax()
    print(starthour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    startstation = df['StartStation'].value_counts().idxmax()
    print(startstation)

    # TO DO: display most commonly used end station
    endstation = df['EndStation'].value_counts().idxmax()
    print(endstation)

    # TO DO: display most frequent combination of start station and end station trip
    df['comb'] = df['StartStation'].str.cat(df['EndStation'], sep="   ")

    combination = df['comb'].value_counts().idxmax()

    print(combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totaltime = df.loc['Total', 'TripDuration'] = df['TripDuration'].sum()
    print(str(totaltime)+" S")
    def convert(seconds):
        return time.strftime("%H:%M:%S", time.gmtime(totaltime))
    print(totaltime)

    # TO DO: display mean travel time
    meantime = df.loc['Total', 'TripDuration'] = df['TripDuration'].mean()
    print("%.2f" % meantime + " S")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats ...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print(df.groupby('UserType').size())
    except:
        print("No user type data")

    # TO DO: Display counts of gender
    try:
        print(df.groupby('Gender').size())
    except:
        print("No gender data in the database")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        recentyear = df['BirthYear'].max()

        print("%d" % recentyear)

        print("\nThis operation took %s seconds." % (time.time() - start_time))
    except:
        print("No data found.")
    print('-'*40)

def display_data(df):
    i=-5;k=0
    while True:
        restart = input('\n do you want to see raw data?(yes or no)\n')
        if restart.lower() != 'yes':
            break
        else:
            i=i+5;
            k=k+5;
            s = df.iloc[i:k]
            print(s)

def main():
    while True:

        result=get_filters()


        df = load_data(result[0], result[1], result[2])

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

