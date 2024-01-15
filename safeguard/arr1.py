size = int(input("enter the size of array: "))
arr1 = []

for i in range(size):
    ele = input(f"enter element{i+1}: ")
    arr1.append(ele)

print("Array is:  " , arr1)

arr1.remove(arr1[3])