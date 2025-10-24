import time
from functools import lru_cache

print("Hello")
time.sleep(1)
print("World")

@lru_cache()
def surname(name: str = "Vova"):
    print(f"Hello {name}")
    return surname
x = "Hello Ilia"
    
if __name__ == "__main__":
    surname()
    print(x.cache_info())
