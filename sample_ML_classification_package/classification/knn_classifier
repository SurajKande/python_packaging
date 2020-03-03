def knn_classification( n, X_train, X_test, Y_train, Y_test ):
	{
		knn = KNeighborsClassifier(n_neighbors = n, metric = "minkowski", p = 2, n_jobs = -1)
		knn.fit(X_train, Y_train)
		Y_pred = knn.predict(X_test)
    
    print("accuracy score on training data")
		print(round(knn.score(X_train,Y_train)*100,2))
    print("accuracy score on testing data")
		print(round(knn.score(X_test,Y_test)*100,2))
	}
