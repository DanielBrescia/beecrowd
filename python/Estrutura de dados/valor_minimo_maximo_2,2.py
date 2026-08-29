def min_max_in_array(array):

    if len(array) == 0:
        raise Exception ('Lista vazia')
    min_index = 0
    max_index = 0
    for index in range(1, len(array)):
        if array[index] < array[min_index]:
            min_index = index
        elif array[index] > array[max_index]:
            max_index = index
    return array[max_index], array[min_index]

array = [9,7,5,3,1,2,4,6,8,10]
print(min_max_in_array(array))