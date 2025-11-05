# Базовые классы
class BaseCharacter:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Я персонаж {self.name}")

class BaseInActionCharacter(BaseCharacter):
    def perform_action(self):
        print(f"{self.name} выполняет действие!")

class BaseFunkoPop(BaseCharacter):
    def display(self):
        print(f"Это Funko Pop {self.name}")

class BaseHuman:
    def __init__(self, human_name):
        self.human_name = human_name
    
    def introduce_human(self):
        print(f"Я человек {self.human_name}")

class BaseCosplayer(BaseHuman):
    def __init__(self, human_name, character_name):
        super().__init__(human_name)
        self.character_name = character_name
    
    def cosplay(self):
        print(f"{self.human_name} косплеит {self.character_name}")

# Основные персонажи
class Shrek(BaseCharacter):
    def __init__(self):
        super().__init__("Шрек")

class PussinBoots(BaseCharacter):
    def __init__(self):
        super().__init__("Кот в сапогах")

class Donkey(BaseCharacter):
    def __init__(self):
        super().__init__("Осел")

class JackHorner(BaseCharacter):
    def __init__(self):
        super().__init__("Джек Хорнер")

# Персонажи в действии
class ShrekInAction(BaseInActionCharacter):
    def __init__(self):
        super().__init__("Шрек")

class PussinBootsInAction(BaseInActionCharacter):
    def __init__(self):
        super().__init__("Кот в сапогах")

class DonkeyInAction(BaseInActionCharacter):
    def __init__(self):
        super().__init__("Осел")

class JackHornerInAction(BaseInActionCharacter):
    def __init__(self):
        super().__init__("Джек Хорнер")

# Funko Pop
class ShrekFunkoPop(BaseFunkoPop):
    def __init__(self):
        super().__init__("Шрек")

class PussinBootsFunkoPop(BaseFunkoPop):
    def __init__(self):
        super().__init__("Кот в сапогах")

class DonkeyFunkoPop(BaseFunkoPop):
    def __init__(self):
        super().__init__("Осел")

class JackHornerFunkoPop(BaseFunkoPop):
    def __init__(self):
        super().__init__("Джек Хорнер")

# Косплееры
class ShrekCosplayer(BaseCosplayer):
    def __init__(self, human_name):
        super().__init__(human_name, "Шрек")

class PussinBootsCosplayer(BaseCosplayer):
    def __init__(self, human_name):
        super().__init__(human_name, "Кот в сапогах")

class DonkeyCosplayer(BaseCosplayer):
    def __init__(self, human_name):
        super().__init__(human_name, "Осел")

class JackHornerCosplayer(BaseCosplayer):
    def __init__(self, human_name):
        super().__init__(human_name, "Джек Хорнер")

# Проверка работы
print("=== Основные персонажи ===")
shrek = Shrek()
shrek.introduce()

puss = PussinBoots()
puss.introduce()

print("\n=== Персонажи в действии ===")
shrek_action = ShrekInAction()
shrek_action.introduce()
shrek_action.perform_action()

print("\n=== Funko Pop ===")
donkey_funko = DonkeyFunkoPop()
donkey_funko.introduce()
donkey_funko.display()

print("\n=== Косплееры ===")
shrek_cosplayer = ShrekCosplayer("Анна")
shrek_cosplayer.introduce_human()
shrek_cosplayer.cosplay()
    
    