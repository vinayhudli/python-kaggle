import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

#checking na functionality
df = pd.DataFrame({'a':[2,np.nan,3,5], "b":[6,np.nan,7,8], "c":[9,10,11,np.nan]})
print("dataframe ",df)
print("dropping missing rows ",df.dropna(axis=0))

melbourne_path = "data/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_path)

#dropping the missing rows
filtered_data = melbourne_data.dropna(axis=0)

# Choose target
y = filtered_data.Price

# Choose features to predict target
melbourne_data_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
x = filtered_data[melbourne_data_features]

#splitting data into training and validation data
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state=0)

#Define model
melbourne_model = DecisionTreeRegressor()
#Fit model
melbourne_model.fit(X=train_x, y=train_y)

from sklearn.metrics import mean_absolute_error
predicted_prices = melbourne_model.predict(X=val_x)
error = mean_absolute_error(val_y, predicted_prices)
print("mean error is ",error)