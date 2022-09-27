Esse projeto tem como objetivo o desenvolvimento de ferramentas que possam ser utilizadas com a API REST do serviço Motomo Web Analytics para facilitar determinadas tarefas.
Nessa imagem contém um script para criação e configuração de sites em massa dentro do Matomo.

## Requerimentos ##

Ao executar os comandos abaixo o script busca pelo arquivo siteslist.list no diretório /tmp.
Esse arquivo deve conter a lista de sites que serão configurados no Matomo.

## Steps ##

1. O comando abaixo cria uma imagem docker contendo o script:

```
docker image build -t local/matomo-tools:1.0 -f Dockerfile . 
```

2. O comando abaixo executa o script montando a partição /tmp dentro do contêiner.
 
```
docker container run -d -ti --volume /tmp:/tmp local/matomo-tools:1.0 python addsite2piwik.py 
```
