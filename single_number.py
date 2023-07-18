def get_unique_num(num_array: list) -> int:
    unique_num = 0
    for index in range(len(num_array)):
        unique_num = unique_num ^ num_array[index]
    return unique_num


try:
    nums_array = list(map(int, input("Enter integers separated by space : ").split()))
    print(f"The unique number in {nums_array} is : ", get_unique_num(nums_array))
except ValueError:
    print("Invalid input. Please enter only integers.")
