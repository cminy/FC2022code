from mysql.connector import Error
import mysql.connector
import pymysql
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


db = mysql.connector.connect(
    host="127.0.0.1", port=3306, user="root", passwd="mk246900", auth_plugin='mysql_native_password', db="world", charset="utf8")
curs = db.cursor()


qr = "DESC city;"
pd.read_sql(qr, db)


# --------- 7p

qr = "CREATE DATABASE IF NOT EXISTS testdb;"
curs.execute(qr)

qr = "show databases;"
pd.read_sql(qr, db)
qr = "DROP database IF EXISTS test;"
curs.execute(qr)

qr = "show databases;"
pd.read_sql(qr, db)

qr = "USE testdb;"
curs.execute(qr)
qr = "SELECT DATABASE()"
pd.read_sql(qr, db)

qr = '''
CREATE TABLE IF NOT EXISTS user1(
user_id INT,
name Varchar(20),
email Varchar(30),
age INT(3),
rdate DATE
)
'''
curs.execute(qr)

qr = """CREATE TABLE IF NOT EXISTS user2(
user_id INT PRIMARY KEY AUTO_INCREMENT,
name Varchar(20) NOT NULL,
email Varchar(30) UNIQUE NOT NULL,
age INT(3) DEFAULT '30',
rdate TIMESTAMP
)"""
curs.execute(qr)

qr = "show tables"
pd.read_sql(qr, db)

# - ALTER TABLE은 if not exists 를 지원하지 않는다
qr = "alter table user2 add tmp TEXT;"
curs.execute(qr)

qr = "ALTER TABLE user2 MODIFY COLUMN tmp INT;"
curs.execute(qr)

qr = "show full columns from user2;"
pd.read_sql(qr, db)

qr = "ALTER TABLE user2 CONVERT TO character set utf8;"
curs.execute(qr)

qr = """INSERT INTO user1(user_id, name, email, age, rdate)
VALUES (1, "jin", "pdj@gmail.com", 30, now()),
(2, "peter", "peter@daum.net", 33, '2017-02-20'),
(3, "alice", "alice@naver.com", 23, '2018-01-05'),
(4, "po", "po@gmail.com", 43, '2002-09-16'),
(5, "andy", "andy@gmail.com", 17, '2016-04-28'),
(6, "jin", "jin1224@gmail.com", 33, '2013-09-02');"""
curs.execute(qr)
qr = "select * from user1;"
pd.read_sql(qr, db)

qr = """INSERT INTO user2(user_id, name, email, age, rdate)
VALUES (1, "jin", "pdj@gmail.com", 30, now()),
(2, "peter", "peter@daum.net", 33, '2017-02-20'),
(3, "alice", "alice@naver.com", 23, '2018-01-05'),
(4, "po", "po@gmail.com", 43, '2002-09-16'),
(5, "andy", "andy@gmail.com", 17, '2016-04-28'),
(6, "jin", "jin1224@gmail.com", 33, '2013-09-02');"""
curs.execute(qr)

qr = """INSERT INTO user1
SELECT user_id, name, email, age, rdate
FROM user2
WHERE age > 30;
"""
curs.execute(qr)

qr = '''UPDATE user1
SET age=20, email="pdj@daum.net"
WHERE name="jin"'''
curs.execute(qr)

qr = '''delete from user1
where rdate < "2016-01-01"'''
curs.execute(qr)

qr = "TRUNCATE from user1;"
curs.execute(qr)

qr = "DROP FROM user1;"
curs.execute(qr)

qr = '''create table user(
user_id int primary key auto_increment,
name varchar(20),
addr varchar(20)
);'''
curs.execute(qr)

qr = '''create table money(
money_id int primary key auto_increment,
income int,
user_id int,
# 외래키 설정
FOREIGN KEY (user_id) REFERENCES user(user_id)
);'''
curs.execute(qr)

qr = "desc money;"
pd.read_sql(qr, db)

qr = '''alter table money
add constraint fk_user
foreign key (user_id)
references user (user_id);'''
curs.execute(qr)

qr = "desc money;"
pd.read_sql(qr, db)

qr = '''insert into user(name, addr)
values ("jin", "Seoul"), ("andy", "Pusan");
insert into money(income, user_id)
values (5000, 1), (7000, 2);'''
curs.execute(qr)

qr = "select * from user;"
pd.read_sql(qr, db)

qr = "select * from money;"
pd.read_sql(qr, db)

# --- 19p
# world 데이터 베이스에서 countrylanguage 테이블에 있는 언어의 종류가 몇가지 인지 출력
qr = "use world;"
curs.execute(qr)
qr = "desc countrylanguage;"
pd.read_sql(qr, db)
pd.read_sql('select*from countrylanguage;', db)
qr = '''select count(distinct(language)) as uniq_lang
from countrylanguage;'''
pd.read_sql(qr, db)

# --- 20p
# 도시의 인구가 100만이 넘으면 "big city" 그렇지 않으면 "small city"를 출력하는 city_scale 컬럼을 추가
qr = '''select name, population, if(population >= 100*10000, "big city", "small city") as city_scale
from city;'''
an = pd.read_sql(qr, db)
an.head(10)
# 독립년도가 없는 데이터 0 출력
qr = '''select indepyear, ifnull(indepyear,0) as indepyear
from country;'''
an = pd.read_sql(qr, db)
an.head(10)
# 나라별로 인구가 10억 이상, 1억 이상, 1억 이하인 컬럼 추가
qr = '''
    SELECT name, population,
        CASE
            WHEN population > 1000000000 THEN "upper 1 bilion"
            WHEN population > 100000000 THEN "upper 100 milion"
            ELSE "below 100 milion"
        END AS result
    FROM country
    order by result desc;'''
