import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn

def dataset_import(data_name, output_column):
    df = pd.read_csv(data_name)
    X = df.drop(output_column, axis = 'columns', inplace = False).values
    Y = df.output_column.values

def fill_missingdata(X):
    imputer = sklearn.impute.SimpleImputer(missing_values = np.nan, strategy='mean')
    imputer.fit(X)
    X = imputer.transform(X)

def encoding_independant(X):
    ct = sklearn.compose.ColumnTransformer([('encoder', sklearn.preprocessing.OneHotEncoder(), [0])], remainder = 'passthrough')
    X = np.array(ct.fit_transform(X))

def encoding_dependant(Y):
    le = sklearn.preprocessing.LabelEncoder()
    Y = le.fit_transform(Y)

def split_dataset_test_train(X, Y, test_ratio):
    X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, test_size = test_ratio, random_state = 1)