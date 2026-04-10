def isMirror(numb):
    convertToStr= str(numb)
    splited_digit= list(map(lambda x: x.split(" "),convertToStr))

    stored_digits=[]
    for digits in reversed(splited_digit):
        stored_digits +=digits


    join= int("".join(stored_digits))

    if numb==join:
        print("Mirror number")
    else:
        print("Not a mirror number") 



isMirror(113)