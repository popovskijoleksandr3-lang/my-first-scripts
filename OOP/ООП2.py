class phone:
    def __init__(self,name,precent):
        self.name = name
        self.precent = precent
    def display(self):
        if self.precent > 0:
             self.precent = self.precent - 1
             print(f"Ви скористались телефоном у вас залишилось {self.precent} на телефоні {self.name}")
phone1=phone("Iphone 17 pro", 87)
phone1.display()
