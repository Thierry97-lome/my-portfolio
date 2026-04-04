from sklearn.linear_model import LinearRegression

# Training data
X = [[1], [2], [3], [4]]   # hours studied
y = [2, 4, 6, 8]           # test scores

model = LinearRegression()
model.fit(X, y)

print(model.predict([[5]]))  # predict score for 5 hours of study