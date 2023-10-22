class InsertionSort(object):
    def run(self, lst):
        for i in range(len(lst)):
            insertion_index = i
            for j in range(i-1, -1, -1):
                if lst[j] > lst[insertion_index]:
                    lst[insertion_index], lst[j] = lst[j], lst[insertion_index]
                    insertion_index = j
        return lst


perform_insertion_sort = InsertionSort()
print("after result", perform_insertion_sort.run([199, 0, 899, 7, 3]))
