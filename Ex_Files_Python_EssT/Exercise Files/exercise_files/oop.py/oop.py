class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"{self.name} says {sound}")

# Example usage
dog = Animal("Buddy", "Dog")
cat = Animal("Whiskers", "Cat")

dog.make_sound("Woof")
cat.make_sound("Meow")

def change_name(animal, new_name):
    animal.name = new_name
    return animal

dog.change_name('Max')
print(f'The dog\'s name is now {dog.name}')


    