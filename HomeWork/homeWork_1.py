class Robot:

    def __init__(self,name , color, work ):
    # 3 атрибута
        self.name = name
        self.color = color
        self.work = work
# методы, 1
    def action(self):
        return f'имя {self.name},цвет {self.color} профессия {self.work}'
#2
    def cooking(self):
        return f'{self} is cooking!'

    def working(self):
        return f'{self} is working!'

# 2 объекта
H12 = Robot("H12", "red", "cook")
P13 = Robot("P13", "blue"," builder")
print(H12.action())
print(P13.action())


