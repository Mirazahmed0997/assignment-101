

list_of_numbs=[3,5,9,10,15,18,20,21]

filter_numb=list(filter(lambda x: x%3==0 and x%5!=0, list_of_numbs))

print(filter_numb)