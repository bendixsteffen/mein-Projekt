from src.anwendung import anzahl_woerter, anzahl_zeichen, haeufigste_woerter


def test_anzahl_woerter():
    assert anzahl_woerter("Hallo schöne Welt") == 3
    assert anzahl_woerter("") == 0


def test_anzahl_zeichen():
    assert anzahl_zeichen("a b") == 3
    assert anzahl_zeichen("a b", leerzeichen=False) == 2


def test_haeufigste_woerter():
    assert haeufigste_woerter("a b a c a b", n=2) == [("a", 3), ("b", 2)]
