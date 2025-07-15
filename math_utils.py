# math_utils.py
def add(a, b):
    """Addiert zwei Zahlen."""
    # TODO 3: Implementiere die Addition.
    addition = a + b
    return addition
    pass

def subtract(a, b):
    """Subtrahiert zwei Zahlen."""
    # TODO 4: Implementiere die Subtraktion.
    subtraction = a - b
    return subtraction
    pass

#Eingabe des Benutzers
eingabe_zahl1 = int(input("Gib eine Zahl ein: "))
eingabe_zahl2 = int(input("Gib noch eine Zahl ein: "))

addition = add(eingabe_zahl1, eingabe_zahl2)
subtraction = subtract(eingabe_zahl1, eingabe_zahl2)

print(f"{eingabe_zahl1} + {eingabe_zahl2} sind {addition}")
print(f"{eingabe_zahl1} - {eingabe_zahl2} sind {subtraction}")
