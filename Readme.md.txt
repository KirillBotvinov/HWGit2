данный метод ищет минимум из списка
def large(arr): 
    min_ = arr[0]
    for ele in arr:
        if ele < min_:
           min_ = ele
    return min_ 


#list1 = [1,3,5,4,12,6]
n=int(input())
list1 = []
for i in range (n):
    list1.append(int(input()))
result = large(list1)
print(result)

