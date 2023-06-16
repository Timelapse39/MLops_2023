from sklearn.datasets import make_moons, make_circles, make_classification
import numpy as np
from datetime import datetime
import pickle
from pathlib import Path
import consts
from sklearn.model_selection import train_test_split


def make_bin_clf(N, method="line", noises=0.15, random_state=1337):
    if random_state:
        rng = np.random.RandomState(seed=random_state)

    if method == "line" or method is None:
        X, y = make_classification(n_samples=N, n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1,
                                   class_sep=2)
        X += np.random.randn(*X.shape) * noises
    elif method == "moons":
        X, y = make_moons(n_samples=N, noise=noises)

    elif method == "circles":
        X, y = make_circles(n_samples = N, noise = noises, factor = 0.5)

        return X, y

def time_now():
   return datetime.now().strftime("%H:%M:%S")

if __name__ == '__main__':
  print(f'{time_now()} Генерация данных')
  x, y = make_bin_clf(N = consts.DATA_N, noises = 0.15, noise_power=consts.DATA_NOISE_POWER, seed=1337)
  X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=consts.DATA_TEST_SIZE, random_state=consts.RANDOM_STATE)

  print(f'{time_now()} Сохранение данных')
  Path(consts.X_TRAIN).mkdir(parents=True, exist_ok=True)
  with open(consts.X_TRAIN_FULL, 'wb') as f:
    pickle.dump(X_train, f)

  Path(consts.X_TEST).mkdir(parents=True, exist_ok=True)
  with open(consts.X_TEST_FULL, 'wb') as f:
    pickle.dump(X_test, f)

  Path(consts.Y_TRAIN).mkdir(parents=True, exist_ok=True)
  with open(consts.Y_TRAIN_FULL, 'wb') as f:
    pickle.dump(y_train, f)

  Path(consts.Y_TEST).mkdir(parents=True, exist_ok=True)
  with open(consts.Y_TEST_FULL, 'wb') as f:
    pickle.dump(y_test, f)