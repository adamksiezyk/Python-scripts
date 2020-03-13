import random

def split(word): 
    return [char for char in word]

key = {}
alphabet = split("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
nums = [n for n in range(10, 100)]
for l in alphabet:
    key[l] = [nums.pop(random.randint(0, len(nums)-1))]
    key[l].append(nums.pop(random.randint(0, len(nums)-1)))
    key[l].append(nums.pop(random.randint(0, len(nums)-1)))

def Code(s):
    global key

    s.upper()
    sentence = s.split(" ")

    words = []
    for w in sentence:
        words.append(split(w))

    Coded = []
    for w in words:
        codeword = ""
        for l in w:
            codeword += (str(key[l][random.randint(0, 2)]))
            codeword += " "
        Coded.append(codeword.strip())

    return Coded

def Decode(s):
    global key

    Decoded = ""
    # s[:] = [word.replace(" ", "") for word in s]
    for word in s:
        for letter in word.split(" "):
            letter = int(letter)
            for name, value in key.items():
                if letter in value:
                    Decoded += name
        Decoded += " "
    return Decoded

s = "PIERWSZA LABORKA Z BEZPIECZENSTWA JEST DZIS WIEC DZISIAJ LAMIEMY TAJNA WIADOMOSC"
coded = Code(s)
print(coded)
decoded = Decode(coded)
print(decoded)