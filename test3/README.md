# Hvordan gjennomføre Test 3 - HorizontalPodAutoscaling (HPA):

Denne testen er basert på https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
For at man skal kunne gjengi testen 100% må hpa-php-apache.yamel og php-apache.yaml eksikveres og ikke kommandolinjene som inneholder 'kubectl apply -f https://......'

### Pre-install:
- Docker
## 1. Start minikube med denne kommandoen:
```
$ minikube start --driver docker --extra-config=kubelet.housekeeping-interval=10s
```
For at metrics-server skal fungere må `--extra-config=kubelet.housekeeping-interval=10s` være med under oppstart av minikube
## 2. Start den innebygde tilleggsfunksjonen 'metrics-server' i minikube:
```
$ minikube addons enable metrics-server
```
Se om metrics-server fungerer:
```
$ kubectl top pods -n kube-system            
```
## 3. Deployer php-apache.yaml
```
$ kubectl apply -f php-apache.yaml
```
## 4. Lag den horisontalepodautoskalereren og sjekk current status:
```
$ kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10
```
Sjekk status til HPA:
```
$ kubectl get hpa
```
Dette kan ta ett minutt eller to før den registreres.
### 4.1 andre muligheter for HPA:
```
$ kubectl apply -f hpa-php-apache.yaml
```
Denne filen gjør akkurat det samme som kommandoen over.

## 5. Generer en last med busybox i et nytt terminalvindu:
```
$ kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"
```
## 6. Overvåk HPA i den første terminalvinduet:
```
$ kubectl get hpa php-apache --watch
```
## 7. Stopp busybox:
```
$ <ctr> + c
```
## 8. Overvåk HPA og se den skalere ned:
```
$ kubectl get hpa php-apache --watch  
```
Når HPA detekterer at CPU=0% skalerer den automatisk ned til 1 replika. Dette kan ta noen minutter.
