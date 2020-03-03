def svm_classifiaction( X_train, X_test, Y_train, Y_test ):
	{
		svm = SVC(kernel = "linear")
		svm.fit(X_train, Y_train)
		Y_pred = svm.predict(X_test)
    
    print("accuracy score on training data")
		print(round(svm.score(X_train,Y_train)*100,2))
    print("accuracy score on testing data")
		print(round(svm.score(X_test,Y_test)*100,2))
	}
