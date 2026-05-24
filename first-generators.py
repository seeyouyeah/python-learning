# # class Point:
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
    
# #     def __repr__(self):
# #         return f"kek(x={self.x}, y={self.y})"
    
# #     def __eq__(self, other):
# #         return self.x == other.x and self.y == other.y
    
    
# # start = Point(0, 0)

# # print(start)


# def countdown(n):
#     for i in range(n, 0, -1):
#         yield i

# f = countdown(15)
# print(next(f))


# ленивое чтение файла
def read_chunks(filename, chunk_size):
    with open(filename) as f:
        chunk = f.read(chunk_size)
        while chunk != '':
            yield chunk
            chunk = f.read(chunk_size)

s = read_chunks('1.txt', 5)

otvet = input()
while not (otvet := input()):
   print(next(s))