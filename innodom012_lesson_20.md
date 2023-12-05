<!-- TOC -->
* [**Table relations, JOINS**](#table-relations-joins-)
* [**Table relations**](#table-relations-)
* [**One-to-One**](#one-to-one-)
* [**One-to-Many**](#one-to-many-)
* [**Many-to-Many**](#many-to-many-)
* [**Insert\delete forgotten columns**](#insertdelete-forgotten-columns-)
* [**SQL JOIN**](#sql-join)
* [**Types of JOINs and their Mechanics**](#types-of-joins-and-their-mechanics-)
      * [**INNER JOIN**](#inner-join-)
      * [**LEFT JOIN (или LEFT OUTER JOIN)**](#left-join-или-left-outer-join-)
      * [**RIGHT JOIN (или RIGHT OUTER JOIN)**](#right-join-или-right-outer-join-)
      * [**FULL OUTER JOIN**](#full-outer-join-)
      * [**CROSS JOIN**](#cross-join-)
* [**Nested queries**](#nested-queries-)
* [**Soft delete**](#soft-delete-)
* [**DATABASE DUMPS**](#database-dumps-)
<!-- TOC -->

# **Table relations, JOINS**                                                    

# **Table relations**                                                    

В ранних системах управления базами данных (**СУБД**) данные часто хранились в                                                     
больших, нормализованных таблицах. Это приводило к проблемам избыточности                                                     
(повторения одних и тех же данных в разных строках) и сложности                                                    
обновления данных.                                                    


Реляционные базы данных, впервые представленные Эдгаром Коддом в 1970-х годах,                                                    
привнесли концепцию разделения данных на отдельные, связанные таблицы.                                                     
Это позволило более эффективно организовывать данные и уменьшить избыточность.                                                    

Тут у нас появляются такие страшные слова, как **нормализация** и **Отношения таблиц**                                                    

**Нормализация** — это процесс проектирования структуры базы данных для минимизации                                                     
избыточности и зависимостей. Она включает в себя **разделение** **больших таблиц** на                                                    
**более мелкие** и **связанные**, что упрощает **обновление**, **вставку** и **удаление данных**.                                                    


**Отношения таблиц в базах данных** — это способы, которыми таблицы                                                     
связываются друг с другом. Эти отношения позволяют эффективно                                                    
организовывать и связывать данные, обеспечивая целостность, избегая                                                    
избыточности и упрощая запросы к базе данных.                                                    

**Таких отношений существует три типа:**                                                     

**Один к одному**  (**One-to-One**)                                                    
**Один ко многим** (**One-to-Many**)                                                    
**Многие ко многим** (**Many-to-Many**)                                                    

С течением времени реляционные базы данных стали **более оптимизированными** и                                                     
**мощными**, позволяя разрабатывать сложные и высокоэффективные системы                                                     
хранения данных. Эти принципы легли в основу многих современных СУБД,                                                     
таких как **MySQL**, **PostgreSQL** и **Oracle**.                                                    

**Отношения между таблицами** — ключевой компонент в проектировании **реляционных**                                                     
баз данных, обеспечивающий **гибкость**, **эффективность** и **масштабируемость**                                                     
в управлении данными.                                                    

---

# **One-to-One**                                                    

В отношении "**один к одному**" **каждая запись** в **одной таблице** соответствует                                                     
ровно **одной записи** в **другой таблице**.                                                    

**Пример**

У каждого человека есть только один уникальный идентификационный номер паспорта.                                                     
Паспортные данные и личные данные размещены в разных таблицах, но                                                     
связаны через уникальный номер.                                                    

В SQL это обычно реализуется через использование внешних ключей (`FOREIGN KEY`).                                        

```postgresql
CREATE TABLE IF NOT EXISTS Person (
    id INT PRIMARY KEY,
    Name VARCHAR(35)
);

CREATE TABLE IF NOT EXISTS Passport (
    id INT PRIMARY KEY,
    Passport_number VARCHAR(75),
    Person_id INT,
    FOREIGN KEY (Person_id) REFERENCES Person(id)
);
```

**Какие могут быть проблемы с такой связью:**                                                          

* **Избыточность**: если одна таблица зависит от другой, обе таблицы должны                                                           
быть поддержаны и обновлены одновременно.                                                          
* **Ограниченная гибкость**: изменения в структуре данных одной таблицы                                                           
могут требовать изменений в другой.                                                          

**Но есть и плюсы:**                                                          

* **Четкое разделение и защита данных**: данные, требующие дополнительной                                                           
защиты, могут быть изолированы в отдельной таблице.                                                          
* **Упрощение структуры**: удобно, когда связанные данные редко                                                          
используются вместе.                                                          

---

# **One-to-Many**                                                                 

В отношении "**один ко многим**" **одна запись** в **родительской таблице** может                                                                  
соответствовать **множеству записей** в **дочерней таблице**.                                                                 

**Пример**                                                                 
У одного пользователя может быть множество заказов. Пользовательская                                                                  
запись связана с несколькими записями заказов.                                                                 

Внешний ключ в дочерней таблице указывает на первичный ключ родительской                                                                  
таблице.                                                                 

```postgresql
CREATE TABLE IF NOT EXISTS User (
    id INT PRIMARY KEY,
    Name VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS Order (
    id INT PRIMARY KEY,
    Created_at DATE,
    User_id INT,
    FOREIGN KEY (User_id) REFERENCES User(id)
);
```
**Какие могут быть проблемы с такой связью:**                                                           

* **Обновление и удаление**: при удалении или изменении данных в родительской                                                           
таблице необходимо аккуратно обрабатывать связанные данные.                                                           
* **Может привести к избыточности**, если не оптимизировать структуру данных.                                                           


**Плюсы**                                                           

* **Гибкость**: легко добавлять и удалять записи в дочерних таблицах.                                                           
* **Логичная организация**: интуитивно понятная связь между разными сущностями.                                                           

---

# **Many-to-Many**                                                       

В отношении "многие ко многим" множество записей в одной таблице                                                       
могут быть связаны с множеством записей в другой таблице.                                                       

Пример
Студенты и курсы: каждый студент может посещать множество курсов,                                                        
и каждый курс может быть посещен множеством студентов.                                                       

Используется промежуточная таблица для связи двух других таблиц                                                       

```postgresql
CREATE TABLE IF NOT EXISTS Student (
    id INT PRIMARY KEY,
    Name VARCHAR(35)
);

CREATE TABLE IF NOT EXISTS Course (
    id INT PRIMARY KEY,
    Name VARCHAR(75)
);

CREATE TABLE IF NOT EXISTS StudentCourse (
    Student_id INT,
    Course_id INT,
    FOREIGN KEY (Student_id) REFERENCES Student(id),
    FOREIGN KEY (Course_id) REFERENCES Course(id),
    PRIMARY KEY (Student_id, Course_id)
);
```

**Проблемы**                                                       

* **Сложность**: требуется дополнительная таблица и управление связями.                                                       
* **Производительность**: большое количество связей может замедлить запросы.                                                       

**Плюсы**                                                       

* **Гибкость**: позволяет моделировать сложные взаимосвязи между данными.                                                       
* **Масштабируемость**: подходит для больших и разнообразных наборов данных.                                                       

---

**немношк практики:**                                                       

Давайте создадим с вами ту самую базу данных, которая могла бы быть в                                                 
вашей большой домашке (прошлой) и облегчить вам вашу работу в разы                                              
(просто сперва нужно немного "пострадать", прежде чем прийти к хорошему)                                                       


```postgresql
CREATE TABLE Role (
    id INT PRIMARY KEY,
    name VARCHAR(10) NOT NULL 
);

CREATE TABLE User (
    id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(75),
    phone VARCHAR(20),
    email VARCHAR(75) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    repeat_password VARCHAR(255) NOT NULL,
    role_id INT,
    rating FLOAT DEFAULT 0,
    deleted BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP,
    FOREIGN KEY (role_id) REFERENCES Role(id)
);

CREATE TABLE News (
    id INT PRIMARY KEY,
    title VARCHAR(75) NOT NULL,
    body TEXT NOT NULL,
    author_id INT,
    moderated BOOLEAN DEFAULT FALSE,
    deleted BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES User(id)
);

CREATE TABLE Comment (
    id INT PRIMARY KEY,
    body TEXT NOT NULL,
    author_id INT,
    news_id INT,
    deleted BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES User(id),
    FOREIGN KEY (news_id) REFERENCES News(id)
);
```

```postgresql
INSERT INTO Role (id, name)
VALUES
(1, 'admin'),
(2, 'moderator'),
(3, 'author')
```

```postgresql
INSERT INTO "User" (id, first_name, last_name, phone, email, password, repeat_password, role_id, rating, deleted, created_at, updated_at, deleted_at)
VALUES 
(1, 'Stephanie', 'Bowman', '774 838-03-49', 'bowman.s@gmail.com', 'j%Q9VYcT$m', 'j%Q9VYcT$m', 1, 0, False, '2023-10-20 06:26:20', NULL, NULL),
(2, 'Elizabeth', 'Hebert', '349 217-71-87', 'imiller@gmail.com', '#7YN9dKwoW', '#7YN9dKwoW', 3, 4, False, '2020-09-13 00:55:33', NULL, NULL),
(3, 'William', 'Murphy', '+7 973 206-49-20', 'murphywilliams@gmail.com', ')3QWrItLiO', ')3QWrItLiO', 3, 3, False, '2021-08-18 05:25:18', NULL, NULL),
(4, 'Richard', 'Randolph', '577-545-312-29', 'rich.randolph87@yahoo.com', '(0XZmm(mUP', '(0XZmm(mUP', 2, 0, False, '2022-08-17 08:29:53', NULL, NULL),
(5, 'Connor', 'Wright', '310-354-9477', 'c.wright05@icloud.com', 'FgQ9oHtWW!', 'FgQ9oHtWW!', 2, 0, False, '2022-05-09 05:30:04', NULL, NULL),
(6, 'Robert', 'Moore', '+1-757-645-12-12', 'r.moore98@gmail.com', '62aZrOJD!a', '62aZrOJD!a', 3, 2, False, '2020-04-16 18:53:14', NULL, NULL),
(7, 'Julie', 'Barker', '7547137387', 'juliebarker@gmail.com', 'F_3*JMwaRV', 'F_3*JMwaRV', 3, 3, False, '2021-02-10 21:31:23', NULL, NULL),
(8, 'Michele', 'Santos', '+(514)979-777-10', 'mich.shele78@gmail.com', 'JB5_DaVF+5', 'JB5_DaVF+5', 3, 7, False, '2022-06-22 22:21:40', NULL, NULL),
(9, 'Vanessa', 'James', '+1-783-501-525', 'vanessa92@icloud.com', '$z8P3AHbd1', '$z8P3AHbd1', 3, 1, False, '2021-02-23 23:54:03', NULL, NULL),
(10, 'Anna', 'Hall', '(961)123-3341', 'a.hall@yahoo.com', 'Z67JrxaF(R', 'Z67JrxaF(R', 3, 8, False, '2020-03-21 21:57:01', NULL, NULL),
(11, 'Jesus', 'Michael', '001-769-190', 'jes.mich@gmail.com', 'nBK!3VAd@#', 'nBK!3VAd@#', 3, 8, False, '2022-03-19 15:43:11', NULL, NULL),
(12, 'Angela', 'Rodriguez', '671 584-69-98', 'ang.rodriguez@gmail.com', '^70HRg4a*j', '^70HRg4a*j', 3, 9, False, '2022-04-15 02:19:18', NULL, NULL),
(13, 'Whitney', 'Mcneil', '950 611-87-26', 'whitney.mc83@gmail.com', '4osy0Sph+n', '4osy0Sph+n', 3, 4, False, '2023-09-25 03:32:25', NULL, NULL),
(14, 'Brenda', 'Walter', '715 359-63-93', 'br.endawalt@yahoo.com', 'u&5I$ZvLrD', 'u&5I$ZvLrD', 3, 8, False, '2023-09-25 03:05:46', NULL, NULL),
(15, 'Christopher', 'Wells', '740 396-53-71', 'sevans@gmail.com', '(2&EZqlKO(', '(2&EZqlKO(', 3, 8, False, '2022-02-11 19:35:00', NULL, NULL),
(16, 'David', 'Lynch', '+1 696 009-34-74', 'uthompson@yahoo.com', 'ii08vEpNl+', 'ii08vEpNl+', 3, 4, False, '2023-08-17 11:48:04', NULL, NULL),
(17, 'Christopher', 'Daniels', '388 979-66-24', 'gbates@icloud.com', '5eYMuSpV*G', '5eYMuSpV*G', 3, 3, False, '2022-04-30 19:13:31', NULL, NULL),
(18, 'Jared', 'White', '121 676-00-62', 'jared97.white@yahoo.com', '+$we67NymB', '+$we67NymB', 3, 7, False, '2020-10-22 08:29:51', NULL, NULL),
(19, 'Ashley', 'Washington', '+13 455-81-47', 'xevans@yahoo.com', ')6RGBn9h@7', ')6RGBn9h@7', 3, 5, False, '2022-09-30 20:20:36', NULL, NULL),
(20, 'Clinton', 'Cochran', '+001 771-79-60', 'radams@gmail.com', '@Ir2FeLsw&', '@Ir2FeLsw&', 3, 7, False, '2021-05-05 12:06:42', NULL, NULL),
(21, 'Stephanie', 'Wong', '780 464-31-88', 'michele91@icloud.com', 'b_6ZSEsvwQ', 'b_6ZSEsvwQ', 3, 2, False, '2021-07-24 22:12:34', NULL, NULL),
(22, 'Jacqueline', 'Perkins', '+425 350-11-29', 'voneal@yahoo.com', 'pzR0QxDD!%', 'pzR0QxDD!%', 3, 8, False, '2021-06-13 15:23:44', NULL, NULL),
(23, 'Ronald', 'Howard', '694 624-24-73', 'candicecollins@icloud.com', '(bzSTNpNa5', '(bzSTNpNa5', 3, 8, False, '2021-11-06 04:44:16', NULL, NULL),
(24, 'Kaitlin', 'Downs', '+001 844-79-52', 'tammy54@yahoo.com', '&%RUQk4mXJ', '&%RUQk4mXJ', 2, 0, False, '2021-12-23 08:13:56', NULL, NULL),
(25, 'Robert', 'Miller', '+1 284-107-020', 'qhayes@gmail.com', 'ZvovI*yS*9', 'ZvovI*yS*9', 2, 0, False, '2020-04-25 01:16:09', NULL, NULL);
```

```postgresql
INSERT INTO News (id, title, body, author_id, moderated, deleted, created_at, updated_at, deleted_at)
VALUES
(1, 'Debate picture stop interesting weight.', 'Prepare measure every play western realize. Poor do herself head.', 20, False, False, '2021-04-03 02:26:36', NULL, NULL),
(2, 'Name project she response size face measure.', 'Push term industry glass. Husband natural while goal one training follow. Store what especially drive crime. Later heart price little skin score contain.', 20, True, False, '2023-08-19 20:02:15', NULL, NULL),
(3, 'Manager article customer write involve this.', 'Age still defense history. Large boy free finish above base onto. Grow seek marriage six sport none Congress. Either move meet everybody piece great or with. Occur song school third popular.', 6, False, False, '2023-08-23 07:16:02', NULL, NULL),
(4, 'Federal Democrat read any scene third protect.', 'And five particularly red someone seek focus expert. Drive tonight hair play. Ability space research movement move.', 11, False, False, '2020-06-19 07:25:49', NULL, NULL),
(5, 'Them smile able whether challenge.', 'Too writer son receive training again remain nearly. While wrong base choice live serve center physical.', 11, False, False, '2023-05-16 09:36:02', NULL, NULL),
(6, 'Attorney different employee need.', 'Particular end test affect difficult or. Soon security half loss move. Action suddenly upon imagine so free adult. Believe finish box play. Right chance interesting world decade analysis film appear.', 14, True, False, '2020-05-15 13:41:40', NULL, NULL),
(7, 'Agree value page effort.', 'Whole late within piece weight particularly social agreement. Then arrive camera forget. Together hotel its into computer. Any much floor message pretty trip month.', 16, False, False, '2023-08-26 02:19:20', NULL, NULL),
(8, 'Detail modern approach teacher.', 'Better window her case. Chair business off sit cost. Yeah attention forget. Gun everyone positive prove heavy strong. Cell lay top scientist process red hospital often. Art agency traditional along.', 9, False, False, '2020-05-19 07:48:49', NULL, NULL),
(9, 'Court ok value large individual.', 'Try hotel up walk. None other defense people after career. Maybe himself cup consumer what believe office.', 8, False, False, '2023-04-29 11:52:08', NULL, NULL),
(10, 'There including face.', 'Show cost treat keep. World sing decade truth. Minute eight talk consider response reduce. List actually worry benefit participant. It collection today answer.', 18, True, False, '2023-09-25 20:40:00', NULL, NULL),
(11, 'Outside argue view teacher study.', 'Truth thus attack save participant dog wish. During customer both box product. Little how look pick simple actually easy. Bill mean low spend themselves night wind outside.', 20, True, False, '2022-07-24 04:24:06', NULL, NULL),
(12, 'Bar growth report increase.', 'Could attention include leader movie. Such remember threat. Against itself new. Community happen region support our side.', 2, False, False, '2020-02-10 04:45:18', NULL, NULL),
(13, 'Part read good control young financial attention.', 'Them country give sport unit beyond. Pass especially give everyone upon. Good about source fight play despite word. Soldier note what there skill land. Truth ground describe only consider believe.', 2, True, False, '2023-03-11 09:41:40', NULL, NULL),
(14, 'Character cover yard really fact drop.', 'Today rise need college level those. Soldier federal prevent speak. Cut exist state improve. Picture service rule participant understand. Artist up ball ahead short save wish reveal.', 21, False, False, '2023-11-05 19:39:15', NULL, NULL),
(15, 'Figure economic particularly lead particularly.', 'Threat full suddenly area bring also go on. Best purpose one attack computer describe. Hour protect form win fill.', 2, False, False, '2022-04-15 22:02:57', NULL, NULL),
(16, 'Outside enjoy result suffer five.', 'Protect apply include meeting what. Trial test begin if industry. Type crime yourself big. Attorney organization some. Wide black reflect capital police.', 19, True, False, '2023-02-26 06:10:50', NULL, NULL),
(17, 'Civil religious increase environment to laugh.', 'Ago when receive student. Eye lawyer small threat. Authority paper let several attack. Would minute herself sense. Key north family reflect significant help produce. Foot nor firm senior buy while.', 18, True, False, '2023-09-14 12:39:13', NULL, NULL),
(18, 'Travel time image most personal blood degree.', 'Necessary create travel ability wish. At happen color medical street. Pay personal truth kid result safe half.', 11, True, False, '2022-12-07 23:41:22', NULL, NULL),
(19, 'Ok price their candidate than environmental student modern.', 'Live add drop return dark time you. Actually social contain forward candidate. Run strategy choice team. Leave political thank six attention hope interesting. Kid nature order something subject dog.', 3, False, False, '2021-08-31 06:06:45', NULL, NULL),
(20, 'Score shake company window another important serious.', 'Become training part take visit perhaps board. Clear later Congress environment. Part test these TV. Kind seven soldier expect mind. Help sell task include. Family look same stand office experience.', 8, False, False, '2021-02-13 00:55:59', NULL, NULL),
(21, 'Fly fund sister image develop.', 'Bar Mr shoulder focus stage member. Character expert argue at chair wrong base. Help themselves tough explain. Buy operation bit. Trial tell feeling once red then.', 21, True, False, '2023-08-09 17:45:00', NULL, NULL),
(22, 'Parent section begin become brother sit hear.', 'Son character join serve. Account reduce determine occur bill. Instead painting data structure. Science wait both including best another result. Win ready yes admit.', 2, False, False, '2020-02-20 12:20:41', NULL, NULL),
(23, 'Six learn red night treatment inside.', 'Far quality suggest heart base difficult. Course media structure family country one. Claim describe couple government ever allow hard.', 8, False, False, '2022-07-30 12:49:52', NULL, NULL),
(24, 'Which group threat so son dinner child free.', 'Several writer general interview then collection. At past actually imagine throughout structure situation country. Create really two eye behind thank.', 6, False, False, '2020-11-13 23:41:03', NULL, NULL),
(25, 'My prevent that bill.', 'Appear debate skin choose forward finally. As member red economy Mrs. Have produce ask. Politics already mother particularly cold. Film involve wall ground win involve.', 11, False, False, '2021-12-15 13:06:25', NULL, NULL),
(26, 'Quite drop keep race police player home.', 'Region offer scientist art major return different. Interesting out approach side lawyer issue cell.', 13, True, False, '2020-07-14 05:14:29', NULL, NULL),
(27, 'Theory offer environmental those.', 'Range road music marriage. Front anyone child service time buy movie nothing. Data outside material. Say rich list three realize. Education party democratic offer.', 18, True, False, '2020-05-25 04:57:51', NULL, NULL),
(28, 'Avoid should teach think everybody discover.', 'Share behind issue able letter election sister. Compare let but why professor after song six. Trouble science job newspaper bit. Skin color against well on yes thought. Lay charge discussion game.', 11, False, False, '2021-11-23 09:38:44', NULL, NULL),
(29, 'Team start team member risk.', 'Listen ask property toward home. Tough beautiful information fast. Address service visit reduce lawyer. Drug poor oil although. Among heart paper drug tough nothing you.', 23, True, False, '2022-09-22 13:13:41', NULL, NULL),
(30, 'Line produce most.', 'Stop rich too despite. Recently there since have. Dream easy language issue which better affect. Stop gun two face tell when tree.', 10, False, False, '2021-09-24 05:39:39', NULL, NULL),
(31, 'Camera gun however.', 'Window painting cause partner majority light draw. Available return team visit firm responsibility. Tv practice size. Also bad her base rock.', 22, True, False, '2022-04-03 04:06:29', NULL, NULL),
(32, 'Worker term star reflect stage benefit feel section.', 'Lay suddenly dark work population charge should. Program enjoy worry fear offer. Different share sound need so almost support.', 22, True, False, '2020-05-28 23:35:42', NULL, NULL),
(33, 'Hospital spring drug sound mind whatever.', 'Suddenly hundred service modern sort win I. Local military two should idea everyone during. May style him dream. Thank quality prepare arrive.', 20, True, False, '2022-05-29 21:22:16', NULL, NULL),
(34, 'Two follow man why.', 'East treat cultural generation art official material house. Training establish sit return. War program set stop attorney try.', 7, True, False, '2020-08-22 02:11:54', NULL, NULL),
(35, 'Training near possible surface if.', 'Town assume return school even find. If reduce president remain local. Month institution high. Budget science determine. Face store human fall dinner start. Enter alone open air before.', 23, True, False, '2022-09-18 23:27:47', NULL, NULL),
(36, 'Glass buy soldier movie realize level spend her.', 'Over recently control station. Company sometimes turn sell. Down should story each industry produce.', 20, False, False, '2022-07-24 01:46:16', NULL, NULL),
(37, 'Sit can hundred suffer against easy shake.', 'Myself property wear property care. Year man subject admit community. Class teach author thing what involve. Name community hotel develop left.', 7, False, False, '2021-12-14 02:16:15', NULL, NULL),
(38, 'And safe wife hard whatever their news.', 'Full likely than enter measure down. Scientist someone kind. Girl exactly trip toward lawyer benefit. Wind site near send hear art seat. Improve mind side sometimes themselves view.', 18, True, False, '2022-12-16 15:38:51', NULL, NULL),
(39, 'Against table drop lawyer.', 'Feeling stock while. Throw mind staff author. Relate exactly matter network. Quality tell career. Contain left necessary. Hit citizen official best.', 16, True, False, '2022-09-28 17:52:43', NULL, NULL),
(40, 'Debate knowledge challenge range result cost skill.', 'Current stop billion ago nice. Particularly office dinner save act quality child. Ok stop hotel fall weight century continue.', 9, False, False, '2022-12-08 03:15:36', NULL, NULL);
```
```postgresql
INSERT INTO Comment (id, body, author_id, news_id, deleted, created_at, updated_at, deleted_at)
VALUES
(1, 'Money but parent address strategy pattern. Onto respond space identify agent four. Trouble once market security couple plan. Authority maintain whom school effort.', 13, 22, False, '2022-03-27 04:35:14', NULL, NULL),
(2, 'Car wear remember believe. Fund reduce life class. Individual especially red region fact teach drop. Where situation read. Among including four prevent check learn but age.', 8, 21, False, '2023-07-25 14:56:20', NULL, NULL),
(3, 'Effort exist expect. Dark high keep sure least again change. Let myself day entire major increase.', 20, 6, False, '2020-12-16 15:32:08', NULL, NULL),
(4, 'Inside beautiful yeah expect. Leg environment prevent how successful. Them collection place middle however human address. Month but idea lead enjoy live imagine. Also great human.', 19, 20, False, '2020-08-20 12:18:46', NULL, NULL),
(5, 'Girl key human discover entire once action. World already offer report theory create. Receive minute itself pretty. Many heavy last blood.', 22, 14, False, '2020-12-05 17:10:21', NULL, NULL),
(6, 'Example reality religious car close per. Option suffer appear run. Type area measure become. Sort form push real official. Performance show dinner drug.', 7, 10, False, '2023-03-02 07:25:46', NULL, NULL),
(7, 'Movement painting section. Agreement performance democratic way. Clearly treatment herself bar fill child red art.', 19, 16, False, '2021-07-29 11:42:39', NULL, NULL),
(8, 'Threat parent like. Big ever white deal dark price official none. Fish western large religious. Return thank program bank. Happy teach tough choice. His miss light pretty.', 21, 28, False, '2021-05-06 22:42:31', NULL, NULL),
(9, 'Then property within authority miss quickly. Check boy almost back gun three sea. Body current even trade common. Four garden bed. Trial face near black down discover standard school.', 11, 38, False, '2020-05-04 12:38:16', NULL, NULL),
(10, 'Else boy billion eat language site defense. Provide hand successful safe material today. Myself car strategy writer memory pass.', 22, 34, False, '2023-01-25 15:11:19', NULL, NULL),
(11, 'Seat smile conference program true. According maybe tree answer. Political including outside what answer. Three seek official boy nation soon whether. Have concern would PM daughter face.', 23, 4, False, '2021-01-24 07:48:51', NULL, NULL),
(12, 'Ever people senior phone lead. Make some country story possible. Back drive us trouble. Keep need need behind from black surface sit.', 8, 39, False, '2021-10-17 16:15:09', NULL, NULL),
(13, 'Talk thus somebody property. Art account red prove. Economy book than four time. Debate focus I life. Beautiful feel central study public live song.', 21, 7, False, '2020-05-16 16:53:34', NULL, NULL),
(14, 'Affect purpose town instead. Determine quickly speech ago first agree our. Here memory open those.', 15, 22, False, '2021-02-25 13:09:07', NULL, NULL),
(15, 'Interview another end however dark again before. Still kind develop better. Some woman never effort. Possible vote about space today. Wife table suffer drive.', 22, 22, False, '2020-06-07 17:15:35', NULL, NULL),
(16, 'Seat claim almost natural past need. Off over against computer easy. Take off campaign any administration assume near. Wait over campaign miss race should animal.', 21, 34, False, '2023-07-17 13:55:00', NULL, NULL),
(17, 'Fall one environmental know fund. Political west president. Our wind sit fly collection a too three. Actually nation center charge.', 12, 32, False, '2022-11-22 08:19:03', NULL, NULL),
(18, 'Central these anyone end. Star necessary off situation his good adult. Would career every travel ahead. Likely choice move success difficult ok. Crime bring rate technology drive.', 19, 35, False, '2020-10-11 11:57:50', NULL, NULL),
(19, 'Impact kid ago sign son spring. Stand city upon democratic majority truth. Standard discuss second remain race life. Movement difficult increase lose boy.', 19, 9, False, '2022-03-25 16:12:20', NULL, NULL),
(20, 'Me nearly number account religious just. Better region full. Itself present music half realize simply. Game page leader nearly.', 12, 8, False, '2022-06-18 01:50:39', NULL, NULL),
(21, 'Girl community she commercial outside. Method describe wish ball there. Heart woman movie into religious southern consumer concern.', 14, 18, False, '2021-08-19 13:07:04', NULL, NULL),
(22, 'Human own party people how modern capital. Its likely trip Republican analysis interesting. Away when establish reason human bit couple mouth. Candidate look nothing per follow follow house letter.', 14, 1, False, '2023-03-16 11:48:12', NULL, NULL),
(23, 'Possible across tree. Should teacher policy through act. Church school free through low hard give. Look walk card leave relate able.', 10, 39, False, '2020-03-29 16:58:48', NULL, NULL),
(24, 'Boy break compare discuss too building. Tonight remember doctor responsibility world. Begin say book suggest mean himself realize.', 6, 15, False, '2023-07-24 06:59:15', NULL, NULL),
(25, 'Ever third from it front between type. Happen nothing word financial team win century. Movement off media order reduce glass.', 20, 23, False, '2020-01-16 03:32:52', NULL, NULL),
(26, 'Bad drug expect us. Region season approach decision. Painting small too fall. Style long middle. She goal area customer government. Big task power politics box deep.', 7, 18, False, '2021-02-04 00:48:30', NULL, NULL),
(27, 'Continue year interest amount through lose. Interview outside phone choose I discover including. Quite baby itself population.', 6, 14, False, '2021-10-20 06:06:32', NULL, NULL),
(28, 'Force similar audience bit center amount. Page available present notice support. Education hit popular down offer.', 3, 19, False, '2021-04-07 07:47:40', NULL, NULL),
(29, 'Million successful front conference day international economic. Station matter yes attack actually buy. Meet more under single. Attack since trip image spring wrong.', 2, 8, False, '2022-05-22 11:35:56', NULL, NULL),
(30, 'Leave make indicate commercial. Debate month reflect ready moment. Bad assume major sign great candidate reality. Project big follow special card. Heavy however cold spring happen whatever.', 12, 1, False, '2021-01-22 06:37:00', NULL, NULL),
(31, 'Free large time series cell own. Partner always rule different wall card generation. Compare stock expert window.', 17, 23, False, '2020-12-02 03:02:49', NULL, NULL),
(32, 'Main little popular president be experience moment image. Suddenly moment short recognize trade finally. Challenge race possible bit usually various bill talk.', 18, 9, False, '2020-07-31 16:13:51', NULL, NULL),
(33, 'Single case protect call above follow issue show. Wish player goal land day late mean growth. Parent set of action provide.', 13, 29, False, '2020-09-19 12:19:31', NULL, NULL),
(34, 'Child federal tell marriage media effort. Event wonder general call. Position beautiful deep treatment specific authority. Here adult next successful although. Book these campaign three.', 11, 29, False, '2020-08-28 11:42:06', NULL, NULL),
(35, 'Never once arm study. Every during never personal toward marriage. View sea different certainly their line. Significant store drug. All customer side. Response strong these.', 2, 28, False, '2023-07-20 09:28:35', NULL, NULL),
(36, 'Education its mention above would. That eight color laugh option. Include attack improve with four.', 7, 26, False, '2021-08-05 12:06:06', NULL, NULL),
(37, 'Have sister at expect computer small. These Mrs specific mission. Doctor significant author agree white. Can full stock stand huge.', 13, 16, False, '2021-01-21 15:48:49', NULL, NULL),
(38, 'So prevent get difficult develop. Room share walk employee seven recent. Trip wall thought nation. Point direction decade special. Story though college with power research walk from.', 2, 39, False, '2020-03-17 20:08:13', NULL, NULL),
(39, 'Set direction happy we choice ground be summer. Policy on respond current play fire model. Poor start identify. Blood I firm. Standard central in over quite growth where.', 7, 37, False, '2022-05-04 23:00:25', NULL, NULL),
(40, 'Admit east point traditional. Get democratic action hot ahead war when. Total expect firm night. Piece wife personal win.', 22, 23, False, '2020-11-13 21:18:47', NULL, NULL),
(41, 'War behind business investment. Camera simple yourself learn school military either. Every out so executive turn. Arm skill director these hot change bar. Value edge wish.', 20, 1, False, '2022-09-23 23:53:06', NULL, NULL),
(42, 'Challenge later federal compare sense. Answer chair ahead. Land reflect east citizen common.', 8, 34, False, '2021-02-14 05:25:56', NULL, NULL),
(43, 'Sing establish world experience. Time total lawyer lose prepare. Rather employee business those. Up age find son. Hard safe during. Partner use develop. Let station rest guess.', 15, 37, False, '2020-02-06 02:34:38', NULL, NULL),
(44, 'Increase player a north term by third. Southern production anyone long gun. Over Democrat difference western prevent. Candidate cause probably speech.', 22, 21, False, '2023-03-08 08:38:43', NULL, NULL),
(45, 'Bag believe produce almost subject. Sense contain few deal enter sell. Role politics recent strong west born.', 13, 27, False, '2023-01-31 00:20:10', NULL, NULL),
(46, 'Positive need article sing seven they forget law. Understand until alone across carry describe. Traditional news mother card. Picture later office leader grow new. Food these general enjoy.', 11, 26, False, '2020-07-19 02:34:43', NULL, NULL),
(47, 'Carry attorney north kid. Up professional see one entire soldier account. Everybody early thus but stock. Government age room determine.', 16, 2, False, '2020-10-11 09:13:27', NULL, NULL),
(48, 'No after theory throughout present camera. Task bag trip various dog agency. Protect build mission writer. Decade issue social result finish moment expect. Central military ago plan best bar.', 20, 25, False, '2023-09-21 17:33:14', NULL, NULL),
(49, 'Stuff produce six treat. Your quality plant provide must action culture. Probably hospital kid yard Mr election. Coach fine between enough. Paper understand special Mrs could good who third.', 14, 33, False, '2021-10-16 01:42:26', NULL, NULL),
(50, 'Glass to scientist road. Tell add without evidence here teach you. Former appear administration assume week. Weight along successful rate school. Least set hand smile.', 13, 39, False, '2021-05-04 12:47:42', NULL, NULL),
(51, 'Especially accept Congress method case base career. Town thing behind across. Range southern big find sense. Laugh rock customer degree. Event father project wrong. Opportunity cell then red.', 10, 6, False, '2020-02-26 13:34:01', NULL, NULL),
(52, 'Detail much kid manage decide foot test. Former box citizen now yes. Back eye reason door really respond. Light decide night. Party plan cold determine.', 20, 9, False, '2021-04-25 21:50:11', NULL, NULL),
(53, 'American suffer common treat reality produce. Force clearly there. Available week old great. Strong might feeling measure community arm should. Set myself study a attorney report on see.', 19, 39, False, '2022-03-06 23:24:16', NULL, NULL),
(54, 'Individual film great research medical black all. Into police arrive. Consumer base they nothing budget magazine. Instead statement tree return sell.', 13, 12, False, '2023-05-18 05:48:01', NULL, NULL),
(55, 'After show radio dark pick through. Rest eye page notice. Pretty TV fight when film. Finally speech north standard state. Tax large front teach. Clearly piece back continue.', 9, 30, False, '2023-02-18 17:13:20', NULL, NULL),
(56, 'Can class begin institution. Section author eye cold either blue. Available enough notice simply crime. Rule before fight however. Treatment first thousand herself might no.', 18, 6, False, '2023-09-10 08:56:35', NULL, NULL),
(57, 'Standard drug example hot. Growth water once vote surface black rise. History stage religious mention again well think.', 15, 21, False, '2022-03-19 23:33:27', NULL, NULL),
(58, 'Ground space discussion. Whether nature beyond. Customer employee doctor quickly when across. Local think chance some catch very the. See important night decide pretty soon else.', 14, 39, False, '2021-04-10 06:10:10', NULL, NULL),
(59, 'Item through much certainly budget. Message firm note itself soldier information. She second same must offer present.', 12, 1, False, '2020-12-15 19:43:44', NULL, NULL),
(60, 'We your also as hair rock adult. Age officer day network end Mrs so. Part item reach none of oil over. Human forget lay Mr test. Employee method political.', 13, 21, False, '2020-11-25 05:17:24', NULL, NULL),
(61, 'Really college several region anyone herself. Case detail would drug cold. Character similar difference interest another. If window enough deep easy rock. Debate officer social else.', 2, 27, False, '2023-03-29 04:55:42', NULL, NULL),
(62, 'Night go listen other. Together simply apply body. Ten hand offer born big. Morning really international store rate hold.', 15, 22, False, '2020-09-18 14:45:34', NULL, NULL),
(63, 'Say effect area just town. Owner arm standard generation. Reality child chair eye wear cold. People approach peace official how. Field brother structure kitchen top exist age.', 17, 17, False, '2022-01-18 01:34:03', NULL, NULL),
(64, 'Him quickly cold establish example program. Poor word his free. Start piece face leader research old right.', 12, 10, False, '2020-04-15 21:53:01', NULL, NULL),
(65, 'Half yeah onto. One choice reveal thing. Shoulder learn item professor above interesting rule. Hear leave list establish large clear town. Issue dream similar seem.', 6, 33, False, '2023-03-12 21:14:51', NULL, NULL),
(66, 'Pretty both away close stay especially bed. Father southern ago half stock issue. Visit above term still card for list. Responsibility trade behind subject. True time over range.', 22, 23, False, '2020-12-10 04:48:01', NULL, NULL),
(67, 'Outside such show society realize purpose. Director shake management meet issue reason his cultural. Born author address herself who.', 20, 20, False, '2020-03-17 16:21:58', NULL, NULL),
(68, 'Pay between year arrive. Power base total change. Agency glass voice though mouth health. During part sit budget program.', 17, 21, False, '2022-07-29 21:27:57', NULL, NULL),
(69, 'Ask would six glass more political. American nothing religious minute. Reflect approach them professor human course. Growth certain star way reality. Entire husband drop billion account woman.', 7, 9, False, '2021-05-11 03:17:30', NULL, NULL),
(70, 'Brother possible dinner seven record person. How name it. Fall majority agency deep later. Along daughter already organization time according million will. Rich may bad at.', 19, 29, False, '2020-12-15 22:04:26', NULL, NULL);
```

---

# **Insert\delete forgotten columns**                                                 

Если каким-то невероятным чудом вы забыли добавить поле, а таблица уже создана                                                 
и даже заполнена данными - вы всё ещё можете это сделать (на свой страх                                                 
и риск) благодаря определённым командам, которые позволяют нам вставлять                                                 
новые поля, задавать им нужные настройки и даже вставлять их в определённое                                                 
место в таблице                                                 

В SQL добавление новых полей в существующую таблицу можно выполнить с                                                  
помощью команды `ALTER TABLE`                                                 

**Добавление Поля в Конец Таблицы**                                                        

Это самый простой способ добавления поля. Допустим, вы хотите добавить поле                                                        
`date_of_birth` типа `DATE` в таблицу `User`. Для этого используйте                                                         
следующую команду:                                                        

```postgresql
ALTER TABLE "User" ADD date_of_birth date;
```

После выполнения этой команды, поле `date_of_birth` будет добавлено в конец                                                 
списка полей таблицы `User`.


**Добавление Поля в Конкретное Место в Таблице**                                                

В некоторых системах управления базами данных, таких как `MySQL`, вы можете                                                 
указать местоположение нового поля в таблице. Например, если вы хотите                                                 
добавить поле `rating` после поля `body` в таблицу `News`,                                                 
используйте команду:                                                

```postgresql
ALTER TABLE News ADD rating FLOAT DEFAULT 0 AFTER body; -- не сработает в postgresql
```

Это добавит поле `rating` непосредственно после поля `body`. Однако                                                
стоит отметить, что **не все** **СУБД** поддерживают возможность указания                                                
точного места добавления поля. В таких системах, как `PostgreSQL`,                                                 
поля **всегда** добавляются **в конец таблицы**.                                                

**Важные Замечания**                                                

1) **Перед Изменением Структуры**: **Всегда** делайте резервную копию данных перед                                                 
изменением структуры таблицы, особенно в производственных системах.                                                

2) **Влияние на Существующие Данные**: Добавление новых полей может повлиять                                                 
на существующие запросы и приложения, использующие эту таблицу.                                                 
**Убедитесь**, что все зависимые системы **обновлены** для работы с новой структурой.                                                

3) **Значения по Умолчанию**: Если новое поле не может быть `NULL`, **убедитесь**, что вы                                                 
предоставили значение по умолчанию или заполнили это поле для всех                                                 
существующих записей.                                                

Для **удаления** поля (столбца) из существующей таблицы в `SQL`, вы также будете                                                 
использовать команду `ALTER TABLE`, но с ключевым словом `DROP COLUMN`.                                                 
Вот как это работает:                                                

ДОпустим всё же не нужно нам поле с датой рождения у пользователя:                                                  

```postgresql
ALTER TABLE "User" DROP COLUMN date_of_birth;
```

Эта команда удалит столбец `date_of_birth` из таблицы `User`.                                                

**Важные Замечания**                                                

**Влияние на Данные**: При удалении столбца все данные, содержащиеся в этом                                                 
столбце, будут **безвозвратно утеряны**. Это действие **необратимо**, поэтому                                                 
убедитесь, что вам действительно не нужны данные из этого поля.                                                

**Влияние на Зависимые Запросы и Приложения**: Удаление столбца **может нарушить**                                                 
**работу SQL-запросов**, **представлений**, **триггеров** и **приложений**, которые                                                 
**зависят** от этого столбца. Перед удалением столбца **убедитесь**, что это не                                                 
повлияет на функциональность вашей системы.                                                

**Резервное Копирование**: Всегда полезно иметь актуальную резервную копию вашей                                                 
базы данных перед тем, как вносить в нее изменения. Если после удаления                                                 
столбца возникнут проблемы, вы всегда сможете **восстановиться** из                                                
резервной копии.                                                

**Ограничения и Совместимость**                                                

* Некоторые базы данных могут иметь ограничения или дополнительные требования                                                 
для удаления столбцов. Например, в некоторых случаях может потребоваться                                                 
обновление или пересоздание индексов и ключей, связанных со столбцом.                                                
* В различных **СУБД** синтаксис команд может немного отличаться, поэтому                                                 
всегда полезно проверять документацию конкретной **СУБД**, с которой вы работаете.

---

# **SQL JOIN**

На старте появления баз данных и систем их управления был вполне себе                                                
резонный вопрос: "А как, собственно, данные получать, если нужны они                                                  
из разных таблиц..?"                                                     

Вполне себе можно попробовать тему: просто передавать в команде **FROM**                                               
названия нужных таблиц через запятую и всё, не париться!                                                    

```postgresql
SELECT *
FROM News, Comment;
```

Но, к сожалению или счастью, не всё так просто!                                                          

При таком подходе мы получаем абсолютно неправильную, грамоздкую, неупорядоченную                                       
и просто ужасную структуру                                                         

результат будет представлять собой [декартово произведение](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D1%8F%D0%BC%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5) (или перекрестное                                                          
соединение) этих таблиц. Это означает, что каждая строка из первой таблицы                                                          
будет соединена с каждой строкой из второй таблицы.                                                         


Допустим, у нас есть таблицы `User` и `News`. Таблица `User` содержит **5**                                                          
записей, а таблица `News` - **10** записей. Если мы выполним запрос:                                                         

```postgresql
SELECT *
FROM User, News;
```

То мы получим **декартово произведение** этих таблиц, что в данном случае                                          
будет состоять из **50** (**5x10**) строк. Каждая строка из таблицы `User`                                          
будет повторена **10** РАЗ, **по одному разу для каждой строки** из таблицы `News`.                                         


Это приведет к **массовому дублированию данных**, что делает результат **трудным**                                                          
**для анализа** и может привести к путанице.                                                         

Так же, такой запрос **не учитывает** связи между таблицами. Это означает,                                                          
что даже если в таблицах есть связанные данные через внешние ключи,                                                          
этот запрос **не** **позволит** корректно их отобразить.                                                         

Выполнение такого запроса может быть очень **неэффективным**, особенно если                                                          
таблицы содержат **большое количество данных**.                                                         


Команда `JOIN` в `SQL` появилась вместе с разработкой реляционных баз данных.                                                         
**Эдгар Кодд**, создатель реляционной модели для баз данных, ввел концепцию                                                         
`JOIN` как **способа объединения данных** из **двух или более** таблиц                                                         

Основная проблема, которую решают `JOIN`'ы, заключается в необходимости                                                          
**объединять данные** из **разных таблиц** для формирования полных и комплексных                                                          
запросов. В реальности данные часто распределены по многим таблицам,                                                          
и для их анализа требуется их объединение.                                                         

---

# **Types of JOINs and their Mechanics**                                                         


#### **INNER JOIN**                                                         

* **Механика**: Возвращает строки, когда есть соответствие в обеих таблицах.                                                         
* **Пример**: Получить список всех пользователей и их комментариев.                                                         

```postgresql
SELECT "User".first_name, "User".last_name, Comment.body
FROM "User"
INNER JOIN Comment ON "User".id = Comment.author_id;
```

#### **LEFT JOIN (или LEFT OUTER JOIN)**                                                  

* **Механика**: Возвращает все строки из **левой таблицы** и соответствующие строки                                                   
из **правой таблицы**. **Если совпадений нет**, возвращается `NULL` на                                                  
месте **правой таблицы**.                                                  
* **Пример**: Получить список всех пользователей и их новостей, даже                                                   
если у пользователей нет новостей.                                                  

```postgresql
SELECT "User".first_name, "User".last_name, News.title AS news_title
FROM "User"
LEFT JOIN News ON "User".id = News.author_id;
```

#### **RIGHT JOIN (или RIGHT OUTER JOIN)**                                                     

**Механика**: Аналогичен `LEFT JOIN`, но возвращает все строки из                                                      
**правой таблицы**.                                                     
**Пример**: Получить список всех новостей и их авторов, даже                                                      
если у новостей **нет авторов**.                                                     

```postgresql
SELECT News.title, "User".first_name, "User".last_name
FROM News
RIGHT JOIN "User" ON News.author_id = "User".id;
```

#### **FULL OUTER JOIN**                                                           

**Механика**: Возвращает строки, когда есть совпадение **в одной из**                                                            
**таблиц**. Если **нет совпадения**, то возвращается `NULL`.                                                           
**Пример**: Получить список всех новостей и всех комментариев,                                                            
вне зависимости от наличия связи.                                                           

```postgresql
SELECT News.title, News.author_id AS news_author, News.moderated, Comment.body AS comment_text, Comment.author_id AS comment_author
FROM News
FULL OUTER JOIN Comment ON News.id = Comment.author_id;
```

#### **CROSS JOIN**                                                       

* **Механика**: Создает декартово произведение двух таблиц, т.е. соединяет                                                       
каждую строку одной таблицы со всеми строками другой таблицы.                                                       
* **Пример**: Получить все возможные комбинации пользователей и новостей.                                                       

```postgresql
SELECT "User".first_name, "User".last_name, News.title AS news_title
FROM "User"
CROSS JOIN News;
```

---

# **Nested queries**                                               

С разного рода объединениями, отношениями мы разобрались, супер!                                                   
Но есть ещё вот какой важный момент:                                             

ЧТо делать, если мы захотим в **одной таблице** получить необходимые данные,                                                
только тех записей, **вторичный ключ** которых будет равен определённому значению,                                           
При этом поля (любые) из другой таблицы нас **АБСОЛЮТНО** **не интересуют**,                                                   
нам нужны только **id** этих записей для выборки в первой таблице.                                                 

В таком подходе мы могли бы, конечно сделать следующее:                                               

1) Выбрать все интересующие нас id из второй таблицы отдельно                                                  
2) Вставить эти id в наш основной запрос.                                                    

```postgresql
SELECT id
FROM "User"
WHERE email LIKE '%yahoo.com';
```

```postgresql
SELECT *
FROM NEWS
WHERE author_id IN (4, 10, 14, 16, 18, 19, 22, 24);
```

Примерно вот так. Но на сколько ок так делать с точки зрения траты времени,                                            
затрат ресурсов и написания самого sql?                                                  

Для таких ситуаций нам могут прийти на выручку такие интересные штуки, как                                              
**вложенные запросы**                                                     

**Вложенные запросы** (или **подзапросы**) в `SQL` — это запросы, размещенные **внутри**                                                     
другого **SQL-запроса**. Они могут использоваться в различных частях основного                                                     
запроса, включая `SELECT`, `FROM`, `WHERE` и даже в `HAVING`. Вложенные запросы                                                      
позволяют выполнять более сложные операции, такие как **агрегация**, **фильтрация**                                                      
и **сравнение данных на основе результатов другого запроса**.                                                     

**Как работают вложенные запросы**                                                              

* **Выполнение вложенного запроса**: Сначала выполняется вложенный запрос, который                                                               
возвращает некоторые данные.                                                              
* **Использование результатов вложенного запроса**: Затем эти данные используются                                                               
во внешнем (**основном**) запросе для фильтрации, сравнения или                                                              
каким-либо другим образом.                                                              

```postgresql
SELECT *
FROM News
WHERE author_id IN (
	SELECT id
	FROM "User"
	WHERE email LIKE '%yahoo.com'
);
```
Здесь мы получаем список всех новостей только тех пользователей, кто пользуется                                         
почтой от yahoo.com.                                                                 


```postgresql
SELECT id, (
    SELECT COUNT(*)
    FROM News
    WHERE News.author_id = "User".id
) AS news_count
FROM "User";
```
А здесь мы хотим получить таблицу из двух полей: id и какого-то поля,                                                    
в котором будет считаться количество новостей для каждого пользователя                                                  
(мол кто сколько написал)                                                              


**Преимущества и ограничения**                                                             

* **Гибкость**: Вложенные запросы обеспечивают большую гибкость в выборке                                                              
и анализе данных.                                                             
* **Читаемость**: Они могут сделать запросы более читаемыми, разделяя                                                              
сложные операции на более мелкие шаги.                                                             
* **Производительность**: Некоторые вложенные запросы могут быть менее                                                              
эффективными по сравнению с их эквивалентами, использующими JOIN,                                                              
особенно в больших базах данных.                                                             


**Вложенные запросы** — это мощный инструмент в `SQL`, позволяющий решать сложные                                                              
задачи **обработки данных**. Однако их использование требует понимания **влияния**                                                             
на **производительность** и умения **правильно** структурировать запросы для                                                             
достижения нужных результатов.                                                             


Вот так может выглядеть подсчёт кол-ва новостей для пользователей и кол-ва                                              
комментариев для новостей:                                                       

```postgresql
SELECT
	us.id,
	us.first_name,
	us.email,
	r.name AS user_role,
	COUNT(DISTINCT n.id) AS number_of_news,
	COALESCE(SUM(sub.comment_count), 0) AS total_comments,
	n.moderated AS news_moderated
FROM "User" AS us
LEFT JOIN Role as r ON us.role_id = r.id
LEFT JOIN News AS n ON us.id = n.author_id
LEFT JOIN (
	SELECT
		n.id AS news_id,
		COUNT(c.id) AS comment_count
	FROM News AS n
	LEFT JOIN Comment AS c ON n.id = c.news_id
	GROUP BY n.id
) AS sub ON n.id = sub.news_id
GROUP BY us.id, us.first_name, us.email, r.name, n.moderated
ORDER BY number_of_news ASC;
```

В `SQL` запросы обрабатываются с использованием определенной последовательности                                                 
действий, особенно когда они включают подзапросы и соединения (`JOINS`)                                                 

Сначала выполняются подзапросы внутри `LEFT JOIN`. Эти подзапросы агрегируют                                                  
данные (в данном случае, считают комментарии **для каждой новости**).                                                  
Подзапросы работают **независимо** от основного запроса и формируют **временные**                                                 
таблицы с результатами.                                                 

Например, подзапрос внутри `LEFT JOIN` создаст временную таблицу с **количеством**                                                 
**комментариев** для каждой новости.                                                 


Затем `SQL` обрабатывает основной запрос. В этом запросе:                                                 

Сначала формируется "основная" часть запроса, в данном случае, это выборка из                                                 
таблицы "`User`" и соединение (`LEFT JOIN`) с таблицей `Role` для получения                                                  
информации о пользователях и их ролях.                                                 

Затем `SQL` добавляет данные из **временных таблиц**, созданных подзапросами. Это                                                  
делается с помощью `LEFT JOIN` на основе соответствующих условий соединения.                                                  
В этом случае, присоединяются агрегированные данные о комментариях и                                                  
новостях к каждому пользователю.                                                 


Если в запросе присутствуют операторы `GROUP BY` или агрегирующие функции                                                  
(например, `COUNT`), `SQL` затем выполняет эти операции.                                                 

Наконец, `SQL` формирует конечный набор результатов на основе всех предыдущих                                                  
шагов и возвращает его в качестве ответа на запрос.                                                 


---

# **Soft delete**                                                 

Что делать, если клиент хочет, чтобы какие-то данные удалились?                                          
Как поступать, если пользователь удаляет аккаунт в соц сети? Прям удалять его?                                          
А если он через пару недель захочет его восстановить, а данные были стёрты?                                             
Резонно - можно в теории просто вернуться на одно из последних сохранений                                              
базы данных (дамп), где он не был удалён, но что делать, если в том дампе                                               
актуальны другие пользователи, которые наоборот на сегодняшний день выпилили                                             
свою учётную запись, или же обновили свои данные как-то?                                              

Вопросов много и на них на самом деле есть один простой ответ - `soft delete`                                           

`Soft delete` (**мягкое удаление**) - это метод в управлении базами данных, при                                               
котором записи **не удаляются физически** из таблицы. Вместо этого они                                              
**помечаются как удаленные**, что позволяет **сохранить данные** для исторических                                              
или аудитных целей.                                               

Обычно это достигается путем добавления специального столбца (например,                                              
`deleted`, `is_deleted`, `deleted_at`) в таблицу, который указывает,                                               
была ли запись удалена.                                              

**Как Работает Soft Delete?**                                              

1) Добавление Столбца для Метки Удаления:                                              

В таблицу добавляется булевый столбец (например, `deleted` или `is_deleted`) или столбец                                               
с датой (например, `deleted_at`), который будет использоваться для отметки                                               
удаленных записей.                                              

2) Маркировка Записей:                                              

Вместо **физического** удаления записи из таблицы, **устанавливается метка удаления.**                                              
Например, `deleted` устанавливается в `TRUE` или `deleted_at` получает                                               
**временную метку**.                                              


```postgresql
UPDATE "User"
SET deleted = True,
    deleted_at = CURRENT_TIMESTAMP
WHERE id IN (3, 6, 8, 19, 22);
```

3) Изменение Запросов:                                              

Все запросы на выборку (`SELECT`), обновление (`UPDATE`) или удаление                                               
(`DELETE`) должны учитывать статус удаления записей. Например, запросы                                              
`SELECT` должны фильтровать записи, помеченные как удаленные.                                              

```postgresql
SELECT *
FROM "User"
WHERE deleted = False;
```

**Преимущества и Недостатки**                                                      

**Преимущества:**                                                      

* **Аудит и Восстановление**: Удаленные данные могут быть восстановлены                                                      
или проанализированы в будущем.                                                      
* **Безопасность**: Снижается риск случайного или необдуманного удаления                                                      
важных данных.                                                      


**Недостатки:**                                                      

* **Управление Пространством**: Записи остаются в базе данных, что может                                                       
привести к ее разрастанию.                                                      
* **Сложность Запросов**: Необходимо учитывать статус удаления во всех                                                       
запросах, что увеличивает сложность.                                                      
---

# **DATABASE DUMPS**                                                      

Собственно, не редко говорилось в лекции, что нужно делать резервные                                             
копии баз данных, чтобы иметь возможность, если что, откатиться назад.                                                

Но что это и как делать, для чего конкретно нужно?                                                  

    
`Dump` базы данных — это процесс создания **полной копии всех данных** и                                                       
**структур базы данных**. Это, по сути, **снимок** состояния базы данных на                                                      
**определенный момент времени**. Дамп обычно создается в виде серии                                                      
`SQL`-команд, которые воссоздают структуру базы данных (**таблицы**,                                                       
**индексы**, **ограничения**) и заполняют ее данными.                                                      

**Для чего он нужен**                                                      

* **Резервное копирование**: Дампы используются для создания **резервных**                                                      
**копий данных**. В случае сбоев, ошибок или потери данных они позволяют                                                      
**восстановить** базу данных до состояния на момент создания дампа.                                                      

* **Перенос данных**: Дампы помогают переносить базу данных с **одного сервера**                                                      
**на другой**, например, при миграции на новый хостинг или в рамках                                                       
разработки (с продуктивного сервера на тестовый и наоборот).                                                      

* **Архивация**: Для сохранения исторических данных на долгий срок.                                                      

* **Анализ и разработка**: Разработчики могут использовать дампы для                                                       
анализа структуры и данных базы без риска для рабочей базы.                                                      

**Как создать Dump**                                                           

**В MySQL**                                                           
Используйте утилиту `mysqldump` для создания дампа. Базовый синтаксис:                                                           

```commandline
mysqldump -u [username] -p [database_name] > dumpfile.sql
```

**В PostgreSQL**                                                           
Используйте `pg_dump` для создания дампа в `PostgreSQL`:
```commandline
pg_dump -U [user] -h [db host] [db name] > [path to download]
```

Для того, чтобы загрузить данные из дампа в базу, можно заюзать такую                                          
вот команду:                                    

```commandline
psql -U [user] -h [db host] -d [db name] -f [path to dump]
```

**Общие Советы**                                                           

* **Безопасность**: Убедитесь, что дамп базы данных хранится в **безопасном**                                                            
месте, так как он содержит все данные.                                                           
* **Автоматизация**: Рассмотрите возможность настройки **автоматического**                                                            
**создания** дампов для регулярного резервного копирования.                                                           
* **Тестирование восстановления**: После создания дампа всегда полезно                                                           
протестировать процесс восстановления, чтобы убедиться, что                                                           
дамп работает корректно.                                                           
