from abc import abstractmethod


class BaseDuck:
    wings: int = 2
    
    
    @abstractmethod
    def make_noise(self,voleme_do: int) -> None:
        print(f"quack {voleme_do}")
    
class Duck(BaseDuck):
    pass


if __name__ == "__main__":
    d = Duck()
    d.make_noise(12)