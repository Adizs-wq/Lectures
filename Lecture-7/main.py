name: str = "Vova"

class Human_in_low:
    eyes: int = 2
    hands: int = 2
    legs: int = 2
    hair_color: str = "Brown"
    
    def blink():
        print(f"{name} blinked")

    def walk():
        print(f"{name} walked away")
        
if __name__ == "__main__":
    human1 = Human_in_low
    
    human1.blink()
    print(human1.eyes)