class Cat:

    def __init__(self, name):
        self.name = name

    def __call__(self):
        return f"Meow, je suis le chat `{self.name}`!"
