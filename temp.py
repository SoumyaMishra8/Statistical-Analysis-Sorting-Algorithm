import math
import random
import datetime
class Statsort:
    #program to compare python embedded sort and new sort being created
    #main - creating integer normal distribution list of varying lengths, print out times 
    def main():
        upperlimit=100000000
        intBucket=[]
        for i in range (upperlimit):
            intBucket.append((int)(random.uniform(0,upperlimit)))
            Statsort.sorterSimple(intBucket)
            Statsort.sorterBucket(intBucket,upperlimit)
    def sorterSimple(intBucket):
        print (datetime.datetime.now())
        intBucket.sort() #sort list - already optimized in python
        print (datetime.datetime.now())
        #sorting the integer list intBucket using the embedded sort in python 
    def sorterBucket(intBucket,upperlimit):
        print (datetime.datetime.now())
        buckets=(int)(round(upperlimit/1000)) #creating the number of buckets by dividing list length (elements) by 1000 - elements in each bucket 
        intbucket1=[[1000]]*buckets #creating a 2D list in which number of rows is buckets and columns is 1000
        Min=intBucket[0] #setting both min and max for first element in list
        Max=intBucket[0]
        sum=0
        print (datetime.datetime.now()) 
        for i in range (upperlimit): 
            Min=min(Min,intBucket[i]) #comparing each value to get min and max per loop 
            Max=max(Max,intBucket[i])
            sum = sum+intBucket[i] #summing all elements 
        print (datetime.datetime.now())
        mean=round(sum/upperlimit) 
        lowerRange=mean-Min #half of the range of the data set - used to create buckets for each range
        upperRange=Max-mean
        Range=Max-Min
        lowerGroups=round(lowerRange/Range) #number of buckets for lowerRange 
        lowerGroups=max(1,lowerGroups) #if the number of elements 1000 or less than 1000, number of groups will be 1 instead of 0
        upperGroups=buckets-lowerGroups #number of buckets for upperRange
        for x in range(upperlimit):
            value=intBucket[x] #calling value at index x of list
            if mean<value: #determining which range it will fall into 
                bucketSelect=(int)(math.ceil(lowerGroups*(value-Min)/lowerRange)) #seeing where in the lowerRange does this element lie in - distance from mean 
            else:
                bucketSelect=lowerGroups+(int)(math.ceil(upperGroups*(value-mean)/upperRange)) #seeing where in the upperRange does element lie - distance between mean and max
            bucketSelect=(int)(((value-Min)/Range)*upperlimit/1000) #reinstantiating bucketSelect
        for y in range(buckets):
            intbucket1.sort() #uses python sorting algorithm to sort buckets
        print (datetime.datetime.now())
