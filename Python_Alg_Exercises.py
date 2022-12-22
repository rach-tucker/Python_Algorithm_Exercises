#Exercise 1: Reverse the list below in-place using an in-place algorithm.

words = ['this' , 'is', 'a', 'sentence', '.']

def reverse_list(a_list):
    a_list[0], a_list[1], a_list[3], a_list[4] = a_list[4], a_list[3], a_list[1], a_list[0]
    return a_list

print(reverse_list(words))


#output ['.', 'sentence', 'a', 'is', 'this']
#bonus['.', 'ecentens', 'a', 'si' 'siht']

#Exercise 2: Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def word_count(somewords):
    a_list = somewords.split()
    d = {}

    for a in a_list:
        if a.lower() not in d:
            d[a.lower()] = 1
        else:
            d[a.lower()] += 1
    
    return d

print(word_count(a_text))


#Exercise 3: Write a function implementing a Linear Search Algorithm. A linear search is a method for finding an element within a list. It sequentially checks each element of the list until a match is found or the whole list has been searched. If you do not find a match, return -1


nums_list = [10,23,45,70,11,15]
nums_list.sort()
target = 70

# If number is not present return -1
#return statement like binary example

def lin_search(list_nums, target):
    for i in range(len(list_nums)):
        if list_nums[i] == target:
            return i
    return -1


print(lin_search(nums_list, 70))