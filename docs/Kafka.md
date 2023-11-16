### Подготовка данных Kafka

#### Создание топика для приема от системы-источника

~~~
docker run -it --network=host -v "$HOME\.kafka\YandexInternalRootCA.crt:/data/CA.pem"  edenhill/kcat:1.7.1 -b rc1a-lskm6vbum7l8ir2d.mdb.yandexcloud.net:9091 -X security.protocol=SASL_SSL -X sasl.mechanisms=SCRAM-SHA-512 -X sasl.username="producer_consumer" -X sasl.password="producer_consumer" -X ssl.ca.location=/data/CA.pem -L
~~~

![изображение](https://github.com/KirillZhul/de-project-sprint-9/assets/118897479/1aee68e6-c430-4385-94ac-c589003ba18c)


#### Перевод kcat в режим консьюмера

~~~
docker run -it --name "kcat" --network=host --rm -v "$HOME\.kafka\YandexInternalRootCA.crt:/data/CA.pem" edenhill/kcat:1.7.1 -b rc1a-lskm6vbum7l8ir2d.mdb.yandexcloud.net:9091 -X security.protocol=SASL_SSL -X sasl.mechanisms=SCRAM-SHA-512 -X sasl.username="producer_consumer" -X sasl.password="producer_consumer" -X ssl.ca.location=/data/CA.pem -t order-service_orders -C -o beginning
~~~

![изображение](https://github.com/KirillZhul/de-project-sprint-9/assets/118897479/2d27a82e-2924-47be-a2f5-be01172455a0)


#### Регистрация созданного топика

~~~
curl -X POST https://order-gen-service.sprint9.tgcloudenv.ru/register_kafka -H "Content-Type: application/json; charset=utf-8" -d "{\"student\": \"kirillzhul\",\"kafka_connect\":{\"host\": \"rc1a-lskm6vbum7l8ir2d.mdb.yandexcloud.net\",\"port\": 9091,\"topic\":\"order-service_orders\",\"producer_name\":\"producer_consumer\",\"producer_password\":\"producer_consumer\"}}"
~~~

![изображение](https://github.com/KirillZhul/de-project-sprint-9/assets/118897479/722ebdad-2ed7-4cb6-a864-ba938b1d3e13)


#### Проверка корректности работы кластера

~~~
curl -X POST https://order-gen-service.sprint9.tgcloudenv.ru/test_kafka -H "Content-Type: application/json; charset=utf-8" -d "{\"student\": \"kirillzhul\",\"kafka_connect\":{\"host\": \"rc1a-lskm6vbum7l8ir2d.mdb.yandexcloud.net\",\"port\": 9091,\"topic\":\"order-service_orders\",\"producer_name\":\"producer_consumer\",\"producer_password\":\"producer_consumer\"}}"
~~~

![изображение](https://github.com/KirillZhul/de-project-sprint-9/assets/118897479/6b1579df-2d0d-4816-81ec-f664dfcafcee)

![изображение](https://github.com/KirillZhul/de-project-sprint-9/assets/118897479/9d1cfd83-26e2-49ec-8d08-17d0ab0e62e6)



#### Отмена регистрации созданного топика (остановка потока Kafka)

~~~
curl -X POST https://order-gen-service.sprint9.tgcloudenv.ru/delete_kafka -H "Content-Type: application/json; charset=utf-8" -d "{\"student\": \"kirillzhul\"}"
~~~






