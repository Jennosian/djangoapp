# start from an official image
FROM python:3

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

#Install FreeTDS and dependencies for PyODBC
RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install unixodbc-dev -y \
 && apt-get install freetds-dev -y \
 && apt-get install freetds-bin -y \
 && apt-get install tdsodbc -y \
 && apt-get install --reinstall build-essential -y

# populate "ocbcinst.ini"
RUN echo "[FreeTDS]\n\
TDS_Version = '7.4'\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini

# modify "freetds.conf"
RUN echo "[mssql]\n\
host = '172.30.2.18'\n\
tds version = 7.4\n\
port = 1433" >> /etc/freetds/freetds.conf

# 172.30.2.18

# V6ibolla pole vaja
RUN echo MinProtocol = TLSv1.0 >> /etc/ssl/openssl.cnf
RUN echo CipherString = DEFAULT@SECLEVEL=1 >> /etc/ssl/openssl.cnf

# install our two dependencies!!!!!!!!!!!!
# RUN pip install gunicorn django django-pyodbc-azure

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY Pipfile Pipfile.lock /opt/services/djangoapp/src/
RUN pip install pipenv && pipenv install --system

# copy our project code
COPY . /opt/services/djangoapp/src

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "acqmonitoring", "--bind", ":8000", "config.wsgi:application"]