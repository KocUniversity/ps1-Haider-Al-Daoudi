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
T=5000
UB=10000
lowestformula=10000000000000000000000000
LB=0
formula=0
stepNumber=n
int(T)
while n>0:
  formula+=(List[f]**(n-1)) * T
  n-=1
  f+=1 
  if n==0 and formula<B:
    LB=T
    T = (UB+LB)/2
    f=0
    n=stepNumber
    formula=0

  elif n==0 and formula>B:
    UB=T
   
    f=0
    n=stepNumber
    

    if lowestformula>formula and formula!=0:
      lowestformula=formula
      ourT=T
    T = (UB+LB)/2
    formula=0

    

print (int(ourT)+1)

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)