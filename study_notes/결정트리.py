# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:45:40 2021

@author: LambFerret
"""
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split as tts
from sklearn.tree import DecisionTreeClassifier 
import pandas as pd

# 데이터 셋 불러 오기
cancer_data = load_breast_cancer()
# 데이터 셋을 살펴보기 위한 코드
X = pd.DataFrame(cancer_data.data, columns = cancer_data.feature_names)
y = pd.DataFrame(cancer_data.target, columns = ['class'])
x_train, x_test, y_train, y_test = tts(X, y, test_size=0.2, random_state=5)
# 코드를 쓰세요
dtc = DecisionTreeClassifier(max_depth = 5, random_state=(42))
dtc.fit(x_train, y_train)

predictions = dtc.predict(x_train)
score = dtc.score(x_test, y_test)

predictions, score

"""
이번 과제에서는 sklearn 라이브러리의 유방암 데이터 셋을 학습에 사용할 수 있게 준비해보겠습니다. 
유방암 데이터 셋은 전 토픽들에서 한 번도 보지 않은 데이터 셋인데요. 간단히만 설명드리겠습니다.

암은 사람한테 치명적인 악성(malignant)과 그렇지 않은 양성(benign)암으로 나뉩니다. 
sklearn 유방암 데이터 셋은 유방암세포들의 다양한 속성들과 (길이, 넓이, 둘레 등등) 암이 악성인지 양성인지를 저장하고 있습니다.

(채점되지는 않지만, 꼭 print(cancer_data.DESCR)를 실행해서 데이터 셋을 살펴보세요.)

데이터 셋은 load_breast_cancer 함수를 호출해서 cancer_data 변수에 저장했습니다.
속성들은 cancer_data.data에, 악성인지 양성인지는 cancer_data.target에 저장돼있습니다.
속성 이름은 cancer_data.feature_names에 저장돼있고, 목표 변수 열 이름은 "class"로 지어주세요.
해야할 일
print(cancer_data.DESCR)를 해서 유방암 데이터를 살펴보세요. (채점하지는 않음)
cancer_data 변수에 저장된 데이터를 입력과 목표 변수로 나눠서 pandas dataframe에 저장하세요.
train_test_split를 이용해서 데이터 셋을 training/test 셋으로 나누세요.
조건
채점을 위해서 train_test_split 옵셔널 파라미터는 test_size=0.2, random_state=5로 설정하세요.
향후 모델을 학습시킬 때 경고 메시지가 나오지 않게 training set 
목표 변수에 대해서 y_train = y_train.values.ravel() 이 코드를 추가해주세요.
채점은 X_train.head()를 출력해서 확인합니다.
"""