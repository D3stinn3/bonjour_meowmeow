import sys
import unittest

sys.path.append("..")

from src.bonjour_meowmeow import Bonjour, Cat


class TestBonjour(unittest.TestCase):

    def test_bonjour(self):

        assert Bonjour()() == "Bonjour!"

    def test_meow(self):

        assert Cat("bonbon")() == "Meow, je suis le chat `bonbon`!"
