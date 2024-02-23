-- 코드를 입력하세요
SELECT board_id, writer_id, title, price, case when status = "sale" then "판매중"
            when status = "reserved" then "예약중"
            when status = "done" then "거래완료"
        end as status
from used_goods_board
where date_format(created_date, "%Y-%m-%d") = "2022-10-05"
order by board_id desc;