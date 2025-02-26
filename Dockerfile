# Use Python base image
FROM python:3.12.4

# Set working directory
WORKDIR /app

COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt


# Copy files
COPY . /app/


# Expose port
EXPOSE 8001 8501

# Run FastAPI app
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
CMD uvicorn main:app --host 0.0.0.0 --port 8001 & streamlit run app.py --server.port=8501 --server.address=0.0.0.0