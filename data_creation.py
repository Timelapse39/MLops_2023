from typing import Any
from sklearn.datasets import make_moons, make_circles, make_classification
import numpy as np
from datetime import datetime
import pickle
from pathlib import Path
import consts
import pandas as pd
from sklearn.model_selection import train_test_split

def save_data(data: Any, path: str, full_path: str) -> None:
   Path(path).mkdir(parents=True, exist_ok=True)
   with open(full_path, 'wb') as f:
      pickle.dump(data, f)


def time_now():
   return datetime.now().strftime("%H:%M:%S")



print(f'{time_now()} Загрузка данных')
data = pd.read_csv(consts.DATA_PATH, delimiter=',')
x = data.drop(columns=["salary_range"])
y = data["salary_range"]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=consts.DATA_TEST_SIZE, random_state=consts.RANDOM_STATE)
print(f'{time_now()} Сохранение данных')
save_data(X_train, consts.X_TRAIN, consts.X_TRAIN_FULL)
save_data(X_test, consts.X_TEST, consts.X_TEST_FULL)
save_data(y_train, consts.Y_TRAIN, consts.Y_TRAIN_FULL)
save_data(y_test, consts.Y_TEST, consts.Y_TEST_FULL)
