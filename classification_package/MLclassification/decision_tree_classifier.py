from sklearn.tree import DecisionTreeClassifier
def decision_tree_classifier( X_train, X_test, Y_train, Y_test ):

  decision_tree = DecisionTreeClassifier(criterion="entropy")
  decision_tree = decision_tree.fit(X_train,Y_train)
  # Y_pred = decision_tree.predict(X_test)
  training_score = round(decision_tree.score(X_train,Y_train)*100,2)
  testing_score = round(decision_tree.score(X_test,Y_test)*100,2)
  return decision_tree,training_score,testing_score
