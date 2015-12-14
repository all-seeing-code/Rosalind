n,k = raw_input().split()
n = int(n)
k = int(k)
ai1,ai2 = 1,1
ai = 1
n = n-2
while n>0:
  ai = ai1 + ai2*k
  ai1 , ai2 = ai , ai1
  n = n-1
print ai

# input 36 3 output 3048504677680