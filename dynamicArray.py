class DynamicArray:
    def __init__(self,capacity:int):
        self.size = 0
        self.capacity = capacity
        self.arr = [0]* capacity


    def insert(self, i:int, n:int)->None:
        self.arr[i] = n

    def get(self,index:int)->int:
        return self.arr[index]
    
    def pushback(self, element:int)->None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = element
        self.size+=1

    def resize(self)->None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
            self.arr = new_arr

    def popback(self)->int:
        self.size -=1
        return self.arr[self.size]

    

    def getSize(self):
        return self.size
    
    def getCapacity(self):
        return self.capacity
    
    def print(self):
        for i in range(self.size):
            print(self.arr[i])
    
if __name__ =="__main__":

    da = DynamicArray(20)
    da.pushback(2)
    da.pushback(8)
    da.pushback(46)
    da.pushback(92)
    da.pushback(19)
    da.pushback(30)

    print(da.get(4))

    da.print()