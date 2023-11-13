# Проект 9-го спринта

### Описание
Репозиторий предназначен для сдачи проекта 9-го спринта по облачным технологиям (с использованием сервисов Yandex Cloud).

### Структура репозитория
- `pics` - здесь лежит единственная фотография для ридми.
- `ddl` - здесь DDL всех таблиц слоёв данных PostgreSQL.
- `documentation` - описание команд, сопровождающих функциональность Kafka и Redis.
- `solution` - здесь реализация полной архитектуры решения. 

## Задача
Бизнес-задача — реализация анализа транзакционной активности пользователей ресторана по завершённым заказам.

### Описание задачи
![image](pics/1.png)

В этом проекте будут реализованы все сервисы которые заполняют слои данных PostgreSQL, и визуализированы данные из витрины в дашборде (в Data Lens).

Полная архитектура решения выглядит так:
![image](pics/2.png)

### Исопользуемые инструменты

- Yandex Cloud;
  
- Docker;
  
- Kubernetes;
  
- Apache Kafka;
  
- Redis;
  
- Python;

- SQL;
  
- PostgreSQL.
