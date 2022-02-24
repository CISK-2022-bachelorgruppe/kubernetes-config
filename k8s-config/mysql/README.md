# Info
Alle disse filene må legges inn i kubernetes, utenom "mysql-service-ClusterIP.yaml"
```
kubectl apply -f mysql-configMap.yaml -f mysql-pv.yaml -f mysql-pvc.yaml -f mysql-secret.yaml -f mysql-service.yaml -f mysql-statefulset.yaml
```