count=0
for x in xrange(1,5):
    for y in xrange(1,5):
        for z in xrange(1,5):
            if x!=y and x!=z and y!=z:
                a=100*x+10*y+z
                count+=1
print count

i=raw_input('i')
l=[10,20,40,60,100]
if i<l[0]:
    print 0.1*l[0]
elif 10<i<20:
    print 213