class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    def bark(self):
        print('Dog is barking')
class Cat(Dog): 
    def meowing(self):
        print('cat is meowing')
class Janwar(Cat):
    def sleep(self):
        print('Janwar is sleeping ')

janwar = Janwar()
janwar.sleep()
janwar.meowing()
janwar.bark()
janwar.eat()


