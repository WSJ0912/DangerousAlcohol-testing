from fastapi import APIRouter

router = APIRouter()

@router.post("/upload")
def upload_physio_data():
    return {"message": "生理数据上传接口待实现"}

@router.get("/{user_id}")
def get_physio_data(user_id: int):
    return {"message": f"获取用户 {user_id} 生理数据接口待实现"}