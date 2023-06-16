import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime
from pathlib import Path
from typing import Any
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import mean_squared_error

import consts


def save_data(data: Any, path: str, full_path: str) -> None:
   Path(path).mkdir(parents=True, exist_ok=True)
   with open(full_path, 'wb') as f:
      pickle.dump(data, f)
def time_now():
   return datetime.now().strftime("%H:%M:%S")
def print_log(string):
   print(f'@{time_now()} {string}')


print_log('Data read')

X: pd.DataFrame = pd.read_pickle(consts.X_TRAIN_FULL)
Y: pd.DataFrame = pd.read_pickle(consts.Y_TRAIN_FULL)

print_log('Models init')
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=consts.DATA_TEST_SIZE,
                                                    random_state=consts.RANDOM_STATE)

model=RandomForestRegressor(max_depth=7 , max_features=3,n_estimators= 100)

print_log('Fit model')
model.fit(X, Y)

print_log(f"Save model: {model}")
save_data(model, consts.MODEL, consts.MODEL_FULL)