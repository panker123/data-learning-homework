# 导入必要的库
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np

# 示例数据集，由于没有具体的数据集，我们创建一个简单的示例
# 这个数据集应该被替换为实际使用的数据集
data = {
    'text': [
        "这是一个非常棒的产品！",
        "我对这次购物体验感到失望。",
        "这个服务真的很差。",
        "我非常喜欢这个应用。",
        "这个餐馆的食物很难吃。",
        "这部电影太精彩了！",
        "我不推荐这家酒店。",
        "这个景点非常值得一游。"
    ],
    'sentiment': [10, -10, -10, 10, -10, 10, -10, 10]  # 情感分数，正数为正面，负数为负面
}

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['sentiment'], test_size=0.2, random_state=42)

# 创建一个SVM模型，使用TF-IDF进行特征提取
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('scaler', StandardScaler(with_mean=False)),  # TF-IDF向量已经是稀疏的，不能计算均值
    ('svm', LinearSVC())
])

# 训练模型
model.fit(X_train, y_train)

# 评估模型
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))

# 示例文本进行情感预测
example_text = ["这个产品真的很不错。", "这次旅行体验非常糟糕。"]
sentiment_scores = model.predict(example_text)
sentiment_scores
