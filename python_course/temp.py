import sys









open c

for line in a
    write line to c

for line in b
    write line to c

close c





x = open(sys.argv[1], "r")

for line1 in x:
    print(line1)
x.close()

f = x.readline()











t = open(sys.argv[2], "r")
for line2 in t:
    print(line2)
t.close()

m = open(sys.argv[3], "w")
#m.write(x.readline() + t.readline())
m.write(str(f + f1))
f = x.readline()
m.close()
for line in m:
    print(line)
""" 
if os.path.exists(sys.argv[3]):
    os.remove(sys.argv[3])
else:
    print("the file does not exist")
 """


#    print(line)
#c = str(x.readline() + t.readline())
#print(r)
#for line in x:
 #   print (line)
#for o in t:
 #   print(o)
#y = open(sys.argv[3],"x")

#y.write(x + t)
#for a in y:
 #   print(a)
""" 
for i in sys.argv[1:]:
      x=open(sys.argv[1])
      #for line in x:
       #   print(line)
      print(x.read())  
      t=open(sys.argv[2])
      print(sys.argv[2])
      #for lines in t:
       #   print(lines)
     # w=open(sys.argv[3],"x")
 """
""" 
#r=str(sys.argv[1] + sys.argv[2])

    x = open("i.py",'r')

    for line in lines(x):

        print(line) 

       #print(i) """
