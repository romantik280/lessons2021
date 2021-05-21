import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
import seaborn as sns


df = pd.read_csv('../lessons/training_mush.csv')
df_test= pd.read_csv('../lessons/testing_mush.csv')
y_true= pd.read_csv('../lessons/testing_y_mush.csv')

pd.options.display.max_rows = 50
pd.options.display.max_columns = None
pd.set_option('display.width', 200)




X = df.drop(['class'], axis = 1)
y = df.pop('class')

parameters={'n_estimators':range(10,51,10),
             'max_depth':range(1,13,2),
             'min_samples_leaf':range(1,8),
             'min_samples_split':range(2,10,2)}


rf = RandomForestClassifier(random_state = 0, n_estimators = 10, min_samples_split = 2, min_samples_leaf = 1, max_depth = 9)
pred_mush = rf.fit(X, y).predict(df_test)
print(pred_mush.sum())
#clf = GridSearchCV(rf, parameters, n_jobs=-1, cv=3)
#best_model = clf.fit(X, y).best_params_


sns.heatmap(confusion_matrix(y_true, pred_mush), annot=True,annot_kws={"size": 16})

#print(best_model)
#imp = pd.DataFrame(rf.feature_importances_, index=X.columns, columns=['importance'])
#imp.sort_values('importance').plot(kind='barh', figsize=(12, 8))