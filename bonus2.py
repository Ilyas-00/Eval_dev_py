def my_sort(my_list: [int]) -> [int]:
    list_copy = my_list[:]
    
    list_length = len(list_copy)
    
    for i in range(list_length):
        for j in range(list_length - i - 1):
            if list_copy[j] > list_copy[j + 1]:
                list_copy[j], list_copy[j + 1] = list_copy[j + 1], list_copy[j]
    
    return list_copy


if __name__ == '__main__':
    my_list = [15, 99, 8, 42, 1, 57, 33]
    sorted_list = my_sort(my_list)
    print("Liste triée :", sorted_list)
