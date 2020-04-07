#mutable:Changable
#ex:
#list,
#Dictionaries


#immutable:Inchangeble
#ex:
#Tuple
#ints,floats,booleans
creditcard_Detail=("1432 5132 6578 1234","482",["Durgaprasad","phonenumber"])
print(creditcard_Detail)
#creditcard_Detail[0]="123 456 876 987" immutable
creditcard_Detail[2][0]="JyothiRani"
print(creditcard_Detail)