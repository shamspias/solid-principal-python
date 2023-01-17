from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Bird(Animal):
    def eat(self):
        pass
    def fly(self):
        pass

class Fish(Animals):
    def eat(self):
        pass
    def swim(self):
        pass
