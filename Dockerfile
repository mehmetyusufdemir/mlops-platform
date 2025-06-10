# Temel imaj olarak resmi Python 3.10 slim versiyonunu kullan
FROM python:3.10-slim

# Çalışma dizinini /app olarak ayarla
WORKDIR /app

# Bağımlılık dosyasını kopyala
COPY requirements.txt requirements.txt

# Gerekli kütüphaneleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarının tamamını kopyala
COPY . .

# Konteyner başlatıldığında çalıştırılacak komut
# Gunicorn, Flask'in kendi sunucusundan daha performanslıdır.
# Önce gunicorn'u yükleyelim.
RUN pip install gunicorn

# Uygulamayı gunicorn ile başlat
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]