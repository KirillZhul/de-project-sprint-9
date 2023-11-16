### Обновление данных Redis

#### Загрузка пользователей

~~~
curl -X POST https://redis-data-service.sprint9.tgcloudenv.ru/load_users -H "Content-Type: application/json; charset=utf-8" -d "{\"redis\":{\"host\":\"rc1b-du2g6vviq7p201kn.mdb.yandexcloud.net\",\"port\":\"6380\",\"password\":\"2aPnimE6P9akzdg\"}}"
~~~

![изображение](https://github.com/KirillZhul/de-project-sprint-9/assets/118897479/be5cb8ac-4fb2-4203-9fa7-cd6d18517c84)


#### Загрузка ресторанов

~~~
curl -X POST https://redis-data-service.sprint9.tgcloudenv.ru/load_restaurants -H "Content-Type: application/json; charset=utf-8" -d "{\"redis\":{\"host\":\"rc1b-du2g6vviq7p201kn.mdb.yandexcloud.net\",\"port\":\"6380\",\"password\":\"2aPnimE6P9akzdg\"}}"
~~~

![изображение](https://github.com/KirillZhul/de-project-sprint-9/assets/118897479/6cf0a90d-838e-4be5-a60e-733fa98d91de)


