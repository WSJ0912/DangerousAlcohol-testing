# DrinkWarning-Backend - 酒后检测系统后端

## 项目简介

基于深度学习的酒后驾驶检测系统后端，集成面部识别、生理数据分析和多模态融合技术，为全国计算机设计大赛准备。

## 项目结构

```
DrinkWarning-Backend/
├── backend/                  # 后端代码
│   ├── app/ 
│   │   ├── api/              # 接口层
│   │   │   ├── mi_band.py      # 小米手环API对接
│   │   │   ├── physio.py       # 生理数据接口
│   │   │   ├── prediction.py   # 预测接口
│   │   │   └── hardware.py     # 硬件数据接口
│   ├── models/               # 数据库ORM模型
│   ├── schemas/              # Pydantic数据模型
│   └── core/                # 核心配置
│   ├── main.py               # FastAPI入口文件
│   └── requirements.txt      # Python依赖
├── model/                    # 模型代码
│   ├── lstm/                 # LSTM生理时序模型
│   ├── face/                 # 面部识别模型
│   ├── fusion/               # 多模态融合逻辑
│   ├── mi_band/              # 小米手环数据处理
│   │   ├── api_client.py     # API客户端
│   │   ├── data_processor.py # 数据清洗和转换
│   │   └── sync.py          # 数据同步逻辑
│   ├── datasets/             # 数据集
│   └── logs/                # 训练日志
├── hardware/                 # 硬件代码
│   ├── esp32/                # ESP32固件
│   └── schematic/            # 硬件原理图
├── docs/                     # 文档
│   ├── mi_band_api.md        # 小米API文档
│   ├── database_er.png       # 数据库ER图
│   ├── training_logs/        # 训练日志截图
│   ├── test_results/         # 测试结果
│   └── hardware_demo/        # 硬件演示素材
└── README.md
```

## 技术栈

### 后端

- **FastAPI**: 现代高性能Web框架
- **SQLAlchemy**: ORM数据库操作
- **Pydantic**: 数据验证
- **Uvicorn**: ASGI服务器

### 深度学习

- **PyTorch**: 深度学习框架
- **OpenCV**: 图像处理
- **NumPy**: 数值计算

### 硬件

- **ESP32**: 嵌入式开发板
- **MQ-3**: 酒精传感器

## 快速开始

### 1. 环境配置

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate  # Linux/Mac

# 安装依赖
pip install -r backend/requirements.txt
```

### 2. 数据库初始化

```bash
cd backend
python init_db.py
```

### 3. 启动服务

```bash
cd backend
python main.py
```

服务将在 `http://localhost:8000` 启动

### 4. 访问API文档

打开浏览器访问 `http://localhost:8000/docs` 查看Swagger API文档

## 核心功能

### 1. 小米手环数据对接

- 自动同步手环数据
- 数据清洗和标准化
- 实时数据监控

### 2. 生理数据分析

- 心率时序分析
- 睡眠质量评估
- 步数统计

### 3. 面部识别

- 酒后面部特征提取
- 实时检测
- 置信度评估

### 4. 多模态融合

- 面部+生理数据融合
- 风险评分计算
- 预警机制

### 5. 硬件接口

- ESP32数据接收
- 酒精传感器数据处理
- 设备状态监控

## API接口

### 生理数据接口

- `POST /api/physio/upload` - 上传生理数据
- `GET /api/physio/{user_id}` - 查询用户生理数据
- `GET /api/physio/stats/{user_id}` - 获取统计数据

### 预测接口

- `POST /api/prediction/face` - 面部预测
- `POST /api/prediction/physio` - 生理预测
- `POST /api/prediction/fusion` - 融合预测

### 硬件接口

- `POST /api/hardware/upload` - 上传硬件数据
- `GET /api/hardware/status` - 设备状态

## 模型训练

### LSTM生理模型

```bash
cd model/lstm
python train.py --epochs 100 --batch_size 32
```

### 面部识别模型

```bash
cd model/face
python train.py --epochs 50 --batch_size 16
```

### 融合模型

```bash
cd model/fusion
python train.py --face_model ../face/best.pth --physio_model ../lstm/best.pth
```

## 数据集准备

### 酒后面部数据集

- 格式：图像文件
- 分类：drunk/sober
- 划分：train/val/test = 7:2:1

### 生理数据集

- 格式：CSV
- 字段：heart\_rate, steps, deep\_sleep\_ratio, is\_drunk, timestamp

### 模拟驾驶数据

- 格式：CSV
- 字段：steering\_frequency, lane\_deviation, brake\_intensity, is\_normal, timestamp

## 部署

### Docker部署

```bash
docker build -t drink-warning-backend .
docker run -p 8000:8000 drink-warning-backend
```

### 生产环境配置

1. 修改 `backend/app/core/config.py` 中的配置
2. 设置环境变量
3. 配置数据库连接
4. 启用HTTPS

## 测试

### 运行测试

```bash
pytest tests/
```

### API测试

使用Postman或curl测试API接口

## 文档

- [API文档](docs/mi_band_api.md)
- [数据库设计](docs/database_er.png)
- [训练日志](docs/training_logs/)
- [测试结果](docs/test_results/)

## 贡献指南

1. Fork项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 许可证

MIT License

## 联系方式

- 项目负责人：\[王烁杰]
- 邮箱：\[3105943895\@qq.com]
- GitHub：\[WSJ0912]

## 致谢

感谢所有为本项目做出贡献的开发者。

***

**注意**: 本项目为参加全国计算机设计大赛而开发，请勿用于商业用途。
