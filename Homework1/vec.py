class Vector():
    def __init__(self, x, y, z):
        if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)) and (isinstance(z, int) or isinstance(z, float)):
            self.x = x
            self.y = y
            self.z = z
        else:
            print('not vector')
    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __add__(self, other):
        if isinstance(other, Vector):
           return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x+other,self.y+other,self.z+other)
    def __radd__(self, other):
        return self + other
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x-other,self.y-other,self.z-other)
    def __mul__(self, other):
        if isinstance(other, Vector) and isinstance(self, Vector):
            return (self.x*other.x+self.y*other.y+self.z*other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x*other,self.y*other,self.z*other)
    def __rmul__(self, other):
        return self * other
    def center(self, other1, other2):
        return Vector((self.x+other1.x+other2.x)/3,(self.y+other1.y+other2.y)/3,(self.z+other1.z+other2.z)/3)
    def S(self, other1, other2):
        p=(abs(self-other1)+abs(self-other2)+abs(other1-other2))/2
        return (p*(p-abs(self-other1))*(p-abs(self-other2))*(p-abs(other1-other2)))**0.5

#упр 1.1
v1 = Vector(1,2,3)
v2 = Vector(2,3,1)
v3 = Vector(3,1,2)
sv = str(v3)
print(v1.center(v2,v3))

#упр 1.2
n = int(input()) #кол-во точек
if n>=3:
    vectors = []
    ans = []
    ans1=[]
    for i in range(n):
        x, y, z = map(float, input().split())
        vectors.append(Vector(x, y, z))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k,vectors[i].S(vectors[j], vectors[k]))
                ans.append(vectors[i].S(vectors[j], vectors[k]))
    print()
    for t in range (len(ans)):
        if type(ans[t])==float and ans[t]>0:
            ans1.append(ans[t])
    print(max(ans1))
else:
    print('need more') 