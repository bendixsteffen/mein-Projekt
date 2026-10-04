"""Kleine Textanalyse: Wörter, Zeichen, häufigste Wörter."""
import re
from collections import Counter


def woerter(text: str) -> list[str]:
    """Zerlegt einen Text in Kleinbuchstaben-Wörter."""
    return re.findall(r"[\wäöüß]+", text.lower())


def anzahl_woerter(text: str) -> int:
    return len(woerter(text))


def anzahl_zeichen(text: str, leerzeichen: bool = True) -> int:
    return len(text) if leerzeichen else len("".join(text.split()))


def haeufigste_woerter(text: str, n: int = 3) -> list[tuple[str, int]]:
    return Counter(woerter(text)).most_common(n)


if __name__ == "__main__":
    beispiel = "Das ist ein Test. Ein Test ist gut, das Ergebnis ist gut."
    print("Wörter:", anzahl_woerter(beispiel))
    print("Zeichen:", anzahl_zeichen(beispiel))
    print("Häufigste:", haeufigste_woerter(beispiel))
