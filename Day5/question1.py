#Write a function that takes a list of integers and returns a new list with duplicates removed, preserving original
#order (no set()).

#with set 
# takeList = [1,2,3,4,5,4,4,2,9,8]

# newList = set(takeList) #with set it manages the order too
# print(newList)



######
def remove_duplicates(numbers):
    new_list = []
    
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    
    return new_list


takeList = [1, 2, 3, 4, 5, 4, 4]
result = remove_duplicates(takeList)
print(result)



