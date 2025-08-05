def scitani(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Sčítá pouze čísla 😁")
    return a + b

def main():
    result = scitani(5, 3)

print("Výsledek: {result}")

if __name__== "__main__": main()