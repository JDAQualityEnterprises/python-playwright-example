FROM mcr.microsoft.com/playwright/python:v1.51.0-noble
WORKDIR /app
COPY models/ /app/models
COPY pages/ /app/pages
COPY contacts_test.py /app/
COPY main_test.py /app/
COPY pytest.ini /app/
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt
#&& pytest -v --html=pwreport.html
CMD ["pytest", "-v", "--html=pwreport.html"]
#CMD [ "tail", "-f", "/dev/null" ]