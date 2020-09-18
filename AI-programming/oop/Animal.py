class Animal:
    sounds = ["..."]

    def __init__(self, name, age):
        self.name = name
        self.age  = age
        # cloning the class attribute, so that when we make changes to it,
        # we won't affect the other Animal instances
        self.sounds = self.sounds[:]

    def __str__(self):
        return "{} ({} years old)".format(self.name, self.age)

    def make_sounds(self):
        sounds_string = ""
        for sound in self.sounds:
            sounds_string += sounds + " "
        print("{} : {}".format(self.name, sounds_string))


a = Animal("kiki", 3)
print(a)
