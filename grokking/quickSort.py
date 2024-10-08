def quickSort(array):

    """ arr=[]
    temp = 0

    if len(array) <2:
        return array
    elif len(array)==2:
        if array[0]>array[1]:
            return array
        else:
            arr = [array[1],array[0]]
            return arr
    """
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)
    
print(quickSort([96,45,3,23,2,124,0,54,7,987,3,2234,1,6684,6,32,8,9,705,3,12,-4]))
