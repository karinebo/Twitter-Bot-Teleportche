# Twitter Bot - Teleportche

Bot no Twitter para responder (@yourappname) de acordo com o sentimento identificado no Tweet, estamos considerando apenas Positivo e Negativo. Além do sentimento, também a probabilidade da resposta.

### Step 1: Instalar dependências

Será necessário instalar as seguintes dependências no seu ambiente de desenvolvimento:

  Linguagem de programação utilizada: [Python](https://www.python.org/downloads/)

  Biblioteca de comunicação com o Twitter: [Tweepy](http://www.tweepy.org/)

  Biblioteca para treinamento do modelo de predição: [FastText](https://pypi.org/project/fasttext/)

### Step 2: Fazer o download do conjunto de dados para treinamento:

Reviews de clientes da amazon:

  [Amazon Reviews for Sentiment Analysis:](https://www.kaggle.com/bittlingmayer/amazonreviews)

  Descompactar os arquivos, que deverão ficar na pasta "./amazonreviews" dentro da pasta do projeto.

### Step 3: Criar uma aplicação no Twitter:

Para criar uma aplicação, é necessário estar logado com uma conta no Twitter.
https://apps.twitter.com/app/new

Observação:
Name: Será o nome da aplicação (@yourappname) que o bot irá monitorar e responder
Website: Se você não tiver um website, pode ser utilizado http://127.0.0.1

### Step 4: Clonar este repositório

Após clonar este repositório, as informações do arquivo secrets.py devem ser substituídas pelas chaves e tokens da sua aplicação no Twitter.

### Step 5: Executar

Excecute o script twitterBot.py com a linha de comando abaixo dentro da pasta do projeto:
(Isso funciona para mac e linux, não sei como é no Windows)

```
$ python twitterBot.py
```
O bot irá responder aos tweets apenas enquanto o scripts estiver executando.
