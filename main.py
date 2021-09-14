class Dog():
    def __init__(self, breed, name, spots):             #breed - параметр
        self.breed = breed                 #self.breed - атрибут
        self.name = name
        self.spots = spots


my_dog = Dog(breed='lab', name='Sammy', spots="NO SPOTS")                      #экземпляр класс
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)








