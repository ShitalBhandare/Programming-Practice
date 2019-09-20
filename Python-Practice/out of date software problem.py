# serverlist.txt =>
'''
Server1, Database, MySQL, 5.5
Server2, Database, MySQL, 5.1
Server3, OS, Ubuntu, 10.04
Server1, OS, Ubuntu, 12.04
Server2, OS, Ubuntu, 12.04
'''


#read file
f = open('serverList.txt', 'r')
x = f.read().splitlines()
 
#get list for each column
a=[] #list of server names
b=[] #list of software category 
c=[] #list of software names
d=[] #list of software version
 
#Split each row in columns 
for info in x:
  if info != "":
    p, q, r, s = info.split(',')
    a.append(p)
    b.append(q)
    c.append(r)
    d.append(s)
 
print(a,b,c,d)
#get unique software 
cSet = list(set(c))
 
print(cSet)

#Save dictionary as Software and Its version
cSetCout = {}
for nCSet in range(0,len(cSet)):
  version = 0.0
  for nRow in range(0,len(c)):
    if(c[nRow] == cSet[nCSet]):
      if(float(version) < float(d[nRow])):
        version= d[nRow]
        cSetCout.update({cSet[nCSet] : version})
 
print(cSetCout)

listLowServer = []
 
#get server having older version of software installed 
for key, value in cSetCout.items():
  lowServer = ''
  lowRow = 0;
  nCount = 0
  
  ''' 
  #count number of same version of given software
  for nRow in range(0, len(c)):
    if(c[nRow] == key):
      nCount = nCount +1
      print(nCount)
  '''

 # if there is multiple software installed,
 # get server having older software version installed
  
  for nRow in range(0, len(c)): 
    if(c[nRow] == key):
      if(d[nRow] != value):
        listLowServer.append(a[nRow])
        #value = d[nRow]
 
#find unique server names
listLowServerName = list(set(listLowServer))
 
#prints server names that have at least one software installation 
#that is not the latest version
for nameList in listLowServerName:
  print(nameList)
