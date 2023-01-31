import unittest
import sys

module = sys.argv[-1].split(".py")[0]


class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global trinca
        undertest = __import__(module)
        trinca = getattr(undertest, 'trinca', None)

    def test_example(self):
        l = [1, 7, 2, 8, 5, 3]
        assert trinca(l) == None
        assert l == [7, 8, 5]

    def test_exemplo2(self):
        l = [1, 3, 2, 7, 3, 2, 1]
        assert trinca(l) == None
        assert l == [7]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
