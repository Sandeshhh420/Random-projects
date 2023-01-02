class wordcounter:
    print("Welcome to word counter")
    a=input("Enter a sentence ")
    b=len(a.split())
    print("The original statement is "+ str(a))
    print("The number of words is "+ str(b))

class sentencecouter:
    print("This is a statement counter cause....... why not")
    a = input("A paragraph ")
    b=len(a.split("."))+len(a.split("?"))-2
    print("Number of statements is: "+ str(b))
    if b < 0:
        print("No statement has been entered")
    if b > 20:
        print("That's a lot of statement")
wordcounter()
sentencecouter()
