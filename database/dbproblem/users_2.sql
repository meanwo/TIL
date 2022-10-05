
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INT NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INT NOT NULL
);

SELECT COUNT(*) AS '개수' FROM users;

UPDATE users
SET country='경기도'
WHERE first_name='옥자' and last_name='김';

SELECT * FROM users WHERE first_name='옥자' and last_name='김';

-- 명세 4 (데이터 삭제)
DELETE FROM users WHERE first_name='진호' and last_name='백';

SELECT * FROM users WHERE first_name='진호' and last_name='백';

-- 명세 5
SELECT country, max(balance), age FROM users
-- 30 <= age < 40 은 오류가 나옴
-- WHERE 30 <= age AND age < 40 은 가능
WHERE age BETWEEN 30 AND 39
GROUP BY country;

-- -- balance의 내림차순으로 정렬
-- ORDER by balance DESC;

-- -- 최상위 3개만 출력
-- LIMIT 3;


