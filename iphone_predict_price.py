import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# import data
data = pd.read_csv('iphone_price.csv')
model = LinearRegression()

#
model.fit(data[['version']], data[['price']])
# Predict the price for version
user_input_version = int(input("Enter the iPhone version to predict the price: "))
version_to_predict = pd.DataFrame({'version': [user_input_version]})
predicted_price = model.predict(version_to_predict)

print(predicted_price)



# separate x axis and y axis
# plt.scatter(data['version'], data['price'])
# show bar chart
# plt.bar(data['version'], data['price'])
# # separate data chart show
# plt.show()
# print(data.head())
