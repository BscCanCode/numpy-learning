import numpy as np

print("This is aggregate function code")

array = np.array([23,45,65,34,76,87])
print(f"This is the array on which you will perform aggregate functions!\n{array}")

while True:
    user_input = input("Enter what would you like to perform?\nsum\nmean\nmax\nmin\nstd\nvar\nexit\nuser_input: ").lower()
    if user_input == "sum":
        value = np.sum(array)
        print("The sum of the array is: ", value)
    
    elif user_input == "mean":
        print("The mean of the array is: ", np.mean(array))

    elif user_input == "max":
        print("The maximum element in array is: ", np.max(array))
    
    elif user_input == "min":
        print("The minimum element in array is: ", np.min(array))

    elif user_input == "std":
        print("The standard_deviation of array is: ", np.std(array))

    elif user_input == "var":
        print("The variance of array is: ", np.var(array))

    elif user_input == "exit":
        print("The program is exit successfull!")
        break
    else:
        print("Wrong input, enter proper input and try again!")
