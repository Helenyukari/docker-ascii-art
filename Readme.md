![Docker CI](https://github.com/Helenyukari/docker-ascii-art/actions/workflows/docker.yml/badge.svg)

#  Docker ASCII Generator

Pequeno projeto para aprender Docker na prática de forma divertida.

Este container gera uma arte ASCII personalizada usando Python e inclui um timestamp na saída.

---

##  Como funciona?

- O Docker cria a imagem a partir do `Dockerfile`
- O container executa o script automaticamente
- Um texto é convertido em ASCII
- Um timestamp é incluído na saída
- Uso de `ENTRYPOINT + argumentos`
- Pipeline automatizado com GitHub Actions (CI)

---

# Rodando localmente

## Clone o repositório

```bash
git clone https://github.com/Helenyukari/docker-ascii-art.git
```
Entre na pasta (se estiver no windows):
```bash
cd docker-ascii-art.git  
```
<!-- Entre na pasta (se estiver no Linux):
```bash
cd `docker-ascii-art.git  
``` -->
 
## Build da Imagen

```bash
docker build -t ascii-app .
```

##Executar o container
```
docker run ascii-app SEU_NOME
```
#### testes - exemplo

Exemplo 0.1:
    Se você executar esse comando abaixo, você tem seu nome somente no seu terminal.
```bash
docker run ascii-app Helen  

   / / / / ____/ /   / ____/ | / /
  / /_/ / __/ / /   / __/ /  |/ /
 / __  / /___/ /___/ /___/ /|  /
/_/ /_/_____/_____/_____/_/ |_/
```
Exemplo 0.2:
    Se você executar esse irá gerar um Output.txt com seu nome salvo.
```bash
python app.py Yukari

 __  __      __              _ 
\ \/ /_  __/ /______ ______(_)
 \  / / / / //_/ __ `/ ___/ / 
 / / /_/ / ,< / /_/ / /  / /  
/_/\__,_/_/|_|\__,_/_/  /_/   
                              
Generated at: 16/02/2026 22:01:54
```