from fastapi import APIRouter

router = APIRouter()

@router.post("/sync")
def sync_mi_band_data():
    return {"message": "小米手环数据同步接口待实现"}

@router.get("/data/{user_id}")
def get_mi_band_data(user_id: int):
    return {"message": f"获取用户 {user_id} 小米手环数据接口待实现"}