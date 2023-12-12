#02200201006 Samed Sonkaya powershellden oluşturduğum kodlar burada bulunmaktadır.
#Ekran görüntülerim AcikKaynakYazilimGelistirmenin altındaki :
#systemctl_status_nginx, systemctl_status_sunucu ve gunicorn_test dosyalarıdır.
#İlgilendiğiniz için teşekkürler, iyi günler.

#app.py
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


#wsgi.py
from app import app

if __name__ == "__main__":
    app.run()

#etc.systemd.system.(dosya içi)
[Unit]
Description=Ornek uygulama
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/AcikKaynakYazilimGelistirme
ExecStart=/home/ubuntu/.local/bin/gunicorn --workers 3 --bind unix:app.sock wsgi:app

[Install]
WantedBy=multi-user.target

#sudo vim /etc/nginx/sites-available/app
server {
listen 82;

location / {
  include proxy_params;
  proxy_pass http://unix:/home/ubuntu/AcikKaynakYazilimGelistirme/app.sock;
    }
location /static  {
    include  /etc/nginx/mime.types;
    root /home/harry/myFlaskApp/;
  }
}