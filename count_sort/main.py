import time


class CountSort(object):
    def run(self, lst):
        max_number = self.find_max_number(lst)
        count_list = self.zero_initializer(max_number)
        for i in range(len(lst)):
            count_list[lst[i]] += 1
        count_list = self.perform_cumulative_sum(count_list)
        output_array = self.zero_initializer(len(lst) - 1)
        for element in range((len(lst))-1, -1, -1):
            count_list_value = count_list[lst[element]]
            output_array[count_list_value - 1] = lst[element]
        return output_array

    def perform_cumulative_sum(self, count_list):
        for index, _ in enumerate(count_list):
            if index > 0:
                count_list[index] += count_list[index - 1]
        return count_list

    def zero_initializer(self, list_input_size):
        return [0] * (list_input_size + 1)

    def find_max_number(self, lst):
        max_number = 0
        for i in range(len(lst)):
            if lst[i] > max_number:
                max_number = lst[i]
        return max_number


count_sort_object = CountSort()
start_time = time.monotonic()
sorted_output = count_sort_object.run([29, 567, 0, 0, 78])
end_time = time.monotonic()
print(f"sorted output --> {sorted_output}")
