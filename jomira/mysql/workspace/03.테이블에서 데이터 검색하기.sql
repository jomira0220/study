# 주석의 종류 : 한줄주석 # 또는 --
/*
두줄 주석은 이렇게!
*/

USE sample;
show tables;

select * from sample21; # 데이블안의 모든 데이터 확인

-- [문제] no열과 name열 값만 읽어오기
select no,name from sample21; # 데이블안의 특정 열만 데이터 확인은 열의 이름

-- [문제] no열 값이 2인 행만 추출
SELECT * FROM sample21 WHERE no = 2;

-- [문제] no열 값이 2가 아닌 행의 no열과 name열 값만 읽어오기
select no,name from sample21 where no <> 2; # 2행만 빼고 데이터 확인 

-- [문제] name열 값이 '박준용'인 행만 추출
SELECT * FROM sample21 WHERE name='박준용';

desc sample21;


-- ▼논리 연산자 사용하기 --
SELECT * FROM sample24;

-- [문제] a열과 b열이 모두 0이 아닌 행 검색
SELECT * FROM sample24 WHERE a <> 0 AND b <> 0;

-- [문제] a열이 0이 아니거나 b열이 0이 아닌 행을 검색
SELECT * FROM sample24 WHERE a <> 0 OR b<> 0;

-- [문제] a열이 0이 아니거나 b열이 0이 아닌 행을 제외한 나머지 행을 검색
SELECT * FROM sample24 WHERE NOT(a <> 0 OR b <> 0);

-- (4) AND는 OR에 비해 우선 순위가 높다!
-- [문제] a열이 1또는 2이고, b열이 1 또는 2인 행을 검색
SELECT * FROM sample24 WHERE a=1 OR a=2 AND b=1 OR b=2;			  -- 잘못된 명령문
SELECT * FROM sample24 WHERE a=1 OR (a=2 AND b=1) OR b=2;			-- 위 문장은 이와 같이 실행되고 있다.
SELECT * FROM sample24 WHERE (a=1 OR a=2) AND (b=1 OR b=2);		-- 올바른 명령문


-- ▼ 부분 검색 사용하기 --
select * from sample25;

-- [문제] text 열이 'SQL'로 시작하는 행을 검색(=전방 일치)
select * from sample25 where text LIKE 'SQL%';

-- [문제] text 열이 'SQL'을 포함하는 행을 검색(= 중간 일치)
SELECT * FROM sample25 WHERE text LIKE '%SQL%';

-- [문제] text 열이 'SQL'로 끝나는 행을 검색(= 후방 일치)
-- 현재 25테이블에 뒤에 SQL이 오는것이 없으므로 아무것도 검색되지 않음
SELECT * FROM sample25 WHERE text LIKE '%SQL';


-- [문제] text열에 %를 포함하는 행을 검색
-- 첫번째와 마지막 %는 메타문자(=임의의 문자열)
-- \%는 % 그 자체 문자
SELECT * FROM sample25 WHERE text LIKE '%\%%';

-- [문제] text열에 _를 포함하는 행을 검색
SELECT * FROM sample25 WHERE text LIKE '%\_%';
