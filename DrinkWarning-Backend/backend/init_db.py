from app.core.database import Base, engine
from app.models.user import User

def init_database():
    print("正在创建数据库表...")
    Base.metadata.create_all(bind=engine)
    print("✅ 数据库表创建完成！")
    
    from sqlalchemy.orm import Session
    from app.core.database import SessionLocal
    
    db = SessionLocal()
    try:
        user_count = db.query(User).count()
        print(f"当前用户表中的记录数: {user_count}")
    finally:
        db.close()
    print("✅ 数据库连接测试成功！")

if __name__ == "__main__":
    init_database()
