import unittest
import pandas
from my_lambdata_tmbern.split_dates import SplitDates

class TestSplitDates(unittest.TestCase):



    def test_is_dataframe(self):
        custom_df = pandas.DataFrame({"Date": ['01/01/2020', '01/03/2020', '01/05/2020', '01/05/2020']})
        self.assertIsInstance(custom_df, pandas.DataFrame)
    



    def test_split_dates(self):
        custom_df = pandas.DataFrame({"Date": ['01/01/2020', '01/03/2020', '01/05/2020', '01/05/2020']})
        custom_df = SplitDates(custom_df, 'Date')
        self.assertEqual(custom_df.split_dates().columns.to_list(), ['Date', 'Month', 'Day', 'Year'])


if __name__ == '__main__':
    unittest.main()