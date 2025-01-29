import argparse
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", type=str, required=True)
    args = parser.parse_args()

    # Caricamento dati
    data = pd.read_csv(args.train)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Addestramento modello
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # Salvataggio modello
    joblib.dump(model, "/opt/ml/model/model.joblib")
