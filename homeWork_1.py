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
    def cooking(H12):
        return f'{H12} is cooking!'

    def working(P13):
        return f'{P13} is working!'

# 2 объекта
H12 = Robot("H12", "red", "cook")
P13 = Robot("P13", "blue"," builder")
print(H12.action())
print(P13.working())
