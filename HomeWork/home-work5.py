
def class_dexorator(cls):
    class new_class(cls):
       def new_method(self):
           if self.is_admin == True:
               return "база данных удалена"
           else:
               return "вы не являетесь админом"
    return new_class





@class_dexorator
class User:
    def __init__(self, name, is_admin=0):
        self.name = name
        self.is_admin = is_admin


    def delet_database(self):
       pass

andrey = User("andrey", True)
melisa = User("melisa", False)
print(andrey.new_method())
print(melisa.new_method())
