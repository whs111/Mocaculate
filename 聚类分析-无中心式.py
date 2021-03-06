"""
    @Description : perceptron by python
    @Author: Liu_Longpo
    @Time: Sun Dec 20 12:57:00 2015
"""

import matplotlib.pyplot as plt
import numpy as np
import time

a0 = 1
trainSet1 = []
trainSet2 = []
w1 = [0,0]
stor_w1 = [0,0]
w2 = [0,0]
stor_w2 = [0,0]
b1 = 0
b2 = 0
lens = 0
alpha = 1  # learn rate , default 1
trainLoss1 = []
trainLoss2 = []

def updateParm1(sample):
    global w1,b1,lens,alpha
    for i in range(lens):
        w1[i] = w1[i] + alpha*sample[1]*sample[0][i]
    b1 = b1 + alpha*sample[1]

def updateParm2(sample):
    global w2,b2,lens,alpha
    for i in range(lens):
        w2[i] = w2[i] + alpha*sample[1]*sample[0][i]
    b2 = b2 + alpha*sample[1]

def calDistance1(sample):
    global w1,b1
    res = 0
    for i in range(len(sample[0])):
        res += sample[0][i] * w1[i]
    res += b1
    res *= int(sample[1])
    return res

def calDistance2(sample):
    global w2,b2
    res = 0
    for i in range(len(sample[0])):
        res += sample[0][i] * w2[i]
    res += b2
    res *= int(sample[1])
    return res

def trainMLP_1(Iter):
    global stor_w1
    print "training MLP..."
    print "-"*40
    epoch = 0
    for i in range(Iter):
        train_loss =0
        update = False
        #store the value of w
        stor_w1 = w1
        print "epoch",epoch, "  w1: ",w1,"b1:",b1,
        for sample in trainSet1:
            res = calDistance1(sample)
            if res <= 0:
                train_loss += -res
                update = True
                updateParm1(sample)
        print 'train loss1:',train_loss
        trainLoss1.append(train_loss)
        if update:
            epoch = epoch+1
        else:
            print "The training have convergenced,stop trianing "
            print "Optimum W:",w1," Optimum b:",b1
            #os._exit(0)
            break # early stop
        update = False

def trainMLP_2(Iter):
    global stor_w2
    print "training MLP..."
    print "-"*40
     #store the value of w
    stor_w2 = w2
    epoch = 0
    for i in range(Iter):
        train_loss =0
        update = False
        print "epoch",epoch, "  w2: ",w2,"b2:",b2,
        for sample in trainSet2:
            res = calDistance2(sample)
            if res <= 0:
                train_loss += -res
                update = True
                updateParm2(sample)
        print 'train loss2:',train_loss
        trainLoss2.append(train_loss)
        if update:
            epoch = epoch+1
        else:
            print "The training have convergenced,stop trianing "
            print "Optimum W:",w2," Optimum b:",b2
            #os._exit(0)
            break # early stop
        update = False


def Average_1():
    global w1,w2,a0,w0
    t_w1=[w1[0]-stor_w1[0],w1[1]-stor_w1[1]]
    w0=[w0[0]-a0*(t_w1[0]),w0[1]-a0*(t_w1[1])]
    w2=w0       #
    print "="*40
    print w0
    print "="*40

def Average_2():
    global w1,w2,a0,w0
    t_w2=[w2[0]-stor_w2[0],w2[1]-stor_w2[1]]
    w0=[w0[0]-a0*(t_w2[0]),w0[1]-a0*(t_w2[1])]
    w1=w0       #
    print "="*40
    print w0
    print "="*40

if __name__=="__main__":
    '''
    if len(sys.argv)!=4:
        print "Usage: python MLP.py trainFile modelFile"
        exit(0)
    alpha = float(sys.argv[1])
    trainFile = open(sys.argv[2])
    modelPath = sys.argv[3]
    '''
    alpha = float(0.1)
    trainFile = open('C:\\Users\\Administrator\\Desktop\\testSet1.txt')
    trainFile1 = open('C:\\Users\\Administrator\\Desktop\\testSet2.txt')
    #modelPath = 'model'
    lens = 0
    # load data  trainSet[i][0]:data,trainSet[i][1]:label
    for line in trainFile:
        data1 = line.strip().split('\t') # train ' ' ,testSet '/t'
        lens = len(data1) - 1
        sample_all = []
        sample_data = []
        for i in range(0,lens):
            sample_data.append(float(data1[i]))
        sample_all.append(sample_data) # add data
        if int(data1[lens]) == 1:
            sample_all.append(int(data1[lens])) # add label
        else:
            sample_all.append(-1) # add label
        trainSet1.append(sample_all)
    trainFile.close()
    #
    for line in trainFile1:
        data1 = line.strip().split('\t') # train ' ' ,testSet '/t'
        lens = len(data1) - 1
        sample_all = []
        sample_data = []
        for i in range(0,lens):
            sample_data.append(float(data1[i]))
        sample_all.append(sample_data) # add data
        if int(data1[lens]) == 1:
            sample_all.append(int(data1[lens])) # add label
        else:
            sample_all.append(-1) # add label
        trainSet2.append(sample_all)
    trainFile1.close()
    #nect file process

    # initialize w by 0
    for i in range(lens):
        w1.append(0)
        w2.append(0)
    w0 = w1+w2
    # train model for max 100 Iteration
    start = time.clock()
    for i in range(16): #
        trainMLP_1(5)
        Average_1()
        trainMLP_2(5)#conduct as you like
        Average_2()


    end = time.clock()
    print 'train time is %f s.' % (end - start)
    #
    x = np.linspace(-5,5,10)
    plt.figure()
    for i in range(len(trainSet1)):
        if trainSet1[i][1] == 1:
            plt.scatter(trainSet1[i][0][0],trainSet1[i][0][1],c=u'b')
        else:
            plt.scatter(trainSet1[i][0][0],trainSet1[i][0][1],c=u'r')
    plt.plot(x,-(w0[0]*x+b1)/w0[1],c=u'r')
    plt.show()
    trainIter = range(len(trainLoss1))
    plt.figure()
    plt.scatter(trainIter,trainLoss1,c=u'r')
    plt.plot(trainIter,trainLoss1)
    plt.xlabel('Epoch')
    plt.ylabel('trainLoss')
    plt.show()
