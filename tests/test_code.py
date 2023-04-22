import sys
import unittest



from bonjour_meowmeow import Cat, Bonjour


class TestBonjour(unittest.TestCase):

    def test_bonjour(self):

        assert Bonjour()() == "Bonjour!"

    def test_meow(self):

        assert Cat("bonbon")() == "Meow, je suis le chat `bonbon`!"
