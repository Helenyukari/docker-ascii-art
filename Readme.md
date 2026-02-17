![Docker CI](https://github.com/Helenyukari/docker-ascii-art/actions/workflows/docker.yml/badge.svg)


#  Docker ASCII Generator

Pequeno projeto para aprender Docker na prática de forma divertida.

Este container gera uma arte ASCII personalizada usando Python e inclui um timestamp na saída.

---

## Como funciona?

-  O Docker cria a imagem
-  O container executa o script
-  Um texto é convertido em ASCII
-  Um timestamp é incluído na saída
-  Conceito de ENTRYPOINT + argumentos
- Pipeline automatizado com GitHub Actions
---

##  Rodando localmente

### Build da imagem

```bash
docker build -t ascii-app .

docker run ascii-app SEU_NOME
```
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
    Se você executar esse irá gerar um .txt com seu nome salvo.
```bash
python app.py Yukari

 __  __      __              _ 
\ \/ /_  __/ /______ ______(_)
 \  / / / / //_/ __ `/ ___/ / 
 / / /_/ / ,< / /_/ / /  / /  
/_/\__,_/_/|_|\__,_/_/  /_/   
                              
Generated at: 16/02/2026 22:01:54
```