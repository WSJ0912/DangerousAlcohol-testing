Write-Host "正在启动FastAPI服务..."

$backendPath = "c:\Users\31059\Desktop\酒后检测\DrinkWarning-Backend\backend"
$pythonPath = Join-Path $backendPath "venv\Scripts\python.exe"
$mainPath = Join-Path $backendPath "main.py"

Write-Host "切换到: $backendPath"
Set-Location $backendPath

Write-Host "使用Python: $pythonPath"
Write-Host ""
Write-Host "正在启动服务..."
Write-Host "访问 http://localhost:8000/docs 查看API文档"
Write-Host "按 Ctrl+C 停止服务"
Write-Host ""

& $pythonPath $mainPath
