import argparse
import random
import math
class data:
    def __init__(self, temperature,humidity,light,co2,class_value):

        self.temperature = temperature
        self.humidity=humidity
        self.light=light
        self.co2=co2
        self.class_value=class_value
    def change(self):
        self.temperature=0.000

def readInputs():
    f=open("occupancy_data/datatraining.txt","r")
    k=f.readline()
    for line in f:
        ls=line.split(",")
        k=list(ls[len(ls)-1])
        d=data(float(ls[2]),float(ls[3]),float(ls[4]),float(ls[5]),int(k[0]))
        train_date.append(d)
    f.close()

def readInputs1():
    f=open("occupancy_data/datatest.txt","r")
    k=f.readline()
    for line in f:
        ls=line.split(",")
        k=list(ls[len(ls)-1])
        d=data(float(ls[2]),float(ls[3]),float(ls[4]),float(ls[5]),int(k[0]))
        test_data.append(d)
    f.close()

def diff_value(l1,l2):
    return math.sqrt(pow(l1.temperature-l2.temperature,2)+pow(l1.humidity-l2.humidity,2)+pow(l1.light-l2.light,2)+pow(l1.co2-l2.co2,2))

def evaluate_nearest_class(temp,k2):
    count1=0
    count0=0
    finalclass=0
    for q in range(k2):
        if temp[q][1]==1:
            count1+=1
        elif temp[q][1]==0:
            count0+=1
    if count1>count0:
        finalclass=1
    return finalclass

def calculate_distance(validation,train,k1):
    count=0
    for valid_value in validation:
        dist=[]
        for train_value in train:
            dist.append([diff_value(valid_value,train_value),train_value.class_value])
        dist.sort(key=lambda x:x[0])

        if valid_value.class_value==evaluate_nearest_class(dist,k1):
            count+=1
    return (float(count))/(float(len(validation)))

if __name__== '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("KNN_value",help="Entering the KNN Value",type=int)
    args=parser.parse_args()
    test_data=[]
    train_date=[]
    readInputs()
    readInputs1()
    accuracy=calculate_distance(test_data,train_date,args.KNN_value)
    f=open("Accuracies.txt","a")
    f.write("Accuracy when the value of k = "+str(KNN_value)+" is "+accuracy)
    f.close()
    print "Accuracy is : ",accuracy*100
