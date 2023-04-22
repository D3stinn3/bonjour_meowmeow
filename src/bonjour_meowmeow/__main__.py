import sys
from bonjour_meowmeow import bonjour

def main():
    bonjour("".join(sys.argv[1:]))

if __name__ == "__main__":
       main()