# Info

Django-applikasjonen trenger ikke ip-adressen til mysql-databasen fordi service-navnet til databasen blir benyttet!

```
kubectl apply -f django-service.yaml -f django-deployment.yaml
```



