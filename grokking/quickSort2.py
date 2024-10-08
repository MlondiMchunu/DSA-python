
def qs(array):

    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        great = [i for i in array[1:] if i > pivot]

        return qs(less) + [pivot] + qs(great)


print(qs([362,54,123,54,2,870,7,46,32,1]))