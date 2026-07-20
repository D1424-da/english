# English Diagnosis App - Windows Setup Script
# PowerShell で実行: .\setup.ps1

Write-Host "=== English Diagnosis App Setup ===" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "[1/6] Python checking..." -ForegroundColor Yellow
try {
    $pyVer = python --version 2>&1
    Write-Host "  OK: $pyVer" -ForegroundColor Green
} catch {
    Write-Host "  ERROR: Python not found. Install from https://www.python.org/" -ForegroundColor Red
    exit 1
}

# Check Node.js
Write-Host "[2/6] Node.js checking..." -ForegroundColor Yellow
try {
    $nodeVer = node --version 2>&1
    Write-Host "  OK: Node.js $nodeVer" -ForegroundColor Green
} catch {
    Write-Host "  ERROR: Node.js not found. Install from https://nodejs.org/" -ForegroundColor Red
    exit 1
}

# Backend setup
Write-Host "[3/6] Backend setup..." -ForegroundColor Yellow
Set-Location backend
if (-not (Test-Path "venv")) {
    python -m venv venv
    Write-Host "  Created virtual environment" -ForegroundColor Green
}
& .\venv\Scripts\Activate.ps1
pip install -r requirements.txt --quiet
Write-Host "  Dependencies installed" -ForegroundColor Green

# Seed data
Write-Host "[4/6] Database setup..." -ForegroundColor Yellow
if (-not (Test-Path "english_app.db")) {
    python -m seed.seed_data
    Write-Host "  Database created and seeded" -ForegroundColor Green
} else {
    Write-Host "  Database already exists" -ForegroundColor Green
}
Set-Location ..

# Frontend setup
Write-Host "[5/6] Frontend setup..." -ForegroundColor Yellow
Set-Location frontend
npm install --silent
npm run build
Write-Host "  Frontend built" -ForegroundColor Green
Set-Location ..

# Done
Write-Host ""
Write-Host "[6/6] Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "=== How to run ===" -ForegroundColor Cyan
Write-Host "  cd backend" -ForegroundColor White
Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "  python main.py" -ForegroundColor White
Write-Host ""
Write-Host "  Then open: http://localhost:8000" -ForegroundColor Yellow
Write-Host ""
