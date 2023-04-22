import sys
from bonjour_meowmeow import Cat

def main():
    Cat("".join(sys.argv[1:]))

if __name__ == "__main__":
       main()