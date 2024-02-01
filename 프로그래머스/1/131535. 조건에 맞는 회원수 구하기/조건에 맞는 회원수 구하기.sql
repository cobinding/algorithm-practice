-- 코드를 입력하세요
SELECT count(user_id)
from user_info
where date_format(joined, '%Y') = 2021 and age >= 20 and age <= 29