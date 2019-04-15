## SQL

## SQLite3 전용 명령어

| 명령어                             | 설명                                        |
| ---------------------------------- | ------------------------------------------- |
| `.mode csv`                        | csv 모드                                    |
| `.mode column`                     | 컬럼 모드                                   |
| `.headers on`                      | 헤더(컬럼이름) 같이 출력                    |
| `.read <file.sql>`                 | 해당 sql 스크립트 실행                      |
| `.import <file.name> <tabel_name>` | 해당 파일의 데이터를 지정한 테이블에 import |
| `.schema`                          | 스키마 전체 보기                            |



## TABLE 조작 관련

### Table 생성

```sql
CREATE TABLE <table_name> (
	<col> DATA_TYPE PRIMARY KEY AUTOINCREMENT,
    <col> DATA_TYPE NOT NULL,
    <col> DATA_TYPE DEFAULT <value>,
    ...
);
```

### Table ( + 레코드 모두) 삭제

```sql
DROP TABLE <table_name>;
```

### Table 이름 수정

```plsql
ALTER TABLE <table_name>
RENAME TO <new_table_name>;
```

### Table 컬럼 추가

```sql
ALTER TABLE <table_name>
ADD COLUMN <new_col_name> DATATYPE;
```



## Data 조작 관련

### Data 생성 (Create)

```sql
INSERT INTO <table_name> (<col_name_1>, <col_name_2>, ...)
VALUES
(<value_1>, <value_2>, ...),
(<value_1>, <value_2>, ...),
...
(<value_1>, <value_2>, ...);

```

### Data 조회 (Read, Retrieve)

#### 테이블에서 데이터 전체를 모든 col 에 대하여 조회

```sql
SELECT * FROM <table_name>;
```

#### 테이블에서 특정 컬럼만 조회

```sql
SELECT <col_1>, <col_2>, ... FROM <table_name>;
```

#### 특정 조건으로 전체 컬럼 조회

```sql
SELECT * FROM <table_name> WHERE [condition];
```

### Data 수정 (Update)

```sql
UPDATE <table_name>
SET <col_1>=<val_1>, <col_2>=<val_2>, ...
WHERE [condition]; -- 보통 primary key (id) 로 선택
```

### Data 삭제 (Delete, Destroy)

```sql
DELETE FROM <table_name>
WHERE [condtion]; -- 보통 primary key (id) 로 선택
```



## Expression

### 해당 컬럼의 갯수

```sql
SELECT COUNT(<col>) FROM <table_name>;
```

### 해당 컬럼의 

```sql
-- 평균
SELECT AVG(<col>) FROM <table_name>;
-- 총합
SELECT SUM(<col>) FROM <table_name>
-- 최소
SELECT MIN(<col>) FROM <table_name>
-- 최대
SELECT MAX(<col>) FROM <table_name>
```

### 정렬(order)

```sql
SELECT <col> FROM <table_name>
ORDER BY <col_1>, <col_2> [ASC | DESC];
```

### 제한(Limit)

```sql
SELECT <col> FROM <table_name>
LIMIT <num>
```

### 패턴(Pattern)

```sql
SELECT * FROM <table_name>
WHERE <col> LIKE '<pattern>'
```

| 시작 | 예시    | 설명                                 |
| ---- | ------- | ------------------------------------ |
| `%`  | `2%`    | 2로 시작하는 값                      |
|      | `%2`    | 2로 끝나는 값                        |
|      | `%2%`   | 2가 들어가는 값                      |
| `_`  | `_2`    | 두번쨰 글자가 2 인 값                |
|      | `1___`  | 1로 시작하며 4자리                   |
|      | `_2%`   | 한글자 뒤에 2가오고 뒤에 이어지는 값 |
|      | `2_%_%` | 2로 시작하는데 최소 3자리인 값       |





## Ⅰ. SQL

```sql
CREATE TABLE awards (
	id INTEGER PRIMARY KEY,
	recipient TEXT NOT NULL,
	award_name TEXT DEFAULT 'Grammy'
);
```

```sql
SELECT * FROM movies WHERE year BETWEEN 1970 AND 1979;
```

```sql
SELECT *
FROM movies
WHERE year < 1985 AND genre="horror";
```

```sql
SELECT *
FROM movies
WHERE genre = "comedy"
   OR genre = 'romance';
```

```sql
SELECT name,
CASE
WHEN genre="romance" THEN "Chill"
WHEN genre="comedy" THEN "Chill"
ELSE "Intense"
END AS "Mood"
FROM movies;
```

```sql
SELECT DISTINCT year
FROM movies;
```

```sql
SELECT imdb_rating AS 'IMDb'
FROM movies;
```

```sql
SELECT category, price, AVG(downloads)
FROM fake_apps
GROUP BY 1,2;
```

```sql
SELECT price, ROUND(AVG(downloads)), COUNT(*)
FROM fake_apps
GROUP BY price
HAVING COUNT(*) > 10;
```

```sql
SELECT ROUND(AVG(price),2)
FROM fake_apps;
```

```sql
SELECT orders.order_id,
   customers.customer_name
FROM orders
JOIN customers
  ON orders.customer_id = customers.customer_id; 
```

```sql
SELECT *
FROM newspaper
LEFT JOIN online
ON newspaper.id = online.id
WHERE online.id IS NULL;
```

```sql
SELECT month, COUNT(*)
FROM newspaper
CROSS JOIN months
WHERE start_month <= month and end_month >= month
GROUP BY month;
```

```sql
SELECT * FROM newspaper UNION SELECT * FROM online;
```

```sql
WITH previous_query AS (
SELECT customer_id,
   COUNT(subscription_id) AS 'subscriptions'
FROM orders
GROUP BY customer_id
)
SELECT customers.customer_name, previous_query.subscriptions
FROM previous_query
JOIN customers
ON previous_query.customer_id = customers.customer_id;

```

## 



# One to Many

### Writer

| id      | name      |
| ------- | --------- |
| PK, INT | CharField |

### Book

| id      | author          | title     | description |
| ------- | --------------- | --------- | ----------- |
| PK, INT | FK, Writer, INT | CharField | TextField   |

##



### Chapter

| id      | book_id       | title     | description |
| ------- | ------------- | --------- | ----------- |
| PK, INT | FK, Book, INT | CharField | TextField   |

