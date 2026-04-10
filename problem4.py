# line= input()
line=input()
lines=[]
lines.append(line)

splited_words= list(map(lambda x: x.split(" "),lines))

count= list(map(lambda x: len(x),splited_words[0]))

print(count)