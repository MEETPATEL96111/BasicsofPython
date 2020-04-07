list1=[1,2,3,4,5]
list2=["one","two","three","four","five"]

#zipping
zipped=list(zip(list1,list2))
print(zipped)
#un Zipped
unzip=list(zip(*zipped))
print(unzip)

items=["Apples","oranges","Pineapples"]
counts=[3,2,1]
prices=[20,10,50]
sentences=[]
for item,count,price in zip(items,counts,prices):
    item,count,price=str(item),str(count),str(price)
    sentence="I bought "+count+" "+item+" at "+"Rs."+price+ "/-"+" Each"
    sentences.append(sentence)

print(sentences)