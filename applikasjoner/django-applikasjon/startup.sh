#!/bin/sh
A=0
echo " "
echo " "
echo " "
while [ $A -eq 0 ]:
do

if ping -c 1 mysql-service &> /dev/null
then
  echo "Klarte å koble til databasen, starter server."
  echo " "
  python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
else
  echo " "
  echo "Klarer ikke å koble til databasen, prøver igjen om 10 sek"
  sleep 10
fi

done


