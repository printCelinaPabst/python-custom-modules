# greetings.py
def say_hello(name):
    """Sagt Hallo zu einer Person."""
    # TODO 1: Implementiere die Begrüßungsnachricht.
    print("Hallo,", name + "!")
    pass

def say_goodbye(name):
    """Sagt Auf Wiedersehen zu einer Person."""
    # TODO 2: Implementiere die Abschiedsnachricht.
    print("Auf Wiedersehen,", name + "!")
    pass

#Eingabeaufforderung Name des Benutzers
name = input("Gib deinen Namen ein: ").strip().capitalize()

#Aufrufen der Funktionen say_hello und say_goodbye
say_hello(name)
say_goodbye(name)

