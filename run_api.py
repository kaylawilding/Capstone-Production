import numpy as np
import requests
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
df_test_X =pd.read_csv('./data/testX.csv')

X_test = df_test_X.to_numpy()

# Serialize the data into json and send the request to the model
payload = {'data': json.dumps(X_test.tolist())}
y_predict = requests.post('http://127.0.0.1:5000/loandefault', json=payload).json()

y_predict = np.array(y_predict)
y_predict = pd.DataFrame(y_predict)
print(y_predict)

test_y = pd.read_csv('./data/testy.csv')
test_y = pd.DataFrame(test_y['Status'])

accuracy = accuracy_score(test_y, y_predict)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
