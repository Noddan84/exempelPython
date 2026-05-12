from calc import add, multiply


def test_add_positive():
    a, b = 2, 3
    result = add(a, b)
    print(f"\n[KÖR TEST]: Adderar positiva tal: {a} + {b}")
    print(f"[RESULTAT]: Fick {result}, förväntade mig 5")
    assert result == 5

def test_add_negative():
    a, b = -1, -1
    result = add(a, b)
    print(f"\n[KÖR TEST]: Adderar negativa tal: {a} + {b}")
    print(f"[RESULTAT]: Fick {result}, förväntade mig -2")
    assert result == -2

def test_add_mixed():
    a, b = -5, 10
    result = add(a, b)
    
    print(f"\n[KÖR TEST]: Adderar blandade tal: {a} + {b}")
    print(f"[RESULTAT]: Fick {result}, förväntade mig 5")
    assert result == 5

def test_multiply():
    a, b = 4, 5
    result = multiply(a, b)
    print(f"\n[KÖR TEST]: Multiplicerar: {a} * {b}")
    print(f"[RESULTAT]: Fick {result}, förväntade mig 20")
    assert result == 20