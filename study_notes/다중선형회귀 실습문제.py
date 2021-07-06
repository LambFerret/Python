# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 01:33:44 2021

@author: LambFerret
"""

# 필요한 라이브러리 import
from sklearn import datasets
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd  

# 당뇨병 데이터 갖고 오기
diabetes_dataset = datasets.load_diabetes()

# 입력 변수를 사용하기 편하게 pandas dataframe으로 변환
x = pd.DataFrame(diabetes_dataset.data, columns=diabetes_dataset.feature_names)

# 목표 변수를 사용하기 편하게 pandas dataframe으로 변환
y = pd.DataFrame(diabetes_dataset.target, columns=['diabetes'])

x_train, x_test, y_train, y_test = tts(x, y, test_size=0.2, random_state=5)
lr = LinearRegression()
lr.fit(x_train, y_train)
y_test_predict = lr.predict(x_test)
# 코드를 쓰세요

# 평균 제곱 오차의 루트를 통해서 테스트 데이터에서의 모델 성능 판단
mse = mean_squared_error(y_test, y_test_predict)

mse ** 0.5
