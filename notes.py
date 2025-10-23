# object oriented programming

# (define-struct dog [fur_color name age favorite_food]
class Dog:
        def __init__(self, breed, fur_color, name, age):
            self.breed = breed
            self.fur_color = fur_color
            self.name=name
            self.age=age
        def __str__(self) -> str:
            return f"{self.name} is a {self.age} year old {self.fur_color} {self.breed}"
        def bark(self):
            return f"{self.name} says woof woof"
if __name__ == "__main__":
    new_dog = Dog("beagle", "brown", "odie", "6")
    print (new_dog)
    print(new_dog.bark())