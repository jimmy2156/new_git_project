def sum_array(arr):
    #your code here
    highest_number = max(arr)
    lowest_number = min(arr)
    total = 0
    for number in arr:
        if number < highest_number and number > lowest_number:
            total = total + number
            
    return total


#arr = { 6, 2, 1, 8, 10 } 
arr = { 1, 1, 11, 2, 3 }
print("hello world")
print("welocome to this library")