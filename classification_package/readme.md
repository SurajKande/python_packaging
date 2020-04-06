### Directory Structure

|-> classification_package

    - genpactclassifiaction
    
        -- decision_tree_classifier.py
        
        -- knn_classifier.py
        
        -- logistic_regression.py
        
        -- svm_classifier.py
        
    - setup.py
    
    - dist                            
    
        -- wheel file 
        
        -- tar.gz file

### Installing:
for installing the package run the command: 
```pip install http://15.206.160.184:8080/packages/genpactclassification-0.0.3-py3-none-any.whl#md5=b78d8a3653004e5cdaca6c0087326e7e```


### To use the module:
example: using decision_tree_classifier from genpactclassification package on iris dataset

    import numpy as np
    from sklearn.model_selection import train_test_split
    from genpactclassification import decision_tree_classifier as dt
    
    from sklearn.datasets import load_iris
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)
    
    model,train_accuracy,test_accuracy = dt.decision_tree_classifier(X_train,X_test,y_train,y_test)
   
OUTPUT:
   
    >>> model
    DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=None,
                           max_features=None, max_leaf_nodes=None,
                           min_impurity_decrease=0.0, min_impurity_split=None,
                           min_samples_leaf=1, min_samples_split=2,
                           min_weight_fraction_leaf=0.0, presort=False,
                           random_state=None, splitter='best')  
                        
    
      >>> train_accuracy 100.0
      
      >>> test_accuracy  97.37
