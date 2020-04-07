#Sets are unordered and not allow Duplicates
numbers={1,2,3,4,5,6}
print(numbers)
#casting List to set
list_numbers=[1,2,2,2,3,3,4,5,5,6,6]
print(list_numbers)
no_duplicate_set_numbers=set(list_numbers)
print(no_duplicate_set_numbers)
#casting Set to List
no_duplicate_list_numbers=list(no_duplicate_set_numbers)
print(no_duplicate_list_numbers)
movie_library_1={"bahubali","Magadheera","Maharshi"}
movie_library_2={"bahubali","Abilasha","Challenge"}
union_set=movie_library_1.union(movie_library_2)
print(union_set)
common_set=movie_library_1.intersection(movie_library_2)
print(common_set)
diff_set=movie_library_1.difference(movie_library_2)
print(diff_set)



