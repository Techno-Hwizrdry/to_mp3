FROM python:3.10.11
WORKDIR /app/
RUN apt-get update && apt-get install -y ffmpeg
ENV PATH=$PATH:/app/bin

COPY requirements.txt /app/
COPY ${src} /app/

RUN pip install --upgrade pip \ 
    &&  pip install --requirement requirements.txt
COPY to_mp3.py .

CMD ["python", "to_mp3.py"]