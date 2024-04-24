FROM python:alpine
WORKDIR /app
COPY python1.py /app/
COPY paragraphs.txt /app/
RUN pip install --no-cache-dir nltk
RUN python -m nltk.downloader punkt stopwords
CMD ["python","python1.py"]