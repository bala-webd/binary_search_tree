from largest_number import LargestNumber


class SecondLargestNumber(LargestNumber):
    def get_second_largest_number(self, lst):
        if isinstance(lst, list):
            largest_number = self.get(lst)
            second_largest_number = -1
            for number in range(len(lst)):
                if second_largest_number < lst[number] and lst[number] < largest_number:
                    second_largest_number = lst[number]
            return second_largest_number
        return -1


second_largest_number = SecondLargestNumber()
print("second largest number",
      second_largest_number.get_second_largest_number([2, 3, 4, 5, 5678, 7]))
