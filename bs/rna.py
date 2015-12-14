s = raw_input()
t = ""
for i in range(0,len(s)):
  if(s[i]=='T'):
    t = t+'U'
  else:
    t = t+s[i]
print t,