import os

folders = [
    "routes", "logic", "utils", "models", "templates", "static/css", "instance"
]
files = {
    "app.py": "",
    "config.py": "# إعدادات التكوين العامة\n",
    "requirements.txt": "flask\nflask_sqlalchemy\n",
    "routes/__init__.py": "",
    "logic/__init__.py": "",
    "utils/__init__.py": "",
    "models/__init__.py": "",
    "models/models.py": "# هنا تعريف الجداول باستخدام SQLAlchemy\n",
    "static/css/style.css": "body { font-family: Arial; }"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file_path, content in files.items():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ تم إنشاء هيكل مشروع Flask احترافي بنجاح.")
