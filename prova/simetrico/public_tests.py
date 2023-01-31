import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global soma_simetricos
        undertest = __import__(module)
        soma_simetricos = getattr(undertest, 'soma_simetricos', None)

    def test_exemplo_1(self):
        assert soma_simetricos([2]) == [2]

    def test_exemplo_2(self):
        assert soma_simetricos([4, 5, 6, 5]) == [9, 11]
        
    def test_exemplo_3(self):
        assert soma_simetricos([12, 11, 11, 11, 33]) == [45, 22, 11]

    def test_exemplo_4(self):
        assert soma_simetricos([0, 2, 1, 22, 1, 2]) == [2, 3, 23]



if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
