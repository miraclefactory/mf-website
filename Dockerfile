FROM python
WORKDIR /application
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["sh", "run.sh"]
