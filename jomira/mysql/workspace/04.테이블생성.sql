# 데이터 베이스 생성하기
create database db1_book_store;

# 데이터 베이스 사용하기
USE db1_book_store;

#-----------------------------------
# 회원정보 테이블 셋팅하기
CREATE TABLE member (
	member_no INT,
    member_id VARCHAR(20),
    member_pw VARCHAR(20),
    member_name VARCHAR(20),
    member_gender VARCHAR(1),
    member_point INT,
    member_reg_date DATETIME
);

# 회원정보 테이블 전체 삭제하기
-- DROP TABLE member

# 전체 구조 확인
DESC member;

#--------------------------------------

# 책 정보 테이블 생성하기
CREATE TABLE book(
	book_no INT,
    book_kind VARCHAR(3),
    book_title VARCHAR(100),
    book_price INT,
    book_count INT,
    book_author VARCHAR(40),
    book_publishing_com VARCHAR(30),
    book_publishing_date VARCHAR(15),
    book_image VARCHAR(16),
    book_content VARCHAR(500),
    book_discount_rate INT,
    book_reg_date DATETIME
);

# 책 정보 테이블 삭제하기
-- DROP TABLE book;

DESC book;


#----------------------------------------------------------

# 장바구니 테이블 생성하기
CREATE TABLE cart(
	cart_no INT,
    buyer VARCHAR(50),
    buy_price INT,
    buy_count INT,
    book_no INT,
    book_title VARCHAR(100),
    book_image VARCHAR(16)
);

# 장바구니 테이블 삭제하기
-- DROP TABLE cart;

# 장바구니 테이블 전체 구조 확인하기
DESC cart;


