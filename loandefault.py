import pandas as pd
import numpy as np 
from scipy.stats import zscore
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer, make_column_selector
from xgboost import XGBClassifier
import pickle
from transformode import DataFrameOneHotEncoder 


loan_df = pd.read_csv('Raw Data/Loan_Default.csv')

y = loan_df['Status']
loan_df = loan_df.drop(columns=['Status', 'ID', 'rate_of_interest','Interest_rate_spread', 'Upfront_charges'])

loan_df['year'] = str(loan_df['year'])
cat = loan_df[make_column_selector(dtype_include= object)]
dfohe = DataFrameOneHotEncoder()
catx = dfohe.fit_transform(cat)

numdf = loan_df[make_column_selector(dtype_include= np.number)]
ss = StandardScaler()
numx = pd.DataFrame(ss.fit_transform(numdf), columns=numdf.columns)

X = numx.join(catx)

X = X.fillna(value =0)

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.2,  random_state=12)

train_X.columns = train_X.columns.str.replace("[[]", "_")
train_X.columns = train_X.columns.str.replace("[]]", "_")
train_X.columns = train_X.columns.str.replace("[<]", "less_than")
train_X.columns = train_X.columns.str.replace("[>]", "greater_than")
test_X.columns = test_X.columns.str.replace("[[]", "_")
test_X.columns = test_X.columns.str.replace("[]]", "_")
test_X.columns = test_X.columns.str.replace("[<]", "less_than")
test_X.columns = test_X.columns.str.replace("[>]", "greater_than")

# fit model on training data
parameters = {
    'max_depth': range (2, 10, 1),
    'n_estimators': range(60, 220, 40),
    'learning_rate': [0.1, 0.01, 0.05]
}
xgbmodel = XGBClassifier(
    objective= 'binary:logistic',
    nthread=4,
    seed=42
)
grid_search = GridSearchCV(
    estimator=xgbmodel,
    param_grid=parameters,
    scoring = 'roc_auc',
    n_jobs = 10,
    cv = 10,
    verbose=True
)
grid_search.fit(train_X, train_y)

# Dictionary of best parameters
best_xgb_params = grid_search.best_params_
# Best XGB model that was found based on the metric score you specify
best_xgb_model = grid_search.best_estimator_
# Save model
pickle.dump(grid_search.best_estimator_, open("xgb_model.pickle", "wb"))

# make predictions for test data
y_pred = best_xgb_model.predict(test_X)
predictions = [round(value) for value in y_pred]

