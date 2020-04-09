# my_lambdata_tmber_Unit3/class3.py

import pandas
from datetime import datetime


# GOAL: inherit from DataFrame and create our own custom DF class



# class DataFrameProcessor():
class CustomFrame(pandas.DataFrame):
    """
    Params my_df (pandas.DataFrame) wiht column containing
    abbreviation of a state
    """
    # def __init__(self, my_df):

    #     self.df = my_df.copy()


    def convert_names(self):
        """
        create new column called "state name"
              
        
        """
        # Give: dataframe with column called "abbrev" which has state abbrev
        # Goal: create new column called"state name"

        

        states = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
    }

        self['state_name'] =  self['abbrev'].map(states)






if __name__ == "__main__":

# State abbreviation -> full name and visa versa
# FL -> Florida

    custom_df = CustomFrame({'abbrev': ['CT', 'CO', 'UT', 'CA', 'TX']})
    print(custom_df.head())

    custom_df.convert_names()
    print(custom_df.head())


    # df = pandas.DataFrame({'abbrev': ['CT', 'CO', 'UT', 'CA', 'TX']})
    # transformer = DataTransformer(df)
    # print(transformer.df.head())
    # transformer.convert_names()
    # print(transformer.df.head())


    # df2 = pandas.DataFrame({'abbrev': ['HI', 'TX', 'WA', 'FL', 'CA']})
    # transformer2 = DataTransformer(df2)
    # print(transformer2.df.head())
    # transformer2.convert_names()
    # print(transformer2.df.head())

