from app.somar import Soma


def test_soma():
    n1 = 2
    n2 = 2

    assert Soma.calc(n1, n2) == 4
