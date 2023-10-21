class BubbleSort(object):
    def start(self, lst):
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] > lst[j]:
                    lst[j], lst[i] = lst[i], lst[j]
        return lst


cases = [{
    "q": [1, 99, 8, 0, 2, 77],
    "a": [0, 1, 2, 8, 77, 99]
}]

bubble_sort = BubbleSort()
overall_passed_count = 0
for case in cases:
    sorted_result = bubble_sort.start(case["q"])
    result = sorted_result == case["a"]
    if result:
        print("Case is passed and result by program is:", sorted_result)
        overall_passed_count += 1
    else:
        print("Case Failed and result by program is:", sorted_result)
print(
    f"Total cases is {len(cases)} and Total passed is {overall_passed_count}")
if len(cases) == overall_passed_count:
    print("Good Job!")
else:
    print("better luck next time")
