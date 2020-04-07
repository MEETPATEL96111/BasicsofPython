#ordered key value pairs
contacts={
    "Jyothirani":{"phonenumber":7731808882,"email":'g.s.jyothirani'},
    "Prasad":{"phonenumber":7731808882,"email":'durgaprasad888@gmail.com'}
}
print(contacts["Jyothirani"])

sentence="i like the jishnav because the name jishnav is the best"
word_count={
    "i":1,
    "jishnav":2,
    "like":1,
    "the":3,
    "because":1,
    "name":1,
    "is":1
    }
#get list of tuples of key value
print(list(word_count.items()))
#get list of keys
print(list(word_count.keys()))
#get list of vaules
print(list(word_count.values()))
#Add an item into dictionary
print()
print(word_count)
word_count["best"]=1
print(word_count)
#Delete an item from dictionary
print(word_count)
print()
word_count.pop("the")
print(word_count)
#Delet last item
print(word_count.popitem())
print(word_count)