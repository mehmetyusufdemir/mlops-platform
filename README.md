MLOps Platform Prototipi 🚀
Bu proje, bir makine öğrenmesi modelinin eğitiminden sunulmasına kadar olan tüm yaşam döngüsünü kapsayan, uçtan uca bir MLOps platformu prototipidir. Sistem, modern DevOps ve MLOps pratikleri kullanılarak konteynerleştirilmiş servisler üzerine inşa edilmiştir.

🏛️ Mimari ve İşleyiş
Proje, Docker Compose ile yönetilen bir mikroservis mimarisine sahiptir. Temel işleyiş aşağıdaki gibidir:

Kullanıcı Arayüzü (Frontend): Kullanıcı, basit web arayüzü üzerinden model eğitimi veya tahmin talebinde bulunur.
API Sunucusu (Flask App): İstekleri karşılayan ana uygulamadır.
/train isteği geldiğinde, Iris veri seti üzerinde bir model eğitir.
Eğitim parametrelerini ve metriklerini MLflow Tracking Server'a kaydeder.
Eğitilmiş model dosyasını (artifact) MinIO depolama servisine gönderir.
/predict isteği geldiğinde, belirtilen modeli MLflow ve MinIO üzerinden yükler ve gelen veri için tahmin yapar.
MLflow Server: Tüm deneylerin (parametreler, metrikler, vb.) meta verilerini takip eden ve saklayan servistir. Modellerin nerede saklandığı bilgisini tutar.
MinIO Server: Eğitilmiş modeller gibi büyük dosyaların saklandığı S3 uyumlu bir nesne depolama servisidir.
<!-- end list -->

Kod snippet'i

graph TD
    A[👨‍💻 Kullanıcı] -->|Tarayıcı| B(🌐 Frontend);
    B -->|API Çağrısı| C{🚀 Flask API};
    C -->|Loglama| D[📊 MLflow Server];
    C -->|Model Yükleme/Kaydetme| E[📦 MinIO Storage];
    D -->|Artifact Konumu| E;
✨ Özellikler
API ile Model Eğitimi: Tek bir GET isteği ile modelin eğitilmesi ve versiyonlanması.
API ile Tahmin: POST isteği ile daha önce eğitilmiş herhangi bir modelin kullanılarak tahmin yapılması.
Deney Takibi: MLflow ile tüm model eğitimlerinin parametre ve metriklerinin takibi.
Model ve Artifact Depolama: MinIO ile eğitilmiş modellerin kalıcı ve güvenli bir şekilde saklanması.
İnteraktif Arayüz: Modelleri eğitmek ve test etmek için basit ve kullanıcı dostu bir web arayüzü.
Konteynerleştirilmiş Altyapı: Tüm servislerin Docker ile izole edilmesi ve Docker Compose ile kolayca yönetilmesi.
🛠️ Kullanılan Teknolojiler
Backend: Python, Flask, Gunicorn
MLOps & Veri: MLflow, Scikit-learn, Pandas
Altyapı & Konteynerleştirme: Docker, Docker Compose
Veritabanı & Depolama: MinIO (S3 Uyumlu), SQLite
Frontend: HTML, CSS, JavaScript (Fetch API)
🚀 Kurulum ve Çalıştırma
Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

Projeyi Klonlayın:

Bash

git clone https://github.com/mehmetyusufdemir/mlops-platform.git
cd mlops-platform
Docker Servislerini Başlatın:
Projenin ana dizinindeyken aşağıdaki komutu çalıştırın. Bu komut, gerekli imajları indirecek, build edecek ve tüm servisleri başlatacaktır.

Bash

docker-compose up --build
Arayüzlere Erişin:
Sistem tamamen ayağa kalktıktan sonra, aşağıdaki adreslerden servislere ulaşabilirsiniz:

MLOps Platform Arayüzü: http://localhost:5003
MLflow Paneli: http://localhost:5002
MinIO Konsolu: http://localhost:9001 (Kullanıcı Adı: minioadmin, Şifre: minioadmin)
📖 Kullanım
http://localhost:5003 adresine gidin.
"Yeni Model Eğit" butonuna tıklayın. "Sonuçlar" bölümünde başarılı bir yanıt ve run_id göreceksiniz.
Oluşturulan run_id, tahmin bölümündeki "Run ID" kutusuna otomatik olarak dolacaktır.
Tahmin yapmak için 4 adet sayısal özellik girin ve "Tahmin Yap" butonuna tıklayın.
Sonucu "Sonuçlar" bölümünde görün.
&lt;br>

MLOps Platform Prototype 🚀
This project is an end-to-end MLOps platform prototype that covers the entire lifecycle of a machine learning model, from training to serving. The system is built on containerized services using modern DevOps and MLOps practices.

🏛️ Architecture and Workflow
The project utilizes a microservice architecture managed by Docker Compose. The basic workflow is as follows:

User Interface (Frontend): The user initiates a model training or prediction request through a simple web interface.
API Server (Flask App): This is the main application that handles requests.
On a /train request, it trains a model on the Iris dataset.
It logs the training parameters and metrics to the MLflow Tracking Server.
It sends the trained model file (artifact) to the MinIO storage service.
On a /predict request, it loads the specified model from MLflow and MinIO and makes a prediction on the new data.
MLflow Server: A service that tracks and stores the metadata of all experiments (parameters, metrics, etc.). It holds the information about where the models are stored.
MinIO Server: An S3-compatible object storage service where large files, such as trained models, are stored.
<!-- end list -->

Kod snippet'i

graph TD
    A[👨‍💻 User] -->|Browser| B(🌐 Frontend);
    B -->|API Call| C{🚀 Flask API};
    C -->|Logging| D[📊 MLflow Server];
    C -->|Model Load/Save| E[📦 MinIO Storage];
    D -->|Artifact Location| E;
✨ Features
API-Driven Model Training: Train and version a model with a single GET request.
API-Driven Prediction: Use any previously trained model to make predictions via a POST request.
Experiment Tracking: Track parameters and metrics of all training runs with MLflow.
Model & Artifact Storage: Persistently and securely store trained models with MinIO.
Interactive UI: A simple and user-friendly web interface to train and test models.
Containerized Infrastructure: All services are isolated with Docker and easily managed with Docker Compose.
🛠️ Tech Stack
Backend: Python, Flask, Gunicorn
MLOps & Data: MLflow, Scikit-learn, Pandas
Infrastructure & Containerization: Docker, Docker Compose
Database & Storage: MinIO (S3-Compatible), SQLite
Frontend: HTML, CSS, JavaScript (Fetch API)
🚀 Setup and Running
Follow these steps to run the project on your local machine:

Clone the Repository:

Bash

git clone https://github.com/mehmetyusufdemir/mlops-platform.git
cd mlops-platform
Start Docker Services:
From the project's root directory, run the following command. This will download the necessary images, build the custom image, and start all services.

Bash

docker-compose up --build
Access the Interfaces:
After the system is fully up and running, you can access the services at the following addresses:

MLOps Platform UI: http://localhost:5003
MLflow Dashboard: http://localhost:5002
MinIO Console: http://localhost:9001 (Username: minioadmin, Password: minioadmin)
📖 Usage
Navigate to http://localhost:5003.
Click the "Yeni Model Eğit" (Train New Model) button. You will see a success response and a run_id in the results area.
The generated run_id will be auto-filled into the "Run ID" input box in the prediction section.
Enter 4 numerical features to make a prediction and click the "Tahmin Yap" (Make Prediction) button.
See the prediction result in the results area.
