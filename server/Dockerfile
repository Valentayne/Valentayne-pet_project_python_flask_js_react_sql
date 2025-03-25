FROM python:3.12.4-slim AS builder  

WORKDIR /install  

COPY requirements.txt .  

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt  

FROM python:3.12.4-slim  

WORKDIR /app  

COPY --from=builder /install /usr/local  
COPY . .  

EXPOSE 5000  

ENTRYPOINT [ "python3" ]  
CMD ["main.py"]