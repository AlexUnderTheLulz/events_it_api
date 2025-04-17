# events_it_api

API событий в сфере ИТ предоставляет доступ к списку мероприятий, связанных с ИТ, полученных с сайта https://it-event-hub.ru/. API построен на Flask и возвращает данные о событиях в формате JSON, включая название, дату, теги и ссылки на страницы мероприятий.

### Базовый URL

```text
https://<ваш-домен-сервера>/
```
(В моём случае - https://functions.yandexcloud.net/ , так как развёртывал именно на Yandex Cloud)

### Ответ
* Код состояния: 200 OK
* Тип содержимого: application/json
* Тело ответа:
```json
[
  {
    "link": "https://it-event-hub.ru/event/<event-id>",
    "eventName": "Название события",
    "eventDatetime": "ДД.ММ.ГГГГ ЧЧ:ММ",
    "eventsTags": ["Тег1", "Тег2", ...],
    "imageUrl": "Ссылка на обложку мероприятия",
    "city": "Название города, где проходит мероприятие"
  },
  ...
]
```

### Поля ответа

| Название      | Тип данных   | Описание                                            |
|---------------|--------------|-----------------------------------------------------|
| EventsModel   | List<Events> | Список всех мероприятий                             |
| link	        | String       | Ссылка, ведущая на страницу мероприятия             |
| eventName     | String       | Название мероприятия                                |
| eventDatetime | String       | Дата и время проведения мероприятия                 |
| eventTags	    | List<String> | Теги мероприятия                                    |
| imageUrl	    | String       | "Обложка" мероприятия                               |
| city    	    | String       | Город, где проходит мероприятие                     |


### Пример ответа


```json
[
  {
    "link": "https://it-event-hub.ru/events/ai-butkemp-ot-redmadrobot-2025-03-17",
    "eventName": "AI-буткемп от red_mad_robot",
    "eventDatetime": "17 марта — 17 апреля ",
    "eventsTags": [
      "Backend",
      "ML",
      "AI",
      "QA"
    ],
    "imageUrl": "https://api.it-event-hub.ru/uploads/images/2025/3/ai-butkemp-ot-redmadrobot-2025-03-17-preview.webp",
    "city": ""
  },
  {
    "link": "https://it-event-hub.ru/events/avito-ml-cup-2025-personalnye-rekomendacii-2025-03-31",
    "eventName": "Avito ML cup 2025| Персональные рекомендации",
    "eventDatetime": "31 марта — 28 мая ",
    "eventsTags": [
      "ML"
    ],
    "imageUrl": "https://api.it-event-hub.ru/uploads/images/2025/3/avito-ml-cup-2025-personalnye-rekomendacii-2025-03-31-preview.webp",
    "city": ""
  }
]
```

### Зависимости

API использует следующие Python-библиотеки:

* Flask: веб-фреймворк для обработки HTTP-запросов
* BeautifulSoup4: для парсинга HTML и веб-скрейпинга
* Requests: для выполнения HTTP-запросов к целевому сайту
