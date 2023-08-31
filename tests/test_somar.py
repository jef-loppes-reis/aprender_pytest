from app.somar import Soma

def test_soma():
    v1 = 2
    v2 = 2

    assert Soma.calc(v1,v2) == 4