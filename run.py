from app.main import app

if __name__ == '__main__':
    # Uygulamayı başlat
    # host='0.0.0.0' -> Docker içinde çalışabilmesi için önemli
    app.run(host='0.0.0.0', port=5000, debug=True)