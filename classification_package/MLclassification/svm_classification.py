from sklearn.svm import SVC
def svm_classification( X_train, X_test, Y_train, Y_test ):
	
	svm = SVC(kernel = "linear")
	svm = svm.fit(X_train, Y_train)
	# Y_pred = svm.predict(X_test)
	training_score = round(svm.score(X_train,Y_train)*100,2)
	testing_score = round(svm.score(X_test,Y_test)*100,2)
	return svm,training_score,testing_score
