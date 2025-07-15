# greetings.py
def say_hello():
    """Sagt Hallo zu einer Person."""
    name = input("Gib deinen Namen ein: ").strip().capitalize()
    print("Hallo,", name + "!")
    pass

def say_goodbye():
    """Sagt Auf Wiedersehen zu einer Person."""
    name = input("Gib deinen Namen ein: ").strip().capitalize()
    print("Auf Wiedersehen,", name + "!")
    pass
 
if __name__ == "__main__":
    # Wird nur ausgeführt, wenn greetings.py direkt gestartet wird
    
    say_hello()
    say_goodbye()

