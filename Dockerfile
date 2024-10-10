FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
COPY app.py ./
COPY Modelfile ./
COPY Llama-3-ELYZA-JP-8B-q4_k_m.gguf ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]