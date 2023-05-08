USE db1_book_store;

SELECT * FROM cart;

/*
	GROUP BY
	그룹 함수와 함께 사용한다.
	GROUP BY 될 때에 내부적으로 임시 테이블을 만든다.
	이때 임시 테이블의 칼럼은 GROUP BY에 작성한 컬럼과
	SELECT에서 사용한 그룹 함수가 된다.
    내부 데이터의 종류에 맞춰서 임시 테이블을 만들고
    그 종류에 맞춰서 결과값을 도출 가능
    
    ★ 새로운 배열을 만들 때에는 GROUP BY
    ★ 원본 배열의 조건을 넣을 때에는 WHERE
    ★ 새로운 배열의 조건을 넣을 때에는 HAVING

	JOIN
    테이블이 여러개 사용될 때
*/


# [문제] member테이블에서 회원의 수를 성별로 가져오기
SELECT member_gender, COUNT(*) 
FROM member
GROUP BY member_gender;

# [문제] book테이블에서 도서 종류별 도서 수량 가져오기
SELECT book_kind, COUNT(*)
FROM book
GROUP BY book_kind;


# [문제] cart테이블에서 회원별로 구입한 총 수량 가져오기
SELECT buyer, SUM(buy_count) 
FROM cart 
GROUP BY buyer
# [조건] 총수량을 기준으로 한 내림차순 정렬하기
ORDER BY SUM(buy_count) DESC;


# [문제] cart테이블에서 회원이 구입한 도서의 수량이 2개 이상인 회원의 id 가져오기
# [조건] 두개이상인 경우만 출력
SELECT buyer, SUM(buy_count) 
FROM cart 
GROUP BY buyer 
HAVING SUM(buy_count) >= 2;

# [문제] book테이블에서 2015년에서 2019년 사이에 출간한 도서 중에
# 재고 수량이 3개 이하인 도서를 종류별 개수 가져오기
SELECT book_kind, COUNT(*)
FROM book
WHERE '2015-01-01' <= book_publishing_date AND book_publishing_date < '2020-01-01' AND book_count <= 3
GROUP BY book_kind;


