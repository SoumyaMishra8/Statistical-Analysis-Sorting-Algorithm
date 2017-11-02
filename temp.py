import math
import random
class Statsort:
    def main():
            upperlimit=1000
            intBucket=[]
            for i in range (upperlimit):
                intBucket.append(random.uniform(0,upperlimit))
                sorterSimple(intBucket)
                sorterBucket(intBucket,upperlimit)
    def sorterSimple(intBucket):
        from datetime import time 
        print (time)
        intBucket.sort()
        from datetime import time 
        print (time)
    def sorterBucket(intBucket,upperlimit):
        from datetime import time 
        print (time)
        buckets=(int)(round(upperlimit/1000))
        intbucket1=[[1000]]*buckets
        Min=intBucket[0]
        Max=intBucket[0]
        sum=0
        for i in range (upperlimit):
            Min=min(Min,intBucket[i])
            Max=max(Max,intBucket[i])
            sum = sum+intBucket[i]
        mean=round(sum/upperlimit)
        lowerRange=mean-Min
        upperRange=Max-mean
        range=Max-Min
        lowerGroups=round(lowerRange/range)
        lowerGroups=max(1,lowerGroups)
        upperGroups=buckets-lowerGroups
        for x in range(upperlimit):
            value=intBucket[x]
            if mean<value:
                bucketSelect=(int)(math.ceil(lowerGroups*(value-Min)/lowerRange))
            else:
                bucketSelect=lowerGroups+(int)(math.ceil(upperGroups*(value-mean)/upperRange))
            bucketSelect=(int)(((value-Min)/range)*upperlimit/1000)
        for y in range(buckets):
            intbucket1.sort()
        from datetime import time 
        print(time)
