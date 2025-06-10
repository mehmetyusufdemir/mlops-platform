from flask import Flask, jsonify, request,render_template
import mlflow
import mlflow.pyfunc
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd

# --- DEĞİŞİKLİK YOK ---
app = Flask(__name__, template_folder='../templates')
mlflow.set_tracking_uri("http://mlflow-server:5000")


@app.route('/', methods=['GET'])
def index():
    #return jsonify({"status": "ok", "message": "Ana sayfa testi basarili!"})
    return render_template('index.html')


# --- /train ENDPOINT'İ TAMAMEN GÜNCELLENDİ ---
@app.route('/train', methods=['GET'])
def train_model():
    """Iris veri setini kullanarak bir Logistic Regression modeli eğitir ve MLflow'a loglar."""
    try:
        with mlflow.start_run() as run:
            # 1. Gerçek veri setini yükle
            iris = load_iris()
            X = iris.data
            y = iris.target

            # 2. Veriyi eğitim ve test setlerine ayır
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # 3. Modeli ve parametreleri tanımla
            C_param = request.args.get('C', default=1.0, type=float)
            lr = LogisticRegression(C=C_param, max_iter=200)  # Daha hızlı yakınsaması için max_iter eklendi
            lr.fit(X_train, y_train)

            # 4. Modeli test verisi ile değerlendir
            y_pred = lr.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)

            # 5. Parametreleri ve gerçek metrikleri MLflow'a logla
            mlflow.log_param("C", C_param)
            mlflow.log_param("dataset", "iris")
            mlflow.log_metric("accuracy", accuracy)

            # 6. Modeli yeni bir isimle MLflow'a logla
            mlflow.sklearn.log_model(lr, "iris-logistic-regression-model")

            run_id = run.info.run_id
            return jsonify({
                "status": "success",
                "message": "Iris model trained and logged to MLflow successfully.",
                "run_id": run_id,
                "accuracy": accuracy
            })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# --- /predict ENDPOINT'İNDE DEĞİŞİKLİK YOK, SADECE GÖNDERİLECEK VERİ DEĞİŞECEK ---
@app.route('/predict', methods=['POST'])
def predict():
    """Kaydedilmiş bir modeli kullanarak tahmin yapar."""
    try:
        data = request.get_json()
        run_id = data.get('run_id')
        # Iris veri seti 4 özellikli olduğu için, gelen veri de 4 sütunlu olmalı
        predict_data = data.get('data')

        if not run_id or not predict_data:
            return jsonify({"status": "error", "message": "Missing 'run_id' or 'data' in request body"}), 400

        model_uri = f"runs:/{run_id}/iris-logistic-regression-model"
        loaded_model = mlflow.pyfunc.load_model(model_uri)
        data_to_predict = pd.DataFrame(predict_data)
        prediction = loaded_model.predict(data_to_predict)

        return jsonify({
            "status": "success",
            "run_id": run_id,
            "prediction": prediction.tolist()
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500