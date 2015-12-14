s = raw_input()
t = raw_input()
diff = 0
for c1,c2 in zip(s,t):
  if(c1!=c2):
    diff = diff+1
print diff