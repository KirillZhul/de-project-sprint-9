from datetime import datetime
from typing import Any, Dict, List
from lib.pg import PgConnect

class CdmRepository:
    def __init__(self, db: PgConnect) -> None:
        self._db = db

    def user_product_counters_insert(self, user_id:str, product_id: str, product_name: str, order_cnt: int) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into cdm.user_product_counters (user_id, product_id, product_name, order_cnt)
                    values (%(user_id)s, %(product_id)s, %(product_name)s, %(order_cnt)s)
                    on conflict(user_id, product_id) do update
                    set order_cnt = user_product_counters.order_cnt + excluded.order_cnt;
                    """,
                    {
                    'user_id': user_id,
                    'product_id': product_id,
                    'product_name': product_name,
                    'order_cnt': order_cnt
                    }
                )


    def user_category_counters_insert(self, user_id:str, category_id: str, category_name: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into cdm.user_category_counters (user_id, category_id, category_name, order_cnt)
                    values (%(user_id)s, %(category_id)s, %(category_name)s, 1)
                    on conflict(user_id, category_id) do update
                    set order_cnt = user_category_counters.order_cnt + 1;
                    """,
                    {
                    'user_id': user_id,
                    'category_id': category_id,
                    'category_name': category_name
                    }
                )