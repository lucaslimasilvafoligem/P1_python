def test_exemplo_1():
        assert soma_simetricos([2]) == [2]

def test_exemplo_2():
        assert soma_simetricos([4, 5, 6, 5]) == [9, 11]

def test_exemplo_3():
        assert soma_simetricos([12, 11, 11, 11, 33]) == [45, 22, 11]

def test_exemplo_4():
        assert soma_simetricos([0, 2, 1, 22, 1, 2]) == [2, 3, 23]

def test_exemplo_5():
        assert soma_simetricos([1]) == [1]


