
def train_deploy():
    
    import pandas as pd
    
    from sklearn.model_selection import train_test_split
    
    from sklearn.tree import DecisionTreeClassifier
    
    from sklearn.metrics import accuracy_score
    
    df=pd.read_csv('demo_dataset.csv')
    
    X=df.iloc[:,:-1]
    
    y=df.iloc[:,-1]
    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
    
    clf=DecisionTreeClassifier()
    
    clf.fit(X_train,y_train)
    
    y_pred=clf.predict(X_test)
    
    print('Accuracy:',accuracy_score(y_test,y_pred))
    
train_deploy()

