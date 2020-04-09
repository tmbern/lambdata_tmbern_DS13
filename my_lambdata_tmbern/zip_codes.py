import pandas
from uszipcode import Zipcode
from uszipcode import SearchEngine

class ZipCodes():
    """
    Takes a dataframe with Latitude and longitude as its inputs. 

    returns a dataframe with the corresponding zipcode for the given latitude and longitude

    """
    def __init__(self, my_df, my_latitude, my_longitude):
        self.my_df = my_df
        self.my_latitude = my_latitude
        self.my_longitude = my_longitude
        self.search = SearchEngine(simple_zipcode=True)

    # Could we pass this function inside the get_zip_code_df function?
    # def get_zip_code_list(self):
    #     self.zipcode,  = self.search.by_coordinates(lat=self.my_latitude, lng=self.my_longitude, radius=2, returns=1 )
    #     self.zipcode = self.zipcode.to_dict()
    #     self.zipcode = int(zipcode.get('zipcode'))
    #     return self.zipcode

    def get_zip_code_df(self):
        for index, row in self.my_df.iterrows():
            latitude = row.loc[self.my_latitude]
            longitude = row.loc[self.my_longitude]
            zipcode,  = self.search.by_coordinates(lat=latitude, lng=longitude, radius=2, returns=1 ) 
            zipcode = zipcode.to_dict()
            zipcode = int(zipcode.get('zipcode'))
            self.my_df.loc[index, 'zipcode'] = zipcode

        return(self.my_df)


if __name__ == "__main__":

    df = pandas.DataFrame(
        {"latitude": [33.885357, 40.648578, 40.690385, 33.885357],
        "longitude": [-117.266573, -111.846909, -111.804906, -117.266573]}
    )

    df = ZipCodes(df, 'latitude', 'longitude')
    print(df.get_zip_code_df())