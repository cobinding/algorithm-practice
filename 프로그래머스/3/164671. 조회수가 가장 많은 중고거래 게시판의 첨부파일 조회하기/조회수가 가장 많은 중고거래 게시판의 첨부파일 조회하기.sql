SELECT concat("/home/grep/src/", board.board_id, "/", file.file_id, file.file_name, file.file_ext) as file_path
from USED_GOODS_BOARD as board
join USED_GOODS_FILE as file
on board.board_id = file.board_id
where views = (
    select max(views)
    from used_goods_board
)
order by file.file_id desc;

