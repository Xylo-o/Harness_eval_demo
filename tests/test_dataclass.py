from dataclasses import dataclass

@dataclass
class Ksiazka:
    tytul: str
    strony: int

@dataclass
class Auto:
    moc: int
    kolor: str
    marka: str
    model: str
    cena: int