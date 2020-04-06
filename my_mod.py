# Check a dataframe for nulls, print/report them in a nice "pretty" format:

def check_for_nulls(df):
    
    print(df.isnull().sum())

# Function to split dates ("MM/DD/YYYY", etc.) into multiple columns

def split_dates(df, column):
    
    df = df.copy()

    df['Month'] = df[column].dt.month
    df['Day'] = df[column].dt.day
    df['Year'] = df[column].dt.year

    return(df)