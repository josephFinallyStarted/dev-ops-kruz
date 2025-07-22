def scitani(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Sčítá pouze čísla 😁")
    return a + b