class LargestNumber:
    def get(self, lst):
        if isinstance(lst, list):
            largest_number = lst[0]
            for number in range(len(lst)):
                if lst[number] > largest_number:
                    largest_number = lst[number]
            return largest_number
        return -1


# largest_number = LargestNumber()
# print(largest_number.get([33, 2, 3, 4, 4, 4, 4, 4944, 4, 4, 4, 4, 4, 12]))
