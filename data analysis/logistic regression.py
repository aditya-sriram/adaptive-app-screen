import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

filepath = "C:/Users/adity/Desktop/School/Adaptive App Screen/datasets/UbiqLog4UCI/Labelled/03-08--20-45-03/10_M.json"
df = pd.read_json(filepath)

df["ProcessName"] = df["ProcessName"].map(hash)

X = df[["ProcessName", "Day", "Hour"]]
Y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

model = LogisticRegression()
model.fit(X_train, y_train)
model.predict(X_test)
accuracy = model.score(X_test,y_test)

print(accuracy)

filename = "model"
outfile = open(filename, "wb")
pickle.dump(model, outfile)
outfile.close()