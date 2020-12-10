
# In the language of your choice, write code that prints every third element of this list using recursion. [1, 2, 3, 4, 5, 6, 7, 8, 9]
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = len(list)
def thrd_elemnt(list, n=2):
    print(list[n])
    if(n < i - 2):
        thrd_elemnt(list, n + 3)

print(thrd_elemnt(list))
