# Портал групи — Архітектура Django проєкту

[ПОСИЛАННЯ НА ПРЕЗЕНТАЦІЮ М5У1](https://docs.google.com/presentation/d/1fuIGiBZkXGveitLcBIB1I_Yfk6lMfJcrqMsPOjGHVT0/edit?slide=id.g3cfcb7429d2_0_0#slide=id.g3cfcb7429d2_0_0)

[ПОСИЛАННЯ НА ПРЕЗЕНТАЦІЮ М5У2](https://docs.google.com/presentation/d/17iazji_485xHjNA_VVf25H6Is5hbWnYV/edit?slide=id.p1#slide=id.p1)

[ПОСИЛАННЯ НА ПРЕЗЕНТАЦІЮ М5У5](https://docs.google.com/presentation/d/1qJtaAZvXn4VogssObAjOmdnybYoKyCZ75bHLxgPA4Wc/edit?slide=id.g3c6a2d16174_0_0#slide=id.g3c6a2d16174_0_0)


### [Приклад хорошого файлу REDME.md](https://github.com/OlhaTryhub/cafe-web-site/blob/main/README.md)


---

## Зміст

- [Core — головна сторінка порталу](#core)
- [Users — користувачі та автентифікація](#users)
- [Forum — форум](#forum)
- [Grades — електронний щоденник](#grades)
- [Events — події](#events)
- [Calendar — календар подій](#calendar)
- [Polls — система опитувань](#polls)
- [Voting — система голосувань](#voting)
- [Announcements — оголошення](#announcements)
- [Materials — навчальні матеріали](#materials)
- [Media Portal — портфоліо та галерея](#media-portal)
- [Навігація сайту](#navigation)
- [Технології](#технології)
- [Робота в команді](#робота-в-команді)
- [Очікуваний результат](#очікуваний-результат)

---

## Опис проєкту

**Портал групи** — це веб-додаток, створений на фреймворку **Django**, який дозволяє студентам та викладачам взаємодіяти через єдину систему.

На порталі буде розміщено:

* інформацію про групу
* форум для спілкування
* електронний щоденник з оцінками
* календар подій
* систему опитувань
* систему голосувань
* оголошення
* навчальні матеріали
* портфоліо студентів
* галерею фото та відео

Проєкт реалізується у вигляді **Django-порталу, розділеного на окремі додатки (apps)**.
Кожен додаток відповідає за окрему функціональність системи.

Студенти можуть **обрати один із модулів та реалізувати його**.

---

# Архітектура проєкту

Проєкт буде складатися з **11 Django додатків (apps)**.

```
portal_project
│
├── core
├── users
├── forum
├── grades
├── events
├── calendar_app
├── polls
├── voting
├── announcements
├── materials
└── media_portal
```

---


---

<h2 id="core">1. Core — головна сторінка порталу</h2>

### Сторінка

Головна сторінка сайту з інформацією про групу та віджетами інших розділів.

### Функціонал

* Відображення інформації про групу
* Віджети інших модулів (новини, події, оголошення)
* Навігація по сайту

### Моделі

**GroupInfo**

* title
* description
* created_at
* updated_at

**Widget**

* name
* type (events / announcements / forum / polls)
* is_active
* order

---

<h2 id="users">2. Users — користувачі та автентифікація</h2>

### Сторінки

* Реєстрація
* Авторизація
* Профіль користувача
* Редагування профілю

### Ролі користувачів

* User (звичайний користувач)
* Moderator (модератор)
* Admin (адміністратор)

### Моделі

**User**

* username
* email
* password
* first_name
* last_name
* role
* avatar
* created_at

**Profile**

* user (FK → User)
* phone
* birthday
* bio

---

<h2 id="forum">3. Forum — форум</h2>

### Сторінки

* Список категорій
* Список тем
* Сторінка теми
* Створення повідомлення

### Функціонал

* Користувачі можуть створювати повідомлення
* Модератори та адміністратори можуть створювати та редагувати теми

### Моделі

**ForumCategory**

* name
* description

**ForumTopic**

* title
* author (FK → User)
* category (FK → ForumCategory)
* created_at

**ForumPost**

* topic (FK → ForumTopic)
* author (FK → User)
* content
* created_at

---

<h2 id="grades">4. Grades — електронний щоденник</h2>

### Сторінки

* Таблиця оцінок
* Список предметів
* Редагування оцінок (адмін)

### Моделі

**Subject**

* name
* description

**Grade**

* student (FK → User)
* subject (FK → Subject)
* grade
* date
* comment
* created_by (FK → User)

---

<h2 id="events">5. Events — події</h2>

### Сторінки

* Список подій
* Сторінка події
* Створення / редагування події

### Моделі

**Event**

* title
* description
* location
* start_date
* end_date
* created_by (FK → User)
* created_at

---

<h2 id="calendar">6. Calendar — календар подій</h2>

### Сторінки

* Календар
* Перегляд подій за датою

### Моделі

**CalendarDay**

* date
* notes

**CalendarEvent**

* event (FK → Event)
* date

---

<h2 id="polls">7. Polls — система опитувань</h2>

### Сторінки

* Список опитувань
* Проходження опитування
* Результати опитування

### Функціонал

* Багатосторінкові опитування
* Користувач може пройти опитування один раз
* Адміністратори можуть переглядати результати

### Моделі

**Poll**

* title
* description
* created_by
* created_at
* is_active

**Question**

* poll (FK → Poll)
* text
* order

**Choice**

* question (FK → Question)
* text

**PollResponse**

* poll (FK → Poll)
* user (FK → User)
* submitted_at

**Answer**

* response (FK → PollResponse)
* question (FK → Question)
* choice (FK → Choice)

---

<h2 id="voting">8. Voting — система голосувань</h2>

### Сторінки

* Список голосувань
* Сторінка голосування
* Результати голосування

### Моделі

**Vote**

* title
* description
* created_by
* end_date

**VoteOption**

* vote (FK → Vote)
* text

**UserVote**

* vote (FK → Vote)
* user (FK → User)
* option (FK → VoteOption)
* voted_at

---

<h2 id="announcements">9. Announcements — оголошення</h2>

### Сторінки

* Список оголошень
* Сторінка оголошення

### Моделі

**Announcement**

* title
* content
* author (FK → User)
* created_at
* updated_at
* is_active

---

<h2 id="materials">10. Materials — навчальні матеріали</h2>

### Сторінки

* Список матеріалів
* Сторінка матеріалу
* Завантаження матеріалу

### Функціонал

* Підтримка файлів, зображень, посилань та відео з YouTube

### Моделі

**Material**

* title
* description
* file
* link
* youtube_url
* material_type (file / link / video)
* uploaded_by (FK → User)
* created_at

---

<h2 id="media-portal">11. Media Portal — портфоліо та галерея</h2>

### Сторінки

* Портфоліо студентів
* Список проектів
* Галерея фото та відео

### Моделі

**Portfolio**

* title
* description
* author (FK → User)
* link
* created_at

**PortfolioFile**

* portfolio (FK → Portfolio)
* file
* screenshot

**GalleryItem**

* title
* file
* type (image / video)
* uploaded_by (FK → User)
* is_approved
* created_at

---

<h2 id="navigation">Навігація сайту</h2>

```
Головна
│
├── Форум
├── Електронний щоденник
├── Події
├── Календар
├── Опитування
├── Голосування
├── Оголошення
├── Матеріали
├── Портфоліо
├── Галерея
└── Профіль користувача
```

---

# Технології

Проєкт використовує:

* **Python**
* **Django**
* **HTML**
* **CSS**
* **Bootstrap**
* **Git**

---

# Робота в команді

Проєкт виконується командою студентів.

Кожен студент або група студентів:

* обирає **один модуль (app)**
* реалізує **моделі**
* створює **views**
* створює **HTML шаблони**
* підключає **URLs**

Весь код зберігається у **Git репозиторії**.

---

# Очікуваний результат

Після завершення проєкту повинен бути створений **повноцінний портал студентської групи**, де користувачі можуть:

* спілкуватися на форумі
* переглядати оцінки
* брати участь в опитуваннях
* голосувати
* переглядати матеріали
* публікувати свої проєкти
* переглядати фото та відео

---
