digits=[0,1,2,3,4,5,6,7,8,9]
print(digits)
#indexing
print(digits[0])
#negitive Indexing
print(digits[-1])
#slicing
print(digits[:3])
print(digits[0:3])
print(digits[:-1])
#Striding
print(digits[0:10:1])
print(digits[0:10:2])
print(digits[::1])
print(digits[::1])
print(digits[::-1])#Reverse Array

for i  in range(len(digits)):
    print(digits[0:i])
window_size=3;
for i in range(len(digits)-(window_size-1)):
    print(digits[i:i+window_size])#Slicing

