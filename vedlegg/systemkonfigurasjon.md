# Innstallasjonsprossesser
## Docker
Innstallasojnsprossessen er gjennomført på lik måte som beskrevet på [docker sine install-sider per](https://docs.docker.com/engine/install/ubuntu/) 21.04.2022.

Innstallerer dependencies
```shell
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

Legger til dockers GPG nøkkel
```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

Legger til dockers stable repo.
```shell
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  
  (lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

```

Starter innstallasjon av docker
```shell
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## Minikube

Innstallasjon av minikube.
```shell
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64
```

Start av et minikube cluster med docker som driver.
```shell
minikube config set driver docker
minikube start
```

