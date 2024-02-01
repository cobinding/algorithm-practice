-- 코드를 입력하세요
select book_id, date_format(published_date, '%Y-%m-%d') as PUBLISHED_DATE
from book
where (category = '인문' and date_format(published_date, '%Y') = 2021)
order by published_date