#!/bin/sh
A=0
echo " "
echo " "
echo " "
while [ $A -eq 0 ]:
do
nc -vz mysql-service 3306
if [ $? -eq 0 ];
then
  echo "Klarte å koble til databasen, starter server."
  echo " "
  python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
  sleep 10
else
  echo " "
  echo "Klarer ikke å koble til databasen, prøver igjen om 10 sek"
  sleep 10
fi

done


