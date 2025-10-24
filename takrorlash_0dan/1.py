# n=[]
# def a(lst):
#     for b in lst:
#         if b%2!=0:
#             n.append(b)
#     return sum(n)

# assert a([1,2,3,4,5])

# def min_max(lst):
#     return min(lst) , max(lst)
# assert min_max([1,5,3,9,2]) == (1,9)

a=[]
def total(n):
    i=range(1,n)
print(i)
    a.append(i)
    return sum(a)
total(5)
# assert total(5) == 15
# assert total(10) == 55
