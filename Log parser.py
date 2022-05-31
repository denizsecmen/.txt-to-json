g=open("Json.txt","r")#replace Json.txt with your actual file want to see.
h=open("Json.json","w")
f=g.readlines()
f=f[:50]
g='{\n"datas":"['
for gz in f:
    ga=gz.split("]")
    g+="\n{"+"\n"+"\"date\":"+"\""+str(ga[0][1:])+"\""+","+"\n"+"\"notice\":"+"\""+str(ga[1][2:])+"\""+","+"\n"+"\"explanation\":"+"\""+str(ga[2]).rstrip("\n")+"\""+"\n"+"}"+","
g=g[:len(g)-1]
g=g+"\n]\n}"
h.write(g)
h.close()
