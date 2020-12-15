# import required packages
import os
import unittest

# import function
from csv_reader import read_data


class TestCSVReader(unittest.TestCase):

    '''Test the code.'''
    # create temporary file
    def setUp(self):
        self.temporary_file = '/tmp/temporary_file'
        f = open(self.temporary_file, 'w')
        f.close()

    # test wrong input
    def test_no_datafile(self):
        df = read_data('XX')
        self.assertFalse(df)

    # test empty input
    def test_empty_datafile(self):
        df = read_data(self.temporary_file)
        self.assertFalse(df)

    # test wrong file extension
    def test_file_is_not_csv(self):
        df = read_data(self.temporary_file)
        self.assertFalse(df)

    # remove temporary file after testing
    def tearDown(self):
        os.remove(self.temporary_file)


if __name__ == '__main__':
    unittest.main(verbosity=2)
