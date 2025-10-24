class MixinSpeakable:
    
    def speak():
        print(f"This character can speak")
        
class MixinAnimated:
    anime: bool = True
    def is_animated(self):
        print(f"Yea, this {self.anime}")
        
class MixinFunny:
    
    def make_laugh():
        print("Yea, its funny")
        
class BaseCharacter(MixinSpeakable,MixinAnimated,MixinFunny):
    name1: str = "Shrek"
    name2: str = "PussinBoots"
    name3: str = "Donkey"
    name4: str = "JackHorner"
    
    