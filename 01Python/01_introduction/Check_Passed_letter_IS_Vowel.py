#------>>python program to test whether a passed letter ia a vowel or not

char=input("please enter the letter you want to check: ")
vowels=["a","i","o","u","e"]

if char.lower() in vowels:
    print("This letter is vowel")
else:
    print("This letter is consonant")