USE db1_book_store;

DESC cart;
DESC memeber;
DESC book;

SELECT * FROM cart;
SELECT * FROM member;
SELECT * FROM book;

# [문제] book테이블에서 책 제목에 'java'가 포함되어 있는 책정보 가져오기
-- ★ MySQL은 기본적으로 대소문자 구별을 하지 않는다.
select * from book where book_title like '%java%';

# [문제] book테이블에서 책 제목에 'java' 또는 '자바' 가 포함되어 있는 책정보 가져오기
select * from book where book_title like '%자바%' or book_title like '%java%';

# [문제] book테이블에서 책 제목이 '나'로 시작되는 책정보 가져오기
select * from book where book_title like '나%';

# [문제] book테이블에서 책 제목이 '외국어'로 끝나는 책정보 가져오기
select * from book where book_title like '%외국어';

# [문제] member테이블에서 이름이 4글자인 회원정보 가져오기
select * from member where member_name like '____';