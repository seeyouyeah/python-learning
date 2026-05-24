# # # задание 1 изи
# # # def countdown(n):
# # #     for i in range(n, 0, -1):
# # #         yield i

# # # f = countdown(15)
# # # print(next(f))


# # # задание 2 ленивое чтение файла
# # def read_chunks(filename, chunk_size):
# #     with open(filename) as f:
# #         chunk = f.read(chunk_size)
# #         while chunk != '':
# #             yield chunk
# #             chunk = f.read(chunk_size)

# # for i in read_chunks("1.txt", 5):
# #     print(i)




# # задание 3 хард
def merge_sorted(*iterables):
    pointers = [0] * len(iterables)
    while True:
        # текущие элементы всех незаконченных списков
        current = [
            (iterables[k][pointers[k]], k)  # (значение, индекс списка)
            for k in range(len(iterables))
            if pointers[k] < len(iterables[k])  # список ещё не кончился
        ]
        
        if not current:  # все списки кончились
            break
        
        value, k = min(current)  # найди минимальный
        yield value
        pointers[k] += 1  # сдвинь указатель того списка
        
for i in merge_sorted([1, 5], [3, 4], [-10, 0, 12], [2]):
    print(i)






# iterables = [[1, 5], [3, 4], [12, -10, 0], [2]]

# pointers = [0] * len(iterables)
# print(pointers)
# # current = [i for i in range(len(iterables)) if pointers[i] < len(iterables[i])]
# current = [
#         (iterables[k][pointers[k]], k)  # (значение, индекс списка)
#         for k in range(len(iterables))
#         if pointers[k] < len(iterables[k])  # список ещё не кончился
#     ]


# print(current)
# value, k = min(current)  # найди минимальный

# print(value)