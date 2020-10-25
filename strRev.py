#Recursive Python code for reversing a string

def reverse(st):
    if len(st) == 1:
        return st
    return reverse(st[1:]) + st[0]


st = input("Please give me a string! ")
st = reverse(st)
print("st is now " + st)

