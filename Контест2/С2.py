class Heap:
    def __init__(self,arr):
        self.arr = arr
        self.size = len(arr)
        self.heapify()
    def left(self,i):
        if (2*i+1) < self.size:
            return self.arr[2*i+1]
        else:
            return None
    def right(self,i):
        if (2*i+2) < self.size:
            return self.arr[2*i+2]
        else:
            return None
    def parent(self,i):
        if ((i-1)//2) < 0:
            return None
        else:
            return self.arr[(i - 1) // 2]
    def SiftDown(self,value,i):
        right = self.right(i)
        left = self.left(i)
        if not left and not right:
            return
        elif not right:
            if value > left:
                return
            else:
                self.arr[i] = left
                self.arr[2 * i + 1] = value
                self.SiftDown(value, 2 * i + 1)
        elif not left:
            if value > right:
                return
            else:
                self.arr[i] = right
                self.arr[2 * i + 2] = value
                self.SiftDown(value, 2 * i + 2)
        else:
            if value > right and value > left:
                return
            else:
                if right > left:
                    self.arr[i] = right
                    self.arr[2*i+2] = value
                    self.SiftDown(value, 2*i+2)
                else:
                    self.arr[i] = left
                    self.arr[2*i+1] = value
                    self.SiftDown(value, 2*i+1)
    def SiftUp(self,value,i):
        parent = self.parent(i)
        if not parent:
            return
        if value > parent:
            self.arr[(i-1)//2] = value
            self.arr[i] = parent
            self.SiftUp(value,(i-1)//2)
        else:
            return
    def get_max(self):
        return self.arr[0]
    def append(self,value):
        self.arr.append(value)
        self.size += 1
        self.SiftUp(value, self.size-1)
    def pop(self):
        self.arr[0],self.arr[-1] = self.arr[-1],self.arr[0]
        self.size -= 1
        self.arr.pop()
        if self.size>0:
            self.SiftDown(self.arr[0],0)
    def heapify(self):
        index = (self.size - 2)//2
        for i in range(index,-1,-1):
            self.SiftDown(self.arr[i],i)
def HeapSort(arr):
    ans = []
    h = Heap(arr)
    for i in range(len(arr)-1):
        ans.append(h.get_max())
        h.pop()
    ans.append(h.get_max())
    return ans 

def countinv(s):
    inv=0
    for i in range (len(s)):
        for j in range (i+1, len(s)):
            if s[i]>s[j]:
                inv+=1
    return inv

k=int(input())

for _ in range (k):
    n,m=map(int,input().split())
    s=[]
    for i in range (m):
        a=input().strip()
        inv=countinv(a)
        s.append(((-1)*inv,(-1)*i,a))
    h=Heap(s)
    ans=[]
    for _ in range(m):
        minim=h.get_max()[2]
        ans.append(minim)
        h.pop()
    for i in range(len(ans)):
        print(ans[i])
    print()