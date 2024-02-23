SELECT rental.car_id
from car_rental_company_car as rental join CAR_RENTAL_COMPANY_RENTAL_HISTORY as history
on rental.car_id = history.car_id
where rental.car_type like "세단" and date_format(history.start_date, "%m") = 10
group by rental.car_id
order by rental.car_id desc;