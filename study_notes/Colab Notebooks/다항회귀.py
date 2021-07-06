# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 09:20:22 2021

@author: LambFerret
"""

# 필요한 라이브러리 import
from sklearn import datasets
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd  

diabetes_dataset = datasets.load_diabetes()  # 데이터 셋 갖고오기
pn = PolynomialFeatures(2)
pn_data = pn.fit_transform(diabetes_dataset.data)
pn_data.shape
pn_feature = pn.get_feature_names(diabetes_dataset.feature_names)
x = pd.DataFrame(pn_data, columns=(pn_feature))

# 코드를 쓰세요

# 목표 변수
y = pd.DataFrame(diabetes_dataset.target, columns=['diabetes'])
x_train, x_test, y_train, y_test = tts(x, y, test_size=0.2, random_state=5)
lr = LinearRegression()
lr.fit(x_train, y_train)
y_test_predict = lr.predict(x_test)
# 코드를 쓰세요

mse = mean_squared_error(y_test, y_test_predict)
mse ** 0.5
lr.score(x_test, y_test)
