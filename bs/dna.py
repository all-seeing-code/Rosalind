s = raw_input()
a,g,c,t = 0,0,0,0
for i in range(0,len(s)):
  if(s[i]=='A'):
    a = a+1
  elif(s[i]=='G'):
    g = g+1
  elif(s[i]=='C'):
    c = c+1
  else:
    t = t+1
print a, c, g, t