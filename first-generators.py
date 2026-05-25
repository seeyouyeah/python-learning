# # # # задание 1 изи
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


# # задание 3 Напиши генератор merge_sorted(*iterables), который принимает несколько уже отсортированных списков и отдаёт элементы в общем отсортированном порядке — без использования sorted() и без объединения списков в один. (решение от Клода)
# def merge_sorted(*iterables):
#     pointers = [0] * len(iterables)
#     while True:
#         current = [
#             (iterables[k][pointers[k]], k)  # (значение, индекс списка)
#             for k in range(len(iterables))
#             if pointers[k] < len(iterables[k])  # список ещё не кончился
#         ]
        
#         if not current:  # все списки кончились
#             break
        
#         value, k = min(current)
#         yield value
#         pointers[k] += 1  # сдвинь указатель того списка
        
# for i in merge_sorted([1, 5], [3, 4], [-10, 0, 12], [2]):
#     print(i)




def unique(args):
    yielded = set()
    for i in args:
        if i not in yielded:
            yielded.add(i)
            yield i
            
for i in unique([1, 3, 2, 1, 5, 3, 4, 2]):
    print(i)