#Recursive Python code for reversing a string

def reverse(st):
    if len(st) == 1:
        return st
    return reverse(st[1:]) + st[0]


st = input("Please give me a string! ")
st = reverse(st)
print("st is now " + st)

#Reversing a String using for loop

word = input(print("Enter word"))
reverse_word = ""
for i in range(len(word)-1,-1,-1):
  reverse_word = reverse_word + word[i]

print(reverse_word)  
