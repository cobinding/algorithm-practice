-- 코드를 입력하세요
SELECT user_id, product_id
from online_sale
group by product_id, user_id
having count(product_id) > 1 
order by user_id asc, product_id desc;
