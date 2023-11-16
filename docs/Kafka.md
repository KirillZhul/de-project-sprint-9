### Подготовка данных Kafka

## Регистрация созданного топика
~~~
curl -X POST https://order-gen-service.sprint9.tgcloudenv.ru/register_kafka -H "Content-Type: application/json; charset=utf-8" -d "{\"student\": \"kirillzhul\",\"kafka_connect\":{\"host\": \"rc1a-lskm6vbum7l8ir2d.mdb.yandexcloud.net\",\"port\": 9091,\"topic\":\"order-service_orders\",\"producer_name\":\"producer_consumer\",\"producer_password\":\"producer_consumer\"}}"
~~~


