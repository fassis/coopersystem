## Coopersystem Teste Técnico
## Gestão de Produtos e Pedidos usando Django/RestFramework

## Requisitos
1. Django >= 3.2
2. Python >= 3.8
3. PostgresSQL >= 9.4

## Deploy com Docker
0. Tenha o Docker plenamente instalado e configurado

1. Clone o repositório e abra a pasta coopersystem.
```console
git clone https://github.com/fassis/coopersystem.git coopersystem
cd coopersystem
```

2. Rode o comando do docker-composer
```console
docker-compose up -d
```
3. Rode o comando do docker-composer para criar o superusuario
```console
docker-compose exec web python manage.py createsuperuser
```

4. Acesse a aplicação na porta 8000. 
```console
http://localhost:8000
```

Obs: As informações e conteúdos desta aplicação são apenas para fins de demonstrações técnicas.
Portanto não dispõe de dados sensíveis de terceiros.

## Deploy sem Docker

0. Tenha o Postgres plenamente instalado e configurado

1. Clone o repositório e abra a pasta coopersystem.
```console
git clone https://github.com/fassis/coopersystem.git coopersystem
cd coopersystem
```

2. Rode o comando
```console
python -m venv venv
```

3. Rode o comando
```console
.\venv\Scrips\activate
```

4. No ambiente virtual, rode o comando
```console
pip install -r requirements.txt
```

5. Rode o comando
```console
python manage.py makemigrations
```

6. Rode o comando
```console
python manage.py migrate
```

7. Rode o comando
```console
python manage.py createsuperuser
```

8. Rode o comando
```console
python manage.py runserver
```

9. Acesse a aplicação na porta 8000. 
```console
http://localhost:8000
```