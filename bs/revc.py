s = raw_input()
t = ""
for i in range(0,len(s)):
  if(s[i]=='A'):
    t = t+'T'
  elif(s[i]=='G'):
    t = t+'C'
  elif(s[i]=='C'):
    t = t+'G'
  else:
    t = t+'A'
print t[::-1],  #reverses the string
# Slice syntax. 