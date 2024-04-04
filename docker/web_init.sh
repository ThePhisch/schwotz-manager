cd /app

pip install -r requirements.txt
cp /run/secrets/db_password /app/db_password

python main.py