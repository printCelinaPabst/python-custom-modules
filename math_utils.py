# math_utils.py
def add():
    """Addiert zwei Zahlen."""
    # TODO 3: Implementiere die Addition.
    a = int(input("Gib eine Zahl ein: "))
    b = int(input("Gib noch eine Zahl ein: "))
    addition = a + b
    print(f"{a} + {b} sind {addition}")

    pass

def subtract():
    """Subtrahiert zwei Zahlen."""
    # TODO 4: Implementiere die Subtraktion.
    a = int(input("Gib eine Zahl ein: "))
    b = int(input("Gib noch eine Zahl ein: "))
    subtraction = a - b
    print(f"{a} - {b} sind {subtraction}")

    pass

if __name__ == "__main__":
    # Wird nur ausgeführt, wenn greetings.py direkt gestartet wird
    
    add()
    subtract()
