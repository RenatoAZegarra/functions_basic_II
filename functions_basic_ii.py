def countdown(num) :
    for i in range(num, -1, -1):
        print(i)
countdown(5)

def print_and_return(arr):
    print(arr[0])
    return arr[1]
print_and_return([1,2])

def first_plus_length(arr):
    sum = arr[0] + len(arr)
    print (sum)
    return sum
first_plus_length([1,2,3,4,5])

def  values_greater_than_second(arr):
    if len(arr) < 2:
        print(False)
        return False
    else:
        new_list = []
        for i in range(len(arr)):
            if i > arr[1]:
                new_list.append(i)
        print(new_list)
values_greater_than_second([5,2,3,2,1,4])
values_greater_than_second([3])

def length_and_value(size, value):
    return[value] * size
new_list = length_and_value( 4, 7)
print(new_list)
new_list = length_and_value(6,2)
print(new_list)
