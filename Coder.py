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

    sentence = s.split(" ")

    words = []
    for w in sentence:
        words.append(split(w))

    code = []
    for w in words:
        codeword = ""
        for l in w:
            codeword += (str(key[l][0]))
            codeword += " "
        code.append(codeword)

    return code

def Decode(s):
    s[:] = [word.replace(" ", "") for word in s]
    for word in s:
        for letter in word:
            #TODO decode letter by letter


s = "PIERWSZA LABORKA Z BEZPIECZENSTWA JEST DZIS WIEC DZISIAJ LAMIEMY TAJNA WIADOMOSC"
coded = Code(s)
decoded = Decode(coded)