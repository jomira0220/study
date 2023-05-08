use db1_book_store;

select * from memeber;
select * from cart;
select * from book;


# 숫자 함수
# ABS()			절대값
# CEIL()		소수점 올림
# FLOOR()		소수점 버림
# ROUND()		소수점 반올림(자리수 지정 가능)
# TRUNCATE()	소수점 버림(자리수 지정 가능)
# POW()			x의 y제곱근 계산값
# MOD()			나눈 나머지
# GREATEST()	max
# LEAST()		min

select abs(100), abs(-100);

select ceil(1.5);

select floor(1.5);

select round(1.5), round(1.355,2); # 원하는 자리수에서 5이상이면 올림
SELECT ROUND(3.14356, 0), ROUND(3.51234, 0);			# 소수점 이하 0자리
SELECT ROUND(3.14356, 1), ROUND(3.55234, 1);			# 소수점 이하 1자리
SELECT ROUND(13.14356, -1), ROUND(15.55234, -1);		# 1의 자리

select truncate(1.3521,2), truncate(1.822,0); # 뒤에 입력하는 자리수까지만 보이도록
SELECT TRUNCATE(3.14356, 0), TRUNCATE(3.51234, 0);		# 소수점 이하 0자리
SELECT TRUNCATE(3.14356, 1), TRUNCATE(3.55234, 1);		# 소수점 이하 1자리
SELECT TRUNCATE(13.14356, -1), TRUNCATE(15.55234, -1);	# 1의 자리

select pow(10,3);
select mod(10,3);

select greatest(10,3,5,4,7,6,2);
select least(10,3,5,4,7,6,2);

#----------------------------------------------------------------------------
# 문자열 함수
# ★ [주의] 자바와 달리 인덱스가 1부터 시작함 ★

# CONCAT() : 문자열 이어붙이기
# INSERT() : 문자열 추가 및 삭제
# REPLACE() : 문자열 교체
# INSTR() : 특정문자열 위치 탐색

select concat('aaa','bbb','ccc');
# INSERT() : 앞 문장의 2번째부터 3개를 삭제한 후, 삽입
select insert('abcde',2,3,'bbb'); # abbbe
# 2번째 순서부터 추가할 문장(뒷 문장)의 처음부터 끝까지 추가삽입
select insert('abcde',2,0,'bbb'); # abbbbcde 
# 원하는 문제열 선택교체
SELECT REPLACE('aabbcc', 'bb', 'ff');	# aaffcc
# 특정 문자열의 위치값 확인 없으면 0 출력
SELECT INSTR('안녕하세요', '하세');			# 3
SELECT INSTR('안녕하세요', '방갑');			# 0


# LEFT, RIGHT, MID : 위치기준 삭제
# LEFT() : 왼쪽에서부터 3개를 제외한 나머지 삭제
SELECT LEFT('abcdef', 3);				# abc
# RIGHT() : 오른쪽에서부터 3개를 제외한 나머지 삭제
SELECT RIGHT('abcdef', 3);				# def
# MID() : 2번째에서부터 3개를 제외한 나머지 삭제
SELECT MID('abcdefg', 2, 3);			# bcd



# LTRIM, RTRIM, TRIM : 공백제거 관련
SELECT CONCAT('[', '         abc        ', ']');		# 공백제거 없이 연결
SELECT CONCAT('[', LTRIM('         abc        '), ']');	# LTRIM() : 왼쪽 공백 제거 후 연결
SELECT CONCAT('[', RTRIM('         abc        '), ']');	# RTRIM() : 오른쪽 공백 제거 후 연결
SELECT CONCAT('[', TRIM('         abc        '), ']');	# TRIM()  : 좌우 공백 제거 후 연결

# LCASE, LOWER
SELECT LCASE('acDDefg');	# 소문자 변환
SELECT LOWER('acDDefg');	# 소문자 변환

# UCASE, UPPER
SELECT UCASE('acDDefg');	# 대문자 변환
SELECT UPPER('acDDefg');	# 대문자 변환

# REVERSE : 문자열 순서 반전
SELECT REVERSE('acDDefg'); # gfeDDca

#----------------------------------------------------------------------------
# 날짜 함수

# 날짜와 시간
SELECT NOW(); # NOW는 쿼리가 실행되는 순간의 시간
SELECT SYSDATE(); # SYSDATE는 해당 함수를 호출한 시간

/*
	CURRENT_TIMESTAMP() 함수는 현재 날짜와 시간을 반환합니다.
	참고: 날짜 및 시간은 "YYYY-MM-DD HH-MM-SS"(문자열) 또는 YYYYMMDDHHMMSS.uuuuuu(숫자)로 반환됩니다.
*/
SELECT CURRENT_TIMESTAMP();


/*
	CURRENT_DATE() 함수는 현재 날짜를 반환합니다.
	참고: 날짜는 "YYYY-MM-DD"(문자열) 또는 YYYYMMDD(숫자)로 반환됩니다.
	참고: 이 함수는 CURDATE() 함수와 같습니다.
*/
SELECT CURRENT_DATE();

SELECT CURDATE();

# 시간
SELECT CURRENT_TIME();
SELECT CURTIME();

SELECT NOW(), YEAR(NOW()); # 년
SELECT NOW(), MONTH(NOW()); # 월
SELECT NOW(), DAY(NOW()); # 일
SELECT(CONCAT(YEAR(NOW()), '년 ', MONTH(NOW()), '월 ', DAY(NOW()), '일'));

SELECT NOW(), MONTHNAME(NOW()); # 영어 월 출력
SELECT DAYNAME(NOW()); # 영어 요일 출력

SELECT NOW(), DAYOFWEEK(NOW());		# 일요일 = 1, 월요일 = 2 ....
SELECT NOW(), DAYOFYEAR(NOW());		# 올해의 몇번째 날
SELECT NOW(), WEEK(NOW());			# 올해의 몇번째 주

# 포맷 - 원하는 형식으로 출력
SELECT NOW(), DATE_FORMAT(NOW(), '%Y년 %m월 %d일, %H시 %i분 %S초');

# [문제] member테이블에서 회원의 가입 일자를 한글 날짜 형식으로 가져오기 - 날짜 내림차순(최신순)
SELECT member_no, DATE_FORMAT(member_reg_date, '%Y년 %m월 %d일, %H시 %i분 %S초') FROM member ORDER BY member_reg_date DESC;























