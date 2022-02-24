# Info

Før django-applikasjonen legges til i Kubernetes må ip-adressen til mysql-servicen legges inn i django sin deploymentfil.

```
get svc -o wide
```

Finn IP-adressen til mysql-servicen og noter den ned. Denne IP-adressen må legges inn i filen django-deployment.yaml

Så skal yaml-filene legges til i kubernetes:

```
kubectl apply -f django-service.yaml -f django-deployment.yaml
```



