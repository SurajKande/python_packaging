Directory Structure

|-> sample_ML_packaging_example

    - Classifiaction
    
        -- decision_tree_classifier.py
        
        -- knn_classifier.py
        
        -- logistic_regression.py
        
        -- svm_classifier.py
        
    - setup.py
    
    - dist                            
    
        -- wheel file 
        
        -- tar.gz file
        
for installing go to the directory with setup.py and run 'python setup.py sdist bdist_wheel' which will generate a dist folder with both wheel file and tar.gz file 

after installing the package to use the modules:
    from classification import decision_tree_classifier 

after cleaning and feature engineering the data
send the data as arguments as X_train, X_test, Y_train, Y_test data in sequence
> decision_tree_classifier(X_train, X_test, Y_train, Y_test) 

> knn_classification( n, X_train, X_test, Y_train, Y_test ) # here n is for the neighbours

> logistic_regression( X_train, X_test, Y_train, Y_test )

> svm_classifiaction( X_train, X_test, Y_train, Y_test )



