para = "This is the department of ICT and it is located in the heart of the city"

newPara = para.lower().split()
print("Here are the words: ",newPara)

search = ['a','e','i','o','u','in','on','at','of','to','by','for','with','from']

for word in search:
    count = sum(w.count(word) if len(word) == 1 else w == word for w in newPara)
    print(f"Frequency of '{word}':{count}")