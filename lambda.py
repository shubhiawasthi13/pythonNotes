x = lambda a: a+20
print(x(10))
print(".....................")

y = lambda a,b,c,d: a+b+c+d
print(y(2,4,5,6))
print(".....................")

my_list1 = ["4","5","7","3"]
def merge_list(list):
        return lambda newlist: list+newlist
list_merge = merge_list(my_list1)
my_list2 = ["3","6","6","3"]
print(list_merge(my_list2))