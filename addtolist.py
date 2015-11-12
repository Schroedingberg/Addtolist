def addtolistindict(key, comparelist,dictlist):
    i = 0
    while i<len(comparelist):
    	  pair = comparelist[i]

	  if key == pair[0]:
	     dictlist.append(pair[1])




    	  i+=1

#Man, sieht,dass das ganze Strings an Listen in einem Dictionary anhängen soll
# In etwa so:

somedict = {'A':[],'B':[]}

for key in somedict.keys():
    addtolistindict(key, comparelist, somedict[key])
