FROM python

WORKDIR /app

COPY requirements.txt .

RUN /usr/local/bin/python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["sh", "./start.sh"]

#CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
#CMD ["gunicorn", "iron_work.wsgi:application", "-b", "0.0.0.0:80", "-w", "3", "--reload"]