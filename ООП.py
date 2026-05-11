class Tank:
    def __init__(self, name,ammo):
        self.name = name
        self.ammo = ammo

    def Bk(self):
        if self.ammo > 0:
             self.ammo = self.ammo - 1
             print(f"Танк{self.name} вистрілив залишилось {self.ammo} снарядів")
        else:
            print("Закінчились снаряди")

tank1=Tank("Т80 БВМ",43)
tank1.Bk()
tank1.Bk()
tank1.Bk()
tank1.Bk()


