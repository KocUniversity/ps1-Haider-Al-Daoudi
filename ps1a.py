n, B = list(map(int, input().strip().split()))
T = 0

# your code here
n= int(input("please enter n: "))
B= int(input("please enter B: "))
List = [] 


for i in range(n):
  i+=1
  
  if i%2==0:
    a=2**i + 1 
    List.append(a)
  else:
    b=3**i + 1 
    List.append(b)
f=0
T=1
formula=0
stepNumber=n
while n>0:
  formula+=(List[f]**(n-1)) * T
  n-=1
  f+=1 
  if n==0 and formula<B:
    T+=1
    f=0
    formula=0
    n=stepNumber
  if T==10000:
    print("-1")
    break
if T!=10000:
  print(formula) 

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)