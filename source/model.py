from sklearn.svm import SVC, LinearSVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
# from sklearn.externals import joblib
import numpy as np
import pandas as pd
import pickle
import os
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


def algo_predict(vita):
    x = np.array([vita]).reshape(1, -1)
    optimum = pd.read_excel("VITAMINDATASET.xlsx")

     
    values = np.array([ optimum.vitaminA])

    X = values.reshape(-1, 1)
    Y = optimum.DificencyA

    #print(optimum.vitaminA)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size=0.2)  
     
    #clf = RandomForestClassifier()
    clf = KNeighborsClassifier(n_neighbors = 1, weights='uniform', algorithm='auto')

    #clf=linear_model.LogisticRegression(fit_intercept=False)
    #clf = DecisionTreeClassifier(criterion = "entropy", random_state = 1, splitter='best')  
    # Training the classifier
    clf.fit(X_train, y_train)
    acc=clf.score(X_test,y_test)*100
    print(acc)
    ypredict = clf.predict(x)
    print("ddddddddddddddddddddddddddddddddd")
    #print(x[0])
    print(ypredict)
    return ypredict[0]

def algo_predict1(vitb):
    x = np.array([vitb]).reshape(1, -1)
    optimum = pd.read_excel("VITAMINDATASET.xlsx")

     
    values = np.array([ optimum.vitaminB])

    X = values.reshape(-1, 1)
    Y = optimum.DificencyB

    #print(optimum.vitaminA)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size=0.2)  
     
    #clf = RandomForestClassifier()
    clf = KNeighborsClassifier(n_neighbors = 1, weights='uniform', algorithm='auto')

    #clf=linear_model.LogisticRegression(fit_intercept=False)
    #clf = DecisionTreeClassifier(criterion = "entropy", random_state = 1, splitter='best')  
    # Training the classifier
    clf.fit(X_train, y_train)
    acc=clf.score(X_test,y_test)*100
    print(acc)
    ypredict = clf.predict(x)
    print("ddddddddddddddddddddddddddddddddd")
    #print(x[0])
    print(ypredict)
    return ypredict[0]

def algo_predict2(vitc):
    x = np.array([vitc]).reshape(1, -1)
    optimum = pd.read_excel("VITAMINDATASET.xlsx")

     
    values = np.array([ optimum.vitaminC])

    X = values.reshape(-1, 1)
    Y = optimum.DificencyC

    #print(optimum.vitaminA)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size=0.2)  
     
    #clf = RandomForestClassifier()
    clf = KNeighborsClassifier(n_neighbors = 1, weights='uniform', algorithm='auto')

    #clf=linear_model.LogisticRegression(fit_intercept=False)
    #clf = DecisionTreeClassifier(criterion = "entropy", random_state = 1, splitter='best')  
    # Training the classifier
    clf.fit(X_train, y_train)
    acc=clf.score(X_test,y_test)*100
    print(acc)
    ypredict = clf.predict(x)
    print("ddddddddddddddddddddddddddddddddd")
    #print(x[0])
    print(ypredict)
    return ypredict[0]

def algo_predict3(vitd):
    x = np.array([vitd]).reshape(1, -1)
    optimum = pd.read_excel("VITAMINDATASET.xlsx")

     
    values = np.array([ optimum.vitaminD])

    X = values.reshape(-1, 1)
    Y = optimum.DificencyD

    #print(optimum.vitaminA)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size=0.2)  
     
    #clf = RandomForestClassifier()
    clf = KNeighborsClassifier(n_neighbors = 1, weights='uniform', algorithm='auto')

    #clf=linear_model.LogisticRegression(fit_intercept=False)
    #clf = DecisionTreeClassifier(criterion = "entropy", random_state = 1, splitter='best')  
    # Training the classifier
    clf.fit(X_train, y_train)
    acc=clf.score(X_test,y_test)*100
    print(acc)
    ypredict = clf.predict(x)
    print("ddddddddddddddddddddddddddddddddd")
    #print(x[0])
    print(ypredict)
    return ypredict[0]

def algo_predict4(vite):
    x = np.array([vite]).reshape(1, -1)
    optimum = pd.read_excel("VITAMINDATASET.xlsx")

     
    values = np.array([ optimum.vitaminE])

    X = values.reshape(-1, 1)
    Y = optimum.DificencyE

    #print(optimum.vitaminA)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size=0.2)  
     
    #clf = RandomForestClassifier()
    clf = KNeighborsClassifier(n_neighbors = 1, weights='uniform', algorithm='auto')

    #clf=linear_model.LogisticRegression(fit_intercept=False)
    #clf = DecisionTreeClassifier(criterion = "entropy", random_state = 1, splitter='best')  
    # Training the classifier
    clf.fit(X_train, y_train)
    acc=clf.score(X_test,y_test)*100
    print(acc)
    ypredict = clf.predict(x)
    print("ddddddddddddddddddddddddddddddddd")
    #print(x[0])
    print(ypredict)
    return ypredict[0]

def algo_predict5(vitk):
    x = np.array([vitk]).reshape(1, -1)
    optimum = pd.read_excel("VITAMINDATASET.xlsx")

     
    values = np.array([ optimum.vitaminK])

    X = values.reshape(-1, 1)
    Y = optimum.Dificencyk

    #print(optimum.vitaminA)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size=0.2)  
     
    #clf = RandomForestClassifier()
    clf = KNeighborsClassifier(n_neighbors = 1, weights='uniform', algorithm='auto')

    
    # Training the classifier
    clf.fit(X_train, y_train)
    acc=clf.score(X_test,y_test)*100
    print(acc)
    ypredict = clf.predict(x)
    print("ddddddddddddddddddddddddddddddddd")
    #print(x[0])
    print(ypredict)
    return ypredict[0]

def algo_reco(difa,difb,difc,difd,dife,difk):
    x = np.array([difa,difb,difc,difd,dife,difk]).reshape(1, -1)
    recomend = pd.read_excel("recommend.xlsx")
    X_d = recomend.drop("CLASS",axis=1)
    Y_d = recomend.CLASS
    from sklearn.model_selection import train_test_split
    x_train, x_test, Y_train, Y_test = train_test_split(X_d, Y_d,
                                                    test_size=0.2)  

    from sklearn.neighbors import KNeighborsClassifier
    clfd = KNeighborsClassifier(n_neighbors=3)
    clfd.fit(x_train, Y_train)   
    ypredict = clfd.predict(x)
    print("dfdfdfdfdfdfd")
    print(ypredict)
    return ypredict[0]

def algo_recodisease(difa,difb,difc,difd,dife,difk):
    from sklearn import tree
    x = np.array([difa,difb,difc,difd,dife,difk]).reshape(1, -1)
    recomend = pd.read_excel("diseaserecommend.xlsx")
    X_a = recomend.drop("CLASS",axis=1)
    X_d = X_a.drop("Disease",axis=1)
    Y_d = recomend.CLASS
    from sklearn.model_selection import train_test_split
    x_train, x_test, Y_train, Y_test = train_test_split(X_d, Y_d,
                                                    test_size=0.2)  

    from sklearn.neighbors import KNeighborsClassifier
    clfd = KNeighborsClassifier(n_neighbors=3)
    clfd.fit(x_train, Y_train)   
    ypredict = clfd.predict(x)
    print("dfdfdfdfdfdfd")
    print(ypredict)
    return ypredict[0]

def vit_A(vita):
    predicted_val=algo_predict(vita)
    return predicted_val

def vit_B(vitb):
    predicted_val=algo_predict1(vitb)
    return predicted_val

def vit_C(vitc):
    predicted_val=algo_predict2(vitc)
    return predicted_val

def vit_D(vitd):
    predicted_val=algo_predict3(vitd)
    return predicted_val

def vit_E(vite):
    predicted_val=algo_predict4(vite)
    return predicted_val
def vit_K(vitk):
    predicted_val=algo_predict5(vitk)
    return predicted_val
def reco(difa,difb,difc,difd,dife,difk):
    predicted_val=algo_reco(difa,difb,difc,difd,dife,difk)
    predicted_disese=algo_recodisease(difa,difb,difc,difd,dife,difk)
    return (predicted_val,predicted_disese)