def logistic_regression( X_train, X_test, Y_train, Y_test ):
	{
		log_classifier.fit(X_train, Y_train)
		Y_pred = log_classifier.predict(X_test)
    
    print("accuracy score for training data")
		print(round(log_classifier.score(X_train,Y_train)*100,2))
    print("accuracy score for testing data")
		print(round(log_classifier.score(X_test,Y_test)*100,2))
	}
