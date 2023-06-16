import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from pathlib import Path
from typing import Any
import pickle
import consts


def save_data(data: Any, path: str, full_path: str) -> None:
   Path(path).mkdir(parents=True, exist_ok=True)
   with open(full_path, 'wb') as f:
      pickle.dump(data, f)

df = pd.read_csv("/kaggle/input/data-science-salaries-2023/ds_salaries.csv")
x_train = pd.read_pickle(consts.X_TRAIN_FULL)
y_train = pd.read_pickle(consts.Y_TRAIN_FULL)
train = pd.merge(x_train, y_train, on=x_train.index)
x_test = pd.read_pickle(consts.X_TEST_FULL)
y_test = pd.read_pickle(consts.Y_TEST_FULL)
test = pd.merge(x_test, y_test, on=x_test.index)
ntrain = train.shape[0]
ntest = test.shape[0]
all_data = pd.concat((train, test)).reset_index(drop=True)
print("all_data size is : {}".format(all_data.shape))
all_data_na = (all_data.isnull().sum() / len(all_data)) * 100
all_data_na = all_data_na.drop(all_data_na[all_data_na == 0].index).sort_values(ascending=False)[:30]
missing_data = pd.DataFrame({'Missing Ratio': all_data_na})
print(missing_data.head(20))
all_data['experience_level'] = all_data['experience_level'].replace({'SE':'Senior', 'MI':'Mid-level', 'EN':'Entry-level','EX':'Executive-level'})
all_data['employment_type'] = all_data['employment_type'].replace({'FT':'Full-time', 'CT':'Contractual','PT':'Part-time', 'FL':'Freelancer'})
all_data['remote_ratio'] = all_data['remote_ratio'].replace({100: 'On-site', 0:'Remote', 50:'Hybrid'})
all_data['company_size'].replace(['M','L','S'],["medium","Large","Small"],inplace=True)
all_data = all_data.drop(['salary_currency', 'salary'], axis=1)
le=LabelEncoder()
cols = ['experience_level', 'employment_type', 'job_title','salary_currency','employee_residence','company_location','company_size']
all_data[cols]=all_data[cols].apply(LabelEncoder().fit_transform)

train = all_data[:ntrain]
test = all_data[ntrain:]

x_train = train
y_train = y_train

save_data(x_train, consts.X_TRAIN, consts.X_TRAIN_FULL)
save_data(y_train, consts.Y_TRAIN, consts.Y_TRAIN_FULL)

x_test = test
y_test = np.array(y_test['salary_range'])

save_data(x_test, consts.X_TEST, consts.X_TEST_FULL)
save_data(y_test, consts.Y_TEST, consts.Y_TEST_FULL)