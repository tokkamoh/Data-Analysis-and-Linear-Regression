# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:23:09 2020

@author: tukka
"""
import pandas as pd
import matplotlib.pyplot as plt
def predict(x,theta):#calculate error
    ypred= (x*(theta[1])+theta[0])
    return ypred
    
    
    
    
def MeanSquareError(ypred,ytest):
    summ=0
    m=len(y)  
    J= ((1/(m))*(ytest-ypred)**2).tolist()
    for i in J:
        summ+=i
       
    return summ    
    
def error(x,y,theta):
    summ=0
    m=len(y) 
    ypred= (x*(theta[1])+theta[0])
    J= ((1/(2*m))*(ypred-y)**2).tolist()
    for i in J:
        summ+=i
    return summ
def trainings(it,x,y,alpha,theta):
    
    i=0
    m = len(y)
    errors=[]

    while (i<it):
        
         #hypothesis 
        ypred= x*(theta[1])+theta[0]
        currentTheta0=theta[0]
        currenttheta1=theta[1]
        
        theta[0]=theta[0]-((alpha*(1.0/m))*sum(ypred-y))
    
        theta[1]=theta[1]-((alpha*(1.0/m))*sum((ypred-y)*x))
        errors.append(error(x,y,theta))
        
        if currentTheta0==theta[0] and currenttheta1==theta[1] :
            return (theta,errors)
        elif (abs(currentTheta0-theta[0]) <=0.00001 and
              abs(currenttheta1-theta[1])<=0.00001):
            return(theta,errors)
       
        #print(errors)
        i+=1    
    return (theta,errors)


def normalize(x,y):
    xMi=x.min()
    yMi=y.min()
    xMx=x.max()
    yMx=y.max()

    x=((x-xMi)/(xMx-xMi))
    y=((y-yMi)/(yMx-yMi))
    return (x,y)    
def testing (x,t):
    ypredicted=(predict(x, t))
    return (ypredicted)

def accuracy(ypred,y):
    count=0
    for i in ypred:
    
        for x in y:
            
            if i==x or (i-x)<0.01:
                count=count+1
            
                break
    return (count/len(y))*100
    
data =pd.read_csv('diabetic_kidney_disease.csv')      
x=data["FBG (mg/dL)"]    #predicted
y=data["UACR (mg/g creatinine)"] #actual
size=len(data)

alpha=0.005
iterations=5000
theta=[0.0,0.0]
s=normalize(x,y)
x_train=s[0][0:80]
y_train=s[1][0:80]
x_test=s[0][80:]
y_test=s[1][80:]
z=trainings(iterations, x_test, y_test, alpha,theta)
y_pred=testing(x_test,z[0])
a=MeanSquareError(y_pred, y_test)
#print("mean Square error of each iteration = ",z[1]) # mean square error of each iteration
print("mean Square errors for predicted values = ",a)
print("accuracy = ",accuracy(y_pred, y_train),"%")
plt.xlabel("FBG (mg/dL)")
plt.ylabel("UACR (mg/g creatinine)")
plt.title("Real vs predicted values")
plt.scatter(s[0],s[1])
plt.plot(s[0],predict(s[0],[0.0,0.0]),color='red') # Before optimizing l data
plt.show()
plt.scatter(s[0],s[1])
plt.plot(s[0],testing(s[0],z[0]),color='red') #After optimizing the thetas
plt.show()

