def bubble_sort(list):
    for i in range(len(list)): # Answer : len(list)
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1]: # Answer : list[j] > list[j+1]
                list[j], list[j+1] = list[j+1], list[j]
    return list

arr = [1, 3 ,4, 2, 5]
print(bubble_sort(arr))