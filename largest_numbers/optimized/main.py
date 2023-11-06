class LargestNumber:
    def get(self, lst, second=False):
        if isinstance(lst, list):
            largest_number = lst[0] if len(lst) > 0 else 0
            second_largest_number = -1
            for number in range(len(lst)):
                if lst[number] > largest_number:
                    second_largest_number, largest_number = largest_number, lst[number],
                index = number+1 if len(lst) < (number + 1) else number
                if lst[number] > lst[index] and second_largest_number < lst[index]:
                    second_largest_number = lst[index]
            if second:
                return second_largest_number
            return largest_number


largest_number_obj = LargestNumber()
print("second largest number", largest_number_obj.get(
    [2, 3, 4, 5, 346, 7], True))
# print("first_largest_number", largest_number_obj.get(
#     [2, 3, 4, 5, 6, 7]))
