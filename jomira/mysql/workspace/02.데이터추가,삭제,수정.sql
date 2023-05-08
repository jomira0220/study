USE sample;

select * from sample41;
desc sample41;

insert into sample41 (no,a,b) values(1,'ABC','2022-02-01');
insert into sample41 (a,no,b) values('XYZ',2,'2022-02-01');
insert into sample41 VALUES(3,'SDK','2022-02-08');

-- 전체 데이터 삭제 --
TRUNCATE sample41;

-- 특정 행의 데이터만 삭제 : 뒤에 행의 번호 입력 -- 
delete from sample41 where no=3;

-- 데이터 수정하기 : 수정하려는 행의 번호를 뒤에 입력 --
update sample41 set b='2022-03-01' where no=2;
-- 데이터 수정하기 : 수정하려는 열의 이름(타이틀)과 변경 규칙을 뒤에 입력 --
update sample41 set no=no+1;
update sample41 set a='xxx', b='1991-02-21' where no=2;
