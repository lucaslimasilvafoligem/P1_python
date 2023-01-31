import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global inverte3a3
        undertest = __import__(module)
        inverte3a3 = getattr(undertest, 'inverte3a3', None)

    def test_1(self):
        assert inverte3a3("abcdef") == "defabc"
    def test_2(self):
        assert inverte3a3("abcdefghijkl") == "jklghidefabc"
    def test_3(self):
        assert inverte3a3("paisimtio") == "tiosimpai"

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
