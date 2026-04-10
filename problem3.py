from collections import Counter


with open("data.txt","r") as file:
    file= file.readlines()
    content= list(map(str.strip,file)) 
    splited_words= list(map(lambda x: x.split(" "),content))

    marge_lists = splited_words[0]+splited_words[1]

    all_words=[]
    for words in marge_lists:
        word= words.lower().strip('.!?,')
        all_words.append(word)


total_count= Counter(all_words)
highest_count= total_count.most_common(1)
print(highest_count[0][0])
    