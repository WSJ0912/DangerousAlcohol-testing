from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return {"message": "用户接口待实现"}

@router.post("/")
def create_user():
    return {"message": "创建用户接口待实现"}

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"message": f"获取用户 {user_id} 接口待实现"}