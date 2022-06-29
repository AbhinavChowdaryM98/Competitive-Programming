m = int(input())

books = list(map(int, input().split()))
r_books = []
n = int(input())
for i in range(n):
    j = int(input())
    r_books.append(books[j-1])
    del books[j-1]

for i in r_books:
    print(i)