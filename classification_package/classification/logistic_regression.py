def logistic_regression( X_train, X_test, Y_train, Y_test ):
	
	log_classifier = LogisticRegression
	log_classifier.fit(X_train, Y_train)
	Y_pred = log_classifier.predict(X_test)
	training_score = round(log_classifier.score(X_train,Y_train)*100,2)
	testing_score = round(log_classifier.score(X_test,Y_test)*100,2)
	return log_classifier,training_score,testing_score
