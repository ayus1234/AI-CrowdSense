FROM python:3.10-slim

WORKDIR /app

# Copy the backend requirements first for Docker caching
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy backend and frontend source
COPY backend ./backend
COPY frontend ./frontend

# Expose the port that Cloud Run expects
EXPOSE 8080

# Environment variables
ENV PORT=8080

# Run the FastAPI app
CMD ["python", "backend/app.py"]
