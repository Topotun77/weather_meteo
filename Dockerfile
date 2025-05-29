FROM python:3.12

RUN mkdir /meteo_wt

WORKDIR /meteo_wt

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x *.sh