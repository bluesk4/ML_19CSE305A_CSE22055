import numpy as np
def main():
    args = get_arguments()
    matrix_multiplication(*args)
    
def get_arguments():
    # getting matrix of values
    matrix = []
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    for row in range(0,rows):
        small_list = []
        for column in range(0,cols):
            number = int(input("Enter a number: "))
            small_list.append(number)
        matrix.append(small_list)
    # getting the power
    power = int(input("Enter the power: "))
    return [matrix,power]
    
def matrix_multiplication(matrix,power):
    result = np.linalg.matrix_power(matrix,power)
    print(result)
    
main()