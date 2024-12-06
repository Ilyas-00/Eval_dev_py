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
