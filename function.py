def several_zeros():
    return [0] * 10

def several_zeros_custom(nb_zeros=10):
    return [0] * nb_zeros

def matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]

class Matrix:
    def __init__(self, rows, cols):
        self._matrix = [[0] * cols for _ in range(rows)]
        
    def get_value(self, row, col):
        return self._matrix[row][col]
    
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if len(self._matrix) != len(other._matrix) or len(self._matrix[0]) != len(other._matrix[0]):
            return False
        return all(self._matrix[i] == other._matrix[i] for i in range(len(self._matrix)))


if __name__ == '__main__':
    # test
    print(several_zeros())
    print(several_zeros_custom(5))
    print(matrix(3, 4))

    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    print(m1 == m2)  





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
