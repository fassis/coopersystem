# coopersystem

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