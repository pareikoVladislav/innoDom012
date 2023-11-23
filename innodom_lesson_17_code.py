# def linear_searching(arr: list, val: int):
#     for index in range(len(arr)):
#         if arr[index] == val:
#             return index
#     return -1
#
#
# my_list = [2, 4, 1, 5, 6, 3, 8, 7, 0, 1, 4, 3, 13, 4, 22]
# required_elem = 13
#
# result = linear_searching(arr=my_list, val=required_elem)
#
# print(f"Элемент найден на позиции: {result}")
# print(f"Элемент по индексу 12 = {my_list[12]}")

# array1 = [2, 1, 4, 3, 7, 6, 7, 9, 443, 1, 0, 32, 213, 6, 4, 87, 9, 676, 87, 4, 32, 1]


# def bubble_sort(arr: list):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# bubble_sort(array1)
#
# print(array1)

# array2 = [2, 1, 4, 3, 7, 6, 7, 9, 443, 1, 0, 32, 213, 6, 4, 87, 9, 676, 87, 4, 32, 1]
#
#
# def insertion_sort(arr: list):
#     for i in range(1, len(arr)):
#         value = arr[i]
#         index = i - 1
#
#         while index >= 0 and value < arr[index]:
#             arr[index + 1] = arr[index]
#             index -= 1
#
#         arr[index + 1] = value
#
#
# insertion_sort(array2)
#
# print(array2)


# def quick_sort(arr: list):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
#
#
# array3 = [2, 1, 4, 3, 7, 6, 7, 9, 443, 1, 0, 32, 213, 6, 4, 87, 9, 676, 87, 4, 32, 1]
#
# sorted_array = quick_sort(array3)
#
# print(sorted_array)
#
#
# def binary_search(arr: list, x: int):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
#
#     while low <= high:
#         mid = (high + low) // 2
#
#         if arr[mid] < x:
#             low = mid + 1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             return mid
#     return -1
#
#
# required_value = binary_search(arr=sorted_array, x=4)
# print(f"Искомый элемент находится на позиции индекса {required_value}")


# def dfs(graph, node, visited):
#     if node not in visited:
#         print(node, end=" ")
#         visited.append(node)
#
#         for n in graph[node]:
#             # print(*visited)
#             dfs(graph, n, visited)
#
#
# graph = {
#     "A": ["B", "C"],
#     "B": ["D", "E"],
#     "C": ["F"],
#     "D": [],
#     "E": ["F"],
#     "F": []
# }
#
# visited = []
#
# dfs(graph=graph, node="A", visited=visited)

from collections import deque


def bfs(graph, start):
    visited = set()

    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            queue.extend(set(graph[vertex]))

    return visited



graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

bfs(graph=graph, start="A")
