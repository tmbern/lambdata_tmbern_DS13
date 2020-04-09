
from ..my_lambdata_tmbern.class3 import CustomFrame

def test_name_conversion():
    # self.assertEqual(enlarge(3), 300)
    custom_df = CustomFrame({'abbrev': ['CT', 'CO', 'UT', 'CA', 'TX']})
    # print(custom_df.head())
    assert custom_df.columns.tolist() == ["abbrev"]
    custom_df.convert_names()
    assert custom_df.columns.tolist() == ["abbrev", "state_name"]
    # custom_df.convert_names()
    # print(custom_df.head()) = 



