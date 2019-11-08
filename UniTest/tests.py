import unittest

class Mis_test(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(3+1,4)
        print('-------- complete test assertEqual --------')

    def test_resta(self):
        self.assertTrue(3+1 == 4)
        print('-------- complete test assertTrue ---------')


    if __name__ == '__main__':
        unittest.main()
