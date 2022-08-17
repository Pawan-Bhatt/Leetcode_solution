class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ENG_to_MORSE = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.." }
        transform = lambda c: ENG_to_MORSE[c]   # use lambda function
        return len(Counter("".join(map(transform, word)) for word in words))
