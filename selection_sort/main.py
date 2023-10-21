class SelectionSort(object):
    def selection_sort(self, lst):
        for i in range(len(lst)):
            min_index = i
            for j in range(i+1, len(lst)):
                if lst[min_index] > lst[j]:
                    min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
        return lst


cases = [{
    "q": [1, 2, 15, 0, 8],
    "a": [0, 1, 2, 8, 15]
}]

for case in cases:
    selection_sort_obj = SelectionSort()
    # if selection_sort_obj.selection_sort(case["q"]) == case["a"]:
    #     print("case is passed")
    # else:
    print("List object is not passing",
          selection_sort_obj.selection_sort(case["q"]))


# for i in range(len(lst)):
#             length_lst = len(lst)
#             # comparison_element = i
#             # target_index = 0
#             # if i == len(lst)
#             print(
#                 f"lst of i --> {lst[i]} || lst --> {lst} || short array with i replaced [{i}] --> {lst[i+1:len(lst)]}")
#             # print(f"i ---> {i} and list is {lst}")
#             for j in range(len(lst[i+1:length_lst])):
#                 k = i + j
#                 # print(f"i is {i} and k is {k}")
#                 if k >= length_lst:
#                     k = length_lst - 1
#                 if lst[i] > lst[k]:
#                     temp = lst[i]
#                     lst[i] = lst[k]
#                     lst[k] = temp
#                     # if i == length_lst:
#                     #     print(
#                     #         f"inside swapping index {i} splitted Array {lst[i+1:len(lst)]} and lst[j] is {lst[j]} and lst is is greater than lstj", lst)
#                     continue
#                     # print(
#                     #     f"else inside swapping index {i} splitted Array {lst[i+1:len(lst)]} and lst[j] is {lst[j]} and lst is is greater than lst[j] {lst[i] > lst[j]}", lst)
