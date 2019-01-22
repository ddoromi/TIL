# 15_Workshop

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

