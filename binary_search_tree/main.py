total_numbers = int(input("Please enter how many numbers want to create?"))

to_search = []

for number in range(total_numbers):
    number_to_append = int(input("Enter Number: "))
    to_search.append(number_to_append)

to_search.sort()

target_number = int(
    input("Enter the number to search for findin the position of the number: "))


def perform_binary_search(to_search, target_number, lowest_index, highest_index):
    mid_index = (lowest_index + highest_index) // 2
    if lowest_index <= highest_index:
        if to_search[mid_index] == target_number:
            return mid_index
        elif to_search[mid_index] < target_number:
            return perform_binary_search(to_search, target_number, mid_index+1, highest_index)
        else:
            return perform_binary_search(to_search, target_number, lowest_index, mid_index-1)

    else:
        return -1


final_output = perform_binary_search(
    to_search, target_number, 0, len(to_search)-1)

if final_output == -1:
    print("Number not found in the number which you've entered please provide valid number")
else:
    print(f"{target_number} Number found at the position {final_output + 1}")
