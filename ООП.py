class Dog:
    def __init__(self, name): # Тут ми приймаємо ім'я "з вулиці"
        self.name = name      # Тут ми кажемо: "Це ТВОЄ ім'я, запам'ятай його"

    def gav(self):
        # Ми кажемо self.name, щоб собака згадала, як її звати
        print(f"Привіт, я {self.name}")

dog1 = Dog("Рекс") # Спрацював __init__, тепер self.name = "Рекс"
dog1.gav()         # Собака дивиться в себе (self) і бачить там "Рекс"