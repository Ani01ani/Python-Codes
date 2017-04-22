#importing library
from sklearn import tree
#defining the measurements
X = [[181,80,44],[177,40,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],
[175,64,39]]

#defining the gender
Y = ['male','female','female','female','male','male','male']

#defining the classifier
clf = tree.DecisionTreeClassifier()

#training the data
clf = clf.fit(X,Y)

#testing data
prediction = clf.predict([[178,60,41]])

#getting output
print(prediction)
