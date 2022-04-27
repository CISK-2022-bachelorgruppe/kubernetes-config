# Hvordan gjennomføre Test 3:

Pre-instal:
- Docker

## 1. Start minikube med denne kommandoen:
```
minikube start --driver docker --extra-config=kubelet.housekeeping-interval=10s
```
## 2. Start den innebygde tilleggsfunksjonen 'metrics-server' i minikube:
```
minikube addons enable metrics-server
kubectl top pods -n kube-system             #  Viser om metric-server gir detaljer til pods om CPU og minne 
```
## 3. Deployer php-apache.yaml
```
kubectl apply -f php-apache.yaml
```
## 4. Lag den horisontalepodautoskalereren og sjekk current status:
```
kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10
kubectl get hpa
```
## 5. Generer en last med busybox i et nytt terminalvindu:
```
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"
```
## 6. Overvåk HPA i den første terminalvinduet:
```
kubectl get hpa php-apache -watch
```
## 7. Stopp busybox:
```
<ctr> + c
```
## 8. Overvåk HPA og se den skalere ned:
```
kubectl get hpa php-apache -watch  #Når hpa detekterer at cpu=0% skalerer den automatisk ned til 1 replika. Dette kan ta noen minutter.
```

