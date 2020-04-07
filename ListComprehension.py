names=["joe","jennifer","juliet"]
people=[]

for p in names:
    people.append(p)

print(people)

#List Comprehension
print([person for person in names])

l=[]
movie_ratings={"Bahubali":5,"Bahubali2":4,"kaidhino150":3,"syera":1}
for movie in movie_ratings:
    #print(movie)
    if movie_ratings[movie]>3:
        l.append(movie)

print(l)
#Comprehension
print([movie for movie in movie_ratings if movie_ratings[movie]<3])




