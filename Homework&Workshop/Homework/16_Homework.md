# 16_Homework

### 1.  다음과 같은 스키마를 가진 DB 테이블 friends를 작성한다.

![1548206314448](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548206314448.png)

```sqlite
CREATE TABLE friends (id INTEGER, name TEXT, location TEXT);
```

### 2. 해당 테이블에 다음과 같이 데이터를 입력한다.

![1548206804848](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548206804848.png)

```sqlite
INSERT INTO friends(id, name, location)
VALUES (1, 'Justin', 'Seoul'), (2, 'Simon', 'New York'), (3, 'Chag', 'Las Vegas'), (4, 'John', 'Sydney');
```

### 3. 데이터를 다음과 같이 추가한다.

![1548206779730](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548206779730.png)

```sqlite
ALTER TABLE friends
ADD COLUMN married INTEGER;

UPDATE friends
SET married=1 WHERE id IN (1, 4);

UPDATE friends
SET married=0 WHERE id IN (2, 3);
```

### 4. married가 0인 데이터를 모두 삭제한다.

```sqlite
DELETE FROM friends WHERE married=0;
```

### 5. 테이블을 삭제한다.

```sqlite
DROP TABLE friends;
```



