# 15&16_Workshop

![1548139082573](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548139111617.png)

### 1. DB 테이블 생성하고 Data 입력하기

```sqlite
CREATE TABLE bands (id INTEGER, name TEXT, debut INTEGER);
INSERT INTO bands (id, name, debut)
VALUES (1, 'Queen', 1973);
INSERT INTO bands (id, name, debut)
VALUES (2, 'Coldplay', 1998);
INSERT INTO bands (id, name, debut)
VALUES (3, 'MCR', 2001);
```

### 2.  bands 테이블에서 모든 레코드의 id와 name만 조회하는 Query 를 작성하라.

```sqlite
SELECT id, name FROM bands;
```

### 3. bands 테이블에서 debut가 2000보다 작은 밴드들의 이름만을 조회하는 Query를 작성하라.

```sqlite
SELECT name FROM bands WHERE debut < 2000;
```

### 4. 테이블을 수정하여 column을 추가하고 데이터를 삽입해라.

![1548205429599](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548205429599.png)

```sqlite
ALTER TABLE bands
ADD COLUMN members INTEGER;

UPDATE bands
SET members=4 WHERE id=1;

UPDATE bands
SET members=5 WHERE id=2;

UPDATE bands
SET members=9 WHERE id=3;
```



### 5. id가 3인 레코드의 members를 5로 수정하라.

```sqlite
UPDATE bands
SET members=5 WHERE id=3;
```

### 6. id가 2인 레코드를 삭제하라.

```sqlite
DELETE FROM bands
WHERE id=2;
```



