-- 한 줄 명령어 실행 : Ctrl + Enter --
CREATE DATABASE sample;

SHOW TABLES;

-- DB 사용하기 --
USE sample;

-- 테이블 생성
CREATE TABLE sample21(
	-- 순서 : 변수명 + 타입
	no INT(11),
    name VARCHAR(20),
	birthday DATE,
    address VARCHAR(40)
);

CREATE TABLE sample24(
	no INT(11),
    a INT(11),
    b INT(11),
    c INT(11)
);

CREATE TABLE sample25(
	no INT(11),
    text VARCHAR(100)
);

CREATE TABLE sample41(
	no INT(11),
    a VARCHAR(30),
    b DATE
);

-- 테이블 삭제하기 -- 
DROP TABLE sample41;

-- 테이블 안에 데이터 추가하기
DESC sample21;

-- 테이블 안의 데이터 삭제하기 --
DELETE FROM sample21 WHERE no=2; 

-- 데이터 추가하기 --
INSERT INTO sample21 VALUES(1, '박준용', '1976-10-18', '대구광역시 수성구');
INSERT INTO sample21 VALUES(2, '김재진', '1987-02-14', '대구광역시 동구');
INSERT INTO sample21 VALUES(3, '홍길동', '1990-04-28', '서울시 송파구');
select * from sample21;

INSERT INTO sample24 VALUES(1, 1, 0, 0);
INSERT INTO sample24 VALUES(2, 0, 1, 0);
INSERT INTO sample24 VALUES(3, 0, 0, 1);
INSERT INTO sample24 VALUES(4, 2, 2, 0);
INSERT INTO sample24 VALUES(5, 0, 2, 2);
select * from sample24;

INSERT INTO sample25 VALUES(1, 'SQL은 RDBMS를 조작하기 위한 언어이다.');
INSERT INTO sample25 VALUES(2, 'LIKE에서는 메타문자 %와 _를 사용할 수 있다.');
INSERT INTO sample25 VALUES(3, 'LIKE는 SQL에서 사용할 수 있는 술어 중 하나이다.');
select * from sample25;


