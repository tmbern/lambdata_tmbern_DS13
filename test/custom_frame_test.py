
import unittest
from ..my_lambdata_tmbern.class3 import CustomFrame

class TestCustomFrame(unittest.TestCase):

    def test_name_conversion(self):
        # self.assertEqual(enlarge(3), 300)
        custom_df = CustomFrame({'abbrev': ['CT', 'CO', 'UT', 'CA', 'TX']})
        # print(custom_df.head())
        self.assertEqual(custom_df.columns.tolist(), ["abbrev"])
        custom_df.convert_names()
        self.assertEqual(custom_df.columns.tolist(), ["abbrev", "state_name"])
        # custom_df.convert_names()
        # print(custom_df.head()) = 



if __name__ == '__main__':
    unittest.main()