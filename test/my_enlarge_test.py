from my_lambdata_tmbern.enlarge import enlarge

class TestEnlarge(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(enlarge(3), 300)


if __name__ == '__main__':
    unittest.main()