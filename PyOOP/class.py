class person():
    def fact(self,n):
        if n==1:
            return 1
        else:
            return n * self.fact(n - 1)
ob=person()
n =int(input("Enter number you find factorial"))
res=ob.fact(n)
print(res)
