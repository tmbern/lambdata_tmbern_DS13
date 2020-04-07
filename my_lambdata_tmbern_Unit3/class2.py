# my_lambdata/class2.py

import pandas

def convert_names(dataframe):
    """
    create new column called"state name"
    Params dataframe (pandas.DataFrame) with column called "abbrev" which has state abbreviation
    
    
    """
    # Give: dataframe with column called "abbrev" which has state abbrev
    # Goal: create new column called"state name"

    df = dataframe.copy()

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

    # breakpoint()

    df['state_name'] = df['abbrev'].map(states)
    return df





if __name__ == "__main__":

# State abbreviation -> full name and visa versa
# FL -> Florida

    df = pandas.DataFrame({'abbrev': ['CT', 'CO', 'CA', 'TX']})
    full_df = convert_names(df) 
    print(full_df.head())

    df2= pandas.DataFrame({'abbrev': ['GA', 'NY', 'CA', 'CO']})
    full_df2 = convert_names(df2)
    print(full_df2.head())


    print('Hello World')
