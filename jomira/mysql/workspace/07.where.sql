USE db1_book_store;

DESC member;
DESC book;
DESC cart;

select * from book;

# [문제] member테이블에서 id가 qwer인 회원의 이름과 비밀번호 가져오기
select * from member where member_id='qwer';

# [문제] book테이블에서 book_kind가 문학(100)인 책정보 가져오기
select * from book where book_kind='100';

# [문제] book테이블에서 가격이 15,000원 이하인 책정보 가져오기
select * from book where book_price <= 15000;

# [문제] book테이블에서 문학(100)이 아닌 책정보만 가져오기
select * from book where book_kind != '100';

# [문제] book테이블에서 2020년 이전에 등록된 책정보만 가져오기
select * from book where book_reg_date < '2022-01-01';

# [문제] book테이블에서 컴퓨터(300)이면서 가격이 15,000원 이상인 책정보 가져오기
select * from book where book_kind = '300' and book_price >= 15000;

# [문제] book테이블에서 재고가 없는 책정보 가져오기
select * from book where book_count = 0;

# [문제] book테이블에서 문학(100)이거나 컴퓨터(300)인 책정보 가져오기
select * from book where book_kind = 100 or book_kind = 300;

# [문제] book테이블에서 할인률이 없는 책정보 가져오기
select * from book where book_discount_rate = '0';

# [문제] book테이블에서 할인률이 있는 책정보 가져오기 - 두가지 방법 
select * from book where book_discount_rate != '0'; # 첫번째
select * from book where NOT book_discount_rate = '0'; # 두번째