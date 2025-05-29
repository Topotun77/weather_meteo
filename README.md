# Прогноз погоды через API https://open-meteo.com/

Web-приложение, которое позволяет пользователю вводить название города, 
и получать прогноз погоды в этом городе на ближайшее время.  
Приложение написано с использованием фреймворка `Django`.

## В приложении реализовано:

• Ввод пользователем названия города. Определение координат по названию города.   
• Вывод прогноза погоды для заданного города с помощью API https://open-meteo.com/.  
  
## Дополнительно реализовано (по списку):
• Написано несколько тестов для приложения `meteo_app`.  
• Приложение помещено в Docker-контейнер.  
• Сделано автодополнение (подсказки) при вводе города. Реализовано через запрос от фронтенда к базе данных, 
читается таблица ранее использованных городов, бэкенд формирует список значений и передает
в фронтенд, где этот список используется при вводе символов в поле ввода города.  
• При повторном посещении сайта будет предложено посмотреть погоду в городе, в котором пользователь уже смотрел ранее.  
• Сохранение истории поиска для каждого пользователя в БД `PostgreSQL`.  
• Создано API приложение `stat_api_app`, показывающее сколько раз вводили какой город. 
Результат доступен по относительной ссылке: `/api/stat_api_app/stats/`. 
Статистика формируется в процессе обращения пользователей и ведется в отдельной таблице БД `PostgreSQL`.

## Дополнительно реализовано (сверх списка):

• Регистрация / вход / выход пользователей.  
• Сохранение пользовательских предпочтений в БД `PostgreSQL`:
светлая / темная тема интерфейса, последний введенный город.  
• Вывод статистики по пользователям. Доступ к данной странице имеет только суперпользователь.  


### Скриншот домашней страницы
![img01](https://github.com/Topotun77/weather_meteo/blob/master/ScreenShots/001.JPG?raw=true)
### Скриншот страницы регистрации пользователя
![img02](https://github.com/Topotun77/weather_meteo/blob/master/ScreenShots/002.JPG?raw=true)
### Логин пользователя в системе
![img03](https://github.com/Topotun77/weather_meteo/blob/master/ScreenShots/003.JPG?raw=true)
### Страница выбора города
![img04](https://github.com/Topotun77/weather_meteo/blob/master/ScreenShots/004.JPG?raw=true)
### Результат обработки запроса - для выбранного города выводится погода по часам и по дням
![img05](https://github.com/Topotun77/weather_meteo/blob/master/ScreenShots/005.JPG?raw=true)
### Подсказки при вводе города
![img07](https://github.com/Topotun77/weather_meteo/blob/master/ScreenShots/007.JPG?raw=true)
### При возникновении ошибки в запросе, пользователю выводится соответствующее сообщение об ошибке
![img06](https://github.com/Topotun77/weather_meteo/blob/master/ScreenShots/006.JPG?raw=true)
### Статистика по запросам пользователей 
Доступна только суперпользователям  
![img10](https://github.com/Topotun77/weather_meteo/blob/master/ScreenShots/010.JPG?raw=true)
### API приложение `stat_api_app` 
показывает сколько раз вводили какой городй 
![img30](https://github.com/Topotun77/weather_meteo/blob/master/ScreenShots/030.JPG?raw=true)
### Интерфейс в темной теме
![img20](https://github.com/Topotun77/weather_meteo/blob/master/ScreenShots/020.JPG?raw=true)

## Для запуска:
1. Выполните команду для клонирования:  
```
git clone https://github.com/Topotun77/weather_meteo
```
2. Установите все необходимые зависимости, выполнив команду:  
```
pip install -r requirements.txt
```
3. В беде данных `PostgreSQL` создайте базу `meteo_db`.  

4. Перейдите в каталог приложения, создайте суперпользователя, 
произведите все необходимые миграции:  
```
cd .\meteo_wt\

python manage.py createsuperuser

python manage.py makemigrations

python manage.py migrate
```
5. Для локального запуска:  
- перейдите в каталог `meteo_wt`, команда:  
```
cd .\meteo_wt\
```  
- запустите код с помощью команды:  
```
python manage.py runserver
```  
6. Для запуска на сервере используйте команду:  
```
cd meteo_wt && gunicorn meteo_wt.wsgi:application  --bind 0.0.0.0:80
```
7. Либо запустить приложение вместе с базой данных PostgreSQL через Dockerfile и docker-compose .
