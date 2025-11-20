from sklearn import tree
X = [[0,0],[1,1],[1,0],[0,1]]  # features
y = [0,1,1,0]                  # labels
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
print("Predict [1,0]:", clf.predict([[1,0]]))
