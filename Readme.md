###Настройка образов:
```
image: 127.0.0.1:5000/swarm-app
```

###Настройка количества реплик
```
deploy:
    mode: replicated
    replicas: 4
```

###Инициализация Swarm
```
swarm init 
```

##Реестр
###Инициализация локального реестра, в котором будут храниться образы
```
	docker service create --name test_swarm-registry --publish published=10000,target=5000 registry:2 
```
###Отправление приложения в реестр
```
	docker-compose push
```

###Создание приложения
```
docker stack deploy --compose-file docker-compose.yml swarm-app
```
