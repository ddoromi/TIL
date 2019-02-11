# 19. 01. 22 Summary

## Database

### RDBMS :  관계형 데이터베이스 관리 시스템

#### 1. SQLite 

* 파일 하나만 존재, 서버가 아니라 응용 프로그램에 넣어 비교적 가벼운 데이터베이스

#### 2. 용어 정리

* 모델링 & 스키마 : 자료의 구조, 표현 방법 등을 정함. => 확정 시 스키마로 부름.
* 테이블 이름은 복수로 정하기

* 데이터 레코드 : 테이블에서 행 하나

* 데이터가 저장되는 순간에 고유 번호가 자동 할당 되어야 함.

#### 3. 명령어

* SQL 

  | .mode csv                        |       csv 처럼 보임       |
  | -------------------------------- | :-----------------------: |
  | .mode column                     |    컬럼 기준으로 보임     |
  | .headers on                      | 헤더(컬럼 이름) 같이 출력 |
  | .read <file.sql>                 |  해당 sql 스크립트 실행   |
  | .import <file_name> <table_name> |     table에 file 추가     |
  | .nullvalue 'NULL'                |                           |

* TABLE

  * ```CREATE TABLE <table_name> (<스키마>);``` => table_name의  table  생성

  * ```DROP <table_name>```=> table을 없애는 명령어

  * ```INSERT INTO <table_name> (<스키마의 자료형>) ```

    ```VALUES (<스키마에 넣을 데이터>);``` => 데이터 추가

    ```sqlite
    ALTER TABLE <table_name>
    RENAME to <new_table_name>
    ```

  * column 추가

    ```sqlite
    ALTER TABLE <table_name>
    ADD COLUMN <new_col_name> <type> (DEFAULT <value>);
    ```

    

* Data 조작 관련

  * Data 생성(Create)

    ```sqlite
    INSERT INTO <table_name> (<col_name_1>, <col_name_2>)...);
    VALUES (<value_1>, <value_2> ...);
    ```

  * Data 조회(Read, Retrieve)

    * 테이블에서 데이터 전체를 모든 col에 대하여 조회

    ```sqlite
    SELECT * FROM <table_name>;
    ```

    * 테이블에서 특정 컬럼만 조회

    ```sqlite
    SELECT <col_1> <col_2> .. FROM <table_mode>
    ```

    * 특정 조건으로 전체 컬럼 조회

    ```sqlite
    SELECT * FROM <table_name> WHERE <조건>
    ```

  * Data 수정(Update)

    ```sqlite
    UPDATE <table_name>
    SET <col_1>=<val_1>, <col_2>=<val_2>
    WHERE [condition] -- 보통 primary key (id)로 선택
    ```

  * Data 삭제(Delete, Destroy)

    ```sqlite
    DELETE FROM <table_name>
    WHERE [condition]; -- 보통 primary key (id)로 선택
    ```

* Expression

  * 해당 컬럼의 갯수

    ```sqlite
    SELECT COUNT(<col>) FROM <table_name>;
    ```

  * 평균, 총합, 최소, 최대

    ```sqlite
    SELECT AVG(<col>) FROM <table_name>
    SELECT SUM(<col>) FROM <table_name>
    SELECT MIN(<col>) FROM <table_name>
    SELECT MAX(<col>) FROM <table_name>
    ```

* 정렬(order)

  ```sqlite
  SELECT <col> FROM <table_name>
  ORDER BY <col_1>, <col_2> [ASC(오름차순) | DESC(내림차순)];
  ```

* 제한(limit)

  ```sqlite
  SELECT <col> FROM <table_name>
  LIMIT <num>
  ```

* 패턴(pattern)

  ```sqlite
  SELECT * FROM <table_name> WHERE <col> LIKE '<patten>'
  ```

  | 시작 | 예시    | 설명                           |
  | ---- | ------- | ------------------------------ |
  | %    | 2%      | 2로 시작하는 값                |
  |      | %2      | 2로 끝나는 값                  |
  |      | %2%     | 2가 들어가는 값                |
  | _    | _2      | 두번째 글자가 2인 값           |
  |      | 1____   | 1로 시작하며 4자리             |
  |      | _2%     | 두번째에 2가 오고              |
  |      | `2_%_%` | 2로 시작하는데 최소 3자리인 값 |

  