def compute(a,b):  
    try:
        division_numb=a-b
        print(((a*a)+(b*b)/division_numb))
        return ((a*a)+(b*b)/division_numb)
    except ZeroDivisionError:
        print("division_number is zero")
    finally:
        print("Operation completed")


compute(2,2)        