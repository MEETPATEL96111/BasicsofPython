#tuple
#its more secure than list we cannot change
#items in tuple
#[]-->List
#()-->Tuple
person1=("Durgaprasad",37,"Biriyani")
person2=("Jyothi",35,"FriedRice")
person3=("Jishnav",2,"chapathi")

family=[person1,person2,person3]
# packing and un packing the tuples
for name,age,favfood in family:
    print(name)
    print(age)
    print(favfood)
    print()