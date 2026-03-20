import sys
import os

print("正在启动FastAPI服务...")

try:
    import fastapi
    print(f"✅ FastAPI版本: {fastapi.__version__}")
except ImportError:
    print("❌ FastAPI未安装")
    sys.exit(1)

try:
    import sqlalchemy
    print(f"✅ SQLAlchemy版本: {sqlalchemy.__version__}")
except ImportError:
    print("❌ SQLAlchemy未安装")
    sys.exit(1)

try:
    import pydantic
    print(f"✅ Pydantic版本: {pydantic.__version__}")
except ImportError:
    print("❌ Pydantic未安装")
    sys.exit(1)

print("\n正在启动服务...")
print("访问 http://localhost:8000/docs 查看API文档")
print("按 Ctrl+C 停止服务\n")

os.system("python main.py")
