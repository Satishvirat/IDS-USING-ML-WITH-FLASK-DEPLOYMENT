from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle

df=pd.read_csv("final dataset with 10 features.csv")
print(df.head(2))

X = df.drop(columns=['Attack Type'])
y = df['Attack Type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Create a Random Forest classifier
clf2 = RandomForestClassifier(random_state=42)

# Train the model on the training data
clf2.fit(X_train, y_train)

pickle.dump(clf2,open("model.pkl","wb"))