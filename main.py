import pyttsx3
import random

def str_to_phonetic(c: str) -> str:
    mapping = {
        '0': "Zero",
        '1': "One",
        '2': "Two",
        '3': "Three",
        '4': "Four",
        '5': "Five",
        '6': "Six",
        '7': "Seven",
        '8': "Eight",
        '9': "Nine",
        'a': "Alpha",
        'b': "Bravo",
        'c': "Charlie",
        'd': "Delta",
        'e': "Echo",
        'f': "Foxtrot",
        'g': "Golf",
        'h': "Hotel",
        'i': "India",
        'j': "Juliet",
        'k': "Kilo",
        'l': "Lima",
        'm': "Mike",
        'n': "November",
        'o': "Oscar",
        'p': "Papa",
        'q': "Quebec",
        'r': "Romeo",
        's': "Sierra",
        't': "Tango",
        'u': "Uniform",
        'v': "Victor",
        'w': "Whiskey",
        'x': "X-Ray",
        'y': "Yankee",
        'z': "Zulu",
    }

    return ' '.join(map(lambda x: mapping[x], c.lower()))


class CallsignGenerator:

    def __init__(self):
        self.rand = random.Random()

    def gen_len(self):
        return self.rand.randint(4, 5)

    def gen_alphanum(self) -> str:
        rnd = self.rand.randint(0, 35)
        return chr(ord('0') + rnd) if rnd < 10 else chr(ord('a') + rnd - 10)

    def gen(self):
        return ''.join([self.gen_alphanum() for x in range(self.gen_len())])

def main():
    call_gen = CallsignGenerator()
    callsign = call_gen.gen()
    print(callsign.upper())

    engine = pyttsx3.init()
    engine.setProperty('rate', 250)
    engine.say(str_to_phonetic(callsign))
    engine.runAndWait()

if __name__ == '__main__':
    main()
