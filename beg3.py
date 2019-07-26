letter=["a","e","i","o","u"]
word=str(input("Enter a letter"))
for i in word:
    if i in letter:
        print("vowel")
    else:
        print("consonant")
