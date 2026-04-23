# 🚀 Desafio 3 - Primeiro Deploy no Kubernetes

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

## 📋 Sobre o Projeto

Este projeto faz parte do **Desafio 3** da mentoria Kubernetes, demonstrando na prática os conceitos fundamentais de orquestração de containers:

- ✅ Deploy de aplicações no Kubernetes
- ✅ Escalabilidade (Scaling)
- ✅ Auto recuperação (Auto Healing)
- ✅ Exposição de serviços (Service)

## 🎯 Objetivo

Realizar o primeiro deploy de uma aplicação em um cluster Kubernetes, aplicando conceitos essenciais de containerização e orquestração.

## 🛠️ Tecnologias Utilizadas

- **Kubernetes** - Orquestração de containers
- **Docker** - Containerização da aplicação
- **Python 3.9** - Linguagem de programação
- **Flask** - Framework web
- **Minikube** - Cluster Kubernetes local

## 📁 Estrutura do Projeto
```├── app.py # Aplicação Flask "Hello World"
├── Dockerfile # Configuração da imagem Docker
├── requirements.txt # Dependências Python
├── deployment.yaml # Manifesto Kubernetes - Deployment
└── service.yaml # Manifesto Kubernetes - Service


## 🚀 Como Executar

### Pré-requisitos

- Docker instalado
- Kubernetes (Minikube, Kind ou Docker Desktop)
- kubectl configurado

### 1. Build da Imagem Docker

```bash
# Build da imagem
docker build -t roberionascimento300/hello-k8s:v1 .

# Push para o Docker Hub
docker push roberionascimento300/hello-k8s:v1

**🚀 2. Deploy no Kubernetes**
# Criar namespace (se não existir)
kubectl create namespace dev

# Aplicar o deployment
kubectl apply -f deployment.yaml

# Aplicar o service
kubectl apply -f service.yaml

**🚀 3. Verificar o Deploy**

# Verificar deployments
kubectl get deployments -n dev

# Verificar pods
kubectl get pods -n dev

# Verificar services
kubectl get services -n dev

**🚀 4. Acessar a Aplicação**

# Port-forward (recomendado)
kubectl port-forward -n dev service/hello-world-svc 8080:80

# Acessar no navegador
# http://localhost:8080
