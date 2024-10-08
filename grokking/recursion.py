def countdown(i):
    print(i)

    if i<=0:
        return
    else:
        countdown(i-1)

#countdown(7)
def fact(n):

    if n==0 or n ==1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

def sum(arr):
    total = 0

    for i in arr:
        total += i
    return total

print("Total of nums using loop : ",sum([3,7,3,5,2]))

#finding the sum using recursive function

def sum1(arr):

    if arr ==[]:
        return 0
    else:
        return arr[0] + sum(arr[1:])
    
print("Total of nums using recursion : ",sum1([3,2,5,1,4]))


def count1(arr):

    if arr == []:
        return 0
    else:
        return 1 + count1(arr[1:])
    
def max(arr):

    if arr == 0:
        return 0
    else:
        return arr[0:] > max(arr[1:]) 
    
print("Max number in the list : ",max([3,2,1,6,3,4,56,7,6,4,89]))
    

print("Count no. of items in list using recursion : ",count1([4,43,32,7,6,1,23,9,8,3,56,1,3,2]))