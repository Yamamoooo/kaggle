# kaggleのtitanic分析

# 分析の流れ
## 1.ベースライン作成
## 1-1.データセットの分割
FareとPclassを特徴量に指定して、データセットを分割。
この時、trainとvalで生存者の比率を同じになるようにした。


## 1-2.LightGBMを使用
### 精度
![alt text](images/feature_importance1.png)

### 1-3.特徴量の重要度
col	imp
0	Fare	1013.661127
1	Pclass	474.618153

### 1-4.confusion matrix
![alt text](images/confusion_matrix1.png)

### 1-5.予測の確率表示
![alt text](images/predict_prob1.png)

### 1-6.ベースモデルのテスト結果
![alt text](images/first_submission.png)

