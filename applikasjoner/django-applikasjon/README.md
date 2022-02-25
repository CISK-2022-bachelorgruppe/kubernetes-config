# Setup for django-applikasjon

For at applikasjonen skal fungere må en database være satt opp først.
Inne i databasen-konteineren må det også lages en database kalt "bachelor_db"

Bruk minikube sin docker for å lagre imaget i minikube noden
```shell
eval $(minikube docker-env)
```

cd til mappen Dockerfile ligger i
```shell
cd ...../k8s-bachelor/applikasjoner/django-applikasjon
```

Bygg applikasjonen med minikube sin docker.
```shell
docker build -t django-applikasjon .
```