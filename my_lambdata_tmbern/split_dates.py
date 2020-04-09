import pandas


class SplitDates():
    """
    takes a dataframe with column of dates and returns new columns of year,
    month, and day.
    """
    def __init__(self, my_df, my_column):
        self.my_df = my_df
        self.my_column = my_column

    def split_dates(self):

        # # create a copy to prevent copy warnings
        # df = dataframe.copy()

        # convert the column to a date time format
        self.my_df[self.my_column] = pandas.to_datetime(self.my_df[self.my_column], infer_datetime_format=True)

        # create new columns for the month day and year
        # of the given date column
        self.my_df['Month'] = self.my_df[self.my_column].dt.month
        self.my_df['Day'] = self.my_df[self.my_column].dt.day
        self.my_df['Year'] = self.my_df[self.my_column].dt.year

        return(self.my_df)





if __name__ == "__main__":

    df = pandas.DataFrame({"Date": ['01/01/2020', '01/03/2020', '01/05/2020', '01/05/2020']})

    df = SplitDates(df, 'Date')
    
    print(df.split_dates().head())
    print(df.split_dates().columns.to_list())