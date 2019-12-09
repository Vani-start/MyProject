import keyword

def CheckStr(val):
    if(keyword.iskeyword(val)):
        print("its a keyword")
    else:
        print("Its not a keyword")

val=str(input("Enter the string\n"))
CheckStr(val)