an = pd.read_sql(qr, db)
an.head(10)

# 21p
qr = '''SELECT CountryCode, COUNT(CountryCode)
FROM city
GROUP BY CountryCode;'''
an = pd.read_sql(qr, db)
an.head(10)

qr = """SELECT COUNT(DISTINCT(Language)) as language_count
FROM countrylanguage;"""
an = pd.read_sql(qr, db)
an.head()

qr = '''SELECT continent, MAX(Population) as Population_max, MAX(GNP) as GNP_max
FROM country
GROUP BY continent;'''
an = pd.read_sql(qr, db)
an

# --- 22p
# 대륙별 인구수와 GNP 최소 값을 조회 (GNP와 인구수가 0이 아닌 데이터 중에서)
qr = '''
select continent, min(population) as population_min, min(gnp) as gnp_min
from country
where (gnp != 0) and (population!=0)
group by continent;'''
an = pd.read_sql(qr, db)
an

# 대륙별 평균 인구수와 평균 GNP 결과를 인구수로 내림차순 정렬
qr = '''SELECT continent, AVG(Population) as Population, AVG(GNP) as GNP
FROM country
WHERE GNP != 0 AND Population != 0
GROUP BY continent
ORDER BY Population DESC;'''
an = pd.read_sql(qr, db)
an

# sakila의 payment 테이블에서 스태프별 총 수입을 출력하여 어떤 스태프가 더 많은 매출을 올렸는지 출력
qr = 'use sakila;'
curs.execute(qr)
qr = "show tables"
pd.read_sql(qr, db)
qr = "desc payment;"
pd.read_sql(qr, db)
qr = "select * from payment;"
an = pd.read_sql(qr, db)
an.head(3)
qr = "desc staff;"
pd.read_sql(qr, db)
qr = '''
select staff_id, sum(amount) as amount
from payment
group by staff_id;
'''
an = pd.read_sql(qr, db)
an

# --- 23p
qr = "use world;"
curs.execute(qr)
# 대륙별 전체인구를 구하고 5억이상인 대륙만 조회
qr = '''SELECT continent, SUM(Population) as Population
FROM country
GROUP BY continent
HAVING Population > 500000000;'''
an = pd.read_sql(qr, db)
an
# 대륙별 평균 인구수, 평균 GNP, 1인당 GNP한 결과를 1인당 GNP가 0.01 이상인 데이터를 조회하고 1인당 GNP를 내림차순으로 정렬
qr = '''
select continent, avg(population) as population_avg, avg(gnp) as gnp_avg, (AVG(GNP) / AVG(Population) * 1000) as AVG
from country
where GNP != 0 AND Population != 0
GROUP BY continent
HAVING AVG > 0.01
ORDER BY AVG DESC;
'''
an = pd.read_sql(qr, db)
an

qr = "use sakila;"
curs.execute(qr)
qr = '''SELECT customer_id, staff_id, SUM(amount) as amount
FROM payment
GROUP BY customer_id, staff_id
WITH ROLLUP;'''
an = pd.read_sql(qr, db)
an

# --- 24p
# world 데이터 베이스의 country 테이블에서 대륙별 지역별 전체 인구수와 대륙에 대한 전체 인구수를 출력
qr = 'use world;'
curs.execute(qr)
qr = 'desc country'
pd.read_sql(qr, db)
qr = '''
select continent, region, sum(population) as total_population
from country
group by continent, region
with rollup;
'''
an = pd.read_sql(qr, db)
an

# 퀴즈 준비
qr = """
  create table user1(
    user_id int primary key auto_increment,
    name varchar(20)
  )
"""
qr = """
  create table addr1(
    user_id int,
    addr_name varchar(20)
  )
"""
result = curs.execute(qr)


QUERY = '''
 insert into user1(name)
 values ("a"),("b"),("c")
'''
curs.execute(QUERY)

QUERY = """
    INSERT INTO addr1(user_id, addr_name)
    VALUES (1, "S"), (2, "P"), (4, "I"), (5, "S")
"""
result = curs.execute(QUERY)

qr = "select*from user1"
pd.read_sql(qr, db)

qr = "select*from addr1"
pd.read_sql(qr, db)

# INNER JOIN
QUERY = """
    SELECT user1.user_id, user1.name, addr1.addr_name
    FROM user1
    JOIN addr1
    ON user1.user_id = addr1.user_id
"""
pd.read_sql(QUERY, db)

QUERY = """
    SELECT user1.user_id, user1.name, addr1.addr_name
    FROM addr1
    JOIN user1
    ON user1.user_id = addr1.user_id
"""
pd.read_sql(QUERY, db)

# LEFT join
QUERY = """
    SELECT user1.user_id, user1.name, addr1.addr_name
    FROM user1
    LEFT JOIN addr1
    ON user1.user_id = addr1.user_id
"""
pd.read_sql(QUERY, db)

# RIGHT JOIN
QUERY = """
    SELECT addr1.user_id, user1.name, addr1.addr_name
    FROM user1
    RIGHT JOIN addr1
    ON user1.user_id = addr1.user_id
"""
pd.read_sql(QUERY, db)


# FIN.
