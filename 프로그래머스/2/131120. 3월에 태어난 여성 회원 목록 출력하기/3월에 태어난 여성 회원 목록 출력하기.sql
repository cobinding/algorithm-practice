-- 코드를 입력하세요
SELECT member_id, member_name, gender, date_format(date_of_birth, "%Y-%m-%d") as DATE_OF_BIRTH
from member_profile
where (month(date_of_birth) = 3) and (tlno is not null) and gender like "%W"
order by member_id 