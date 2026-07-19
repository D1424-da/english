#!/bin/bash
# English Diagnosis App - Linux/Mac Setup Script
# Run: chmod +x setup.sh && ./setup.sh

echo "=== English Diagnosis App Setup ==="
echo ""

# Backend setup
echo "[1/4] Backend setup..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -q
echo "  Dependencies installed"

# Seed data
echo "[2/4] Database setup..."
if [ ! -f "english_app.db" ]; then
    python -m seed.seed_data
    echo "  Database created and seeded"
else
    echo "  Database already exists"
fi
cd ..

# Frontend setup
echo "[3/4] Frontend setup..."
cd frontend
npm install --silent
npm run build
echo "  Frontend built"
cd ..

# Done
echo ""
echo "[4/4] Setup complete!"
echo ""
echo "=== How to run ==="
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  python main.py"
echo ""
echo "  Then open: http://localhost:8000"
echo ""
