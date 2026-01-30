import numpy as np

def input_show():
    try:
        row = int(input("Enter the how much row you want: "))
        col = int(input("Enter columns you want: "))

        if row <=0 or col <=0:
            print("Error, cannot enter less than 0 or equal to zero or strings, try again with int values!")
            return None, None
    
    except ValueError:
        print("Invalid input")
        return None, None

    return row, col

print("Different types of matrix by taking user_input")

while True:
    
    user_input = input("Enter what matrix would you like to create? zeros/ones/specific_number/sequence_number/identity_matrix/exit?").lower()

    if user_input == "zeros":
        print("Note this matrix will only contain zero element and no different number other than zero")
        row, col = input_show()
        if row is None or col is None:
            continue
        mat = np.zeros((row, col))
        print(mat)
        print("Matrix of zeroes created successfully!")

    elif user_input == "ones":
        print("Note this matrix will only contain ones element and no different number other than ones")
        row, col = input_show()
        if row is None or col is None:
            continue
        mat1 = np.ones((row, col))
        print(mat1)
        print("Matrix of ones created created successfully!")

    elif user_input == "specific_number":
        print("Note this matrix will only contain specific_number element and no different number other than specific_number entered")
        num = int(input("Enter the number you want in your matrix: "))
        row, col = input_show()
        if row is None or col is None:
            continue
        mat2 = np.full((row, col), num)
        print(mat2)
        print("Specific number matrix created successfully!")

    elif user_input == "sequence_number":
        start_num = int(input("Enter the start number: "))
        end_num = int(input("Enter the end number: "))
        step_size = int(input("Enter the step_size means how much difference should each number have between them ex.2 or 3: "))
        seq = np.arange(start_num, end_num, step_size)
        print(seq)
        print("Sequence generated successfully!")

    elif user_input == "identity_matrix":
        size = int(input("Enter the size of matrix ex.3: "))
        identity = np.eye(size)
        print(identity)
        print("your identity_matrix is generate sucessfully!")

    elif user_input == "exit":
        print("Programm is ended successfully!")
        break

    else:
        print("User entered wrong input, check options and try again!")