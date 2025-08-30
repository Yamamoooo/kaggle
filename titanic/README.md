# kaggleのtitanic分析

# 分析の流れ
## 1.ベースライン作成
## 1-1.データセットの分割
FareとPclassを特徴量に指定して、データセットを分割。
この時、trainとvalで生存者の比率を同じになるようにした。

## 1-2.LightGBMを使用
### 精度
Train Accuracy: 0.7669
Validation Accuracy: 0.7207

### 1-3.特徴量の重要度
![alt text](images/feature_importance1.png)

### 1-4.confusion matrix
![alt text](images/confusion_matrix1.png)

### 1-5.予測の確率表示
![alt text](images/predict_prob1.png)

### 1-6.ベースモデルのテスト結果
![alt text](images/first_submission.png)

