use db1_book_store;

desc book;
desc cart;
desc member;

select * from book;
select * from cart;
select * from member;

# 정렬 ( ORDER BY )
# 1) 내림차순 정렬 : DESC
# 2) 오름차순 정렬 : ASC(기본 값)

# 1) SELECT
# 2) FROM
# 3) WHERE
# 4) ORDER BY

# [문제] book테이블에서 도서명과 출판일 가져오기
select book_title, book_reg_date from book;

# [조건] 출판일을 기준으로 정렬
SELECT book_publishing_date, book_title FROM book;
SELECT book_publishing_date, book_title FROM book ORDER BY book_publishing_date ASC; # 기본값이 오름차순 이므로 ASC 생략 가능
SELECT book_publishing_date, book_title FROM book ORDER BY book_publishing_date DESC;

# [문제] book테이블에서 도서명에 '자바'가 들어가는 도서 가져오기
select * from book where book_title like '%자바%';
# [조건] 도서명을 기준으로 정렬
select * from book order by book_title;
select * from book order by book_title DESC;