# VI-UM-CURSO


## Descrição 
O Projeto trata-se de um Python bot para twitter. Sua função é ajudar
toda a comunidade dev ao fazer retweets de cursos e bootcamps gratis.


## Funcionalidades
O bot tem as funções de procurar palavras chave, curtir e retweetar.
Para isso ele acessa a API do twitter atravez da extensão tweepy.

## Instalação e execução
#### 1º Crie uma conta para o bot
Crie uma conta de desenvolvedor do twitter com a função read and write.

#### 2º Dependencias
Primeiro clone o repositório, depois instale as depêndencias que estão no arquivo 
requirements.txt com o pip. Com o seguinte comando:
```
pip install -r requirements.txt
```
#### 3ºAutenticação
Crie um ariquivo ".env" com as keys da sua conta do twitter e as configurações do bot:
```
consumer_key = 'sua consumer key'
consumer_secret = 'seu consumer secret'
access_token = 'seu acess token'
access_token_secret = 'seu acess token secret'
QUERY = palavra chave
LIKE = Verdadeiro
SLEEP_TIME = 300
UserIdViUmCurso = ID da sua conta
```
## Formas de execução
O bot está hospedado no https://www.heroku.com/ conectado diretamente com o 
github, mas tambem pode ser hospedado e executado por container ou localmente.
Use o comando:
```
python main.py
```

## Created by
| [<img src="https://avatars.githubusercontent.com/u/94025010?v=4" width=115><br><sub>Christopher Mickelle</sub>](https://github.com/cmickelle) | [<img src="https://avatars.githubusercontent.com/u/31418573?v=4" width=115><br><sub>João Vitorino</sub>](https://github.com/jvitorinoj) |
|:---------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------:|


https://github.com/cmickelle/

https://github.com/jvitorinoj/
