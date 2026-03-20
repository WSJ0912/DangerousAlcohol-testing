from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="酒后风险预警系统 API", version="1.0")

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 健康检查接口
@app.get("/health", tags=["系统"])
def health_check():
    return {"status": "ok", "message": "服务运行正常"}

# 用户相关接口
try:
    from app.api import users
    app.include_router(users.router, prefix="/api/users", tags=["用户"])
except ImportError:
    print("注意：users模块尚未实现")

# 生理数据相关接口
try:
    from app.api import physio
    app.include_router(physio.router, prefix="/api/physio", tags=["生理数据"])
except ImportError:
    print("注意：physio模块尚未实现")

# 小米手环相关接口
try:
    from app.api import mi_band
    app.include_router(mi_band.router, prefix="/api/mi_band", tags=["小米手环"])
except ImportError:
    print("注意：mi_band模块尚未实现")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)