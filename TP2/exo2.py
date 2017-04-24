def Q1(string) :
        entier = 0
        for i in range(len(string)):
                val = ord(string[i])
                entier += val * 256**(len(string)-1-i)
        print entier

def h(string) :
        a = Q1(string)
        a = a % 255
        print a

Q1("polB")
Q1("Blop")
