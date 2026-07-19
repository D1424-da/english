FROM python:3.11-slim AS backend

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

FROM node:18-slim AS frontend-build

WORKDIR /frontend
COPY frontend/package.json .
RUN npm install
COPY frontend/ .
RUN npm run build

FROM python:3.11-slim

WORKDIR /app

COPY --from=backend /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=backend /usr/local/bin /usr/local/bin
COPY backend/ .
COPY --from=frontend-build /frontend/dist ../frontend/dist

ENV DATABASE_URL=sqlite:///./english_app.db
ENV ANTHROPIC_API_KEY=sk-ant-your-key-here
ENV FRONTEND_URL=http://localhost:3000

EXPOSE 8000

CMD ["sh", "-c", "python -m seed.seed_data && uvicorn main:app --host 0.0.0.0 --port 8000"]
