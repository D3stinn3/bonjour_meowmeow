import sys
from src.bonjour_meowmeow import Bonjour

def main():
    Bonjour("".join(sys.argv[1:]))

if __name__ == "__main__":
       main()