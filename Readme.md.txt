данный метод ищет максимум из списка

def large(arr): 
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
           max_ = ele
    return max_ 


#list1 = [1,3,5,4,12,6]
n=int(input())
list1 = []
for i in range (n):
    list1.append(int(input()))
result = large(list1)
print(result)


теперь пользователь сам может вводить массив