from datetime import datetime
from typing import Any, Dict, List

from lib.pg import PgConnect


class DdsRepository:
    def __init__(self, db: PgConnect) -> None:
        self._db = db

    #hubs
    def h_user_insert(self, h_user_pk: str, user_id: str, load_dt: datetime, load_src: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.h_user (h_user_pk, user_id, load_dt, load_src)
                    values (%(h_user_pk)s, %(user_id)s, %(load_dt)s, %(load_src)s)
                    on conflict(h_user_pk) do nothing;
                    """,
                    {
                    'h_user_pk': h_user_pk,
                    'user_id': user_id,
                    'load_dt': load_dt,
                    'load_src': load_src
                    }
                )

    def h_product_insert(self, h_product_pk: str, product_id: str, load_dt: datetime, load_src: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.h_product (h_product_pk, product_id, load_dt, load_src)
                    values (%(h_product_pk)s, %(product_id)s, %(load_dt)s, %(load_src)s)
                    on conflict(h_product_pk) do nothing;
                    """,
                    {
                    'h_product_pk': h_product_pk,
                    'product_id': product_id,
                    'load_dt': load_dt,
                    'load_src': load_src
                    }
                )

    def h_category_insert(self, h_category_pk: str, category_name: str, load_dt: datetime, load_src: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.h_category (h_category_pk, category_name, load_dt, load_src)
                    values (%(h_category_pk)s, %(category_name)s, %(load_dt)s, %(load_src)s)
                    on conflict(h_category_pk) do nothing;
                    """,
                    {
                    'h_category_pk': h_category_pk,
                    'category_name': category_name,
                    'load_dt': load_dt,
                    'load_src': load_src
                    }
                )

    def h_restaurant_insert(self, h_restaurant_pk: str, restaurant_id: str, load_dt: datetime, load_src: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.h_restaurant (h_restaurant_pk, restaurant_id, load_dt, load_src)
                    values (%(h_restaurant_pk)s, %(restaurant_id)s, %(load_dt)s, %(load_src)s)
                    on conflict(h_restaurant_pk) do nothing;
                    """,
                    {
                    'h_restaurant_pk': h_restaurant_pk,
                    'restaurant_id': restaurant_id,
                    'load_dt': load_dt,
                    'load_src': load_src
                    }
                )

    def h_order_insert(self, h_order_pk: str, order_id: str, order_dt:datetime, load_dt: datetime, load_src: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.h_order (h_order_pk, order_id, load_dt, order_dt, load_src)
                    values (%(h_order_pk)s, %(order_id)s, %(load_dt)s, %(order_dt)s, %(load_src)s)
                    on conflict(h_order_pk) do nothing;
                    """,
                    {
                    'h_order_pk': h_order_pk,
                    'order_id': order_id,
                    'load_dt': load_dt,
                    'order_dt': order_dt,
                    'load_src': load_src
                    }
                )

    #links
    def l_order_product_insert(self, hk_order_product_pk:str, h_order_pk: str, h_product_pk: str, load_dt:datetime, load_src: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.l_order_product (hk_order_product_pk, h_order_pk, h_product_pk, load_dt, load_src)
                    values (%(hk_order_product_pk)s, %(h_order_pk)s, %(h_product_pk)s, %(load_dt)s, %(load_src)s)
                    on conflict(hk_order_product_pk) do nothing;
                    """,
                    {
                    'hk_order_product_pk': hk_order_product_pk,
                    'h_order_pk': h_order_pk,
                    'h_product_pk': h_product_pk,
                    'load_dt': load_dt,
                    'load_src': load_src
                    }
                )

    def l_product_restaurant_insert(self, hk_product_restaurant_pk:str, h_product_pk: str, h_restaurant_pk: str, load_dt:datetime, load_src: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.l_product_restaurant (hk_product_restaurant_pk, h_product_pk, h_restaurant_pk, load_dt, load_src)
                    values (%(hk_product_restaurant_pk)s, %(h_product_pk)s, %(h_restaurant_pk)s, %(load_dt)s, %(load_src)s)
                    on conflict(hk_product_restaurant_pk) do nothing;
                    """,
                    {
                    'hk_product_restaurant_pk': hk_product_restaurant_pk,
                    'h_product_pk': h_product_pk,
                    'h_restaurant_pk': h_restaurant_pk,
                    'load_dt': load_dt,
                    'load_src': load_src
                    }
                )

    def l_product_category_insert(self, hk_product_category_pk:str, h_product_pk: str, h_category_pk: str, load_dt:datetime, load_src: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.l_product_category (hk_product_category_pk, h_product_pk, h_category_pk, load_dt, load_src)
                    values (%(hk_product_category_pk)s, %(h_product_pk)s, %(h_category_pk)s, %(load_dt)s, %(load_src)s)
                    on conflict(hk_product_category_pk) do nothing;
                    """,
                    {
                    'hk_product_category_pk': hk_product_category_pk,
                    'h_product_pk': h_product_pk,
                    'h_category_pk': h_category_pk,
                    'load_dt': load_dt,
                    'load_src': load_src
                    }
                )

    def l_order_user_insert(self, hk_order_user_pk:str, h_order_pk: str, h_user_pk: str, load_dt:datetime, load_src: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.l_order_user (hk_order_user_pk, h_order_pk, h_user_pk, load_dt, load_src)
                    values (%(hk_order_user_pk)s, %(h_order_pk)s, %(h_user_pk)s, %(load_dt)s, %(load_src)s)
                    on conflict(hk_order_user_pk) do nothing;
                    """,
                    {
                    'hk_order_user_pk': hk_order_user_pk,
                    'h_order_pk': h_order_pk,
                    'h_user_pk': h_user_pk,
                    'load_dt': load_dt,
                    'load_src': load_src
                    }
                )

    #satellites
    def s_user_names_insert(self, h_user_pk:str, username: str, userlogin: str, load_dt:datetime, load_src: str, hk_user_names_hashdiff: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.s_user_names (h_user_pk, username, userlogin, load_dt, load_src, hk_user_names_hashdiff)
                    values (%(h_user_pk)s, %(username)s, %(userlogin)s, %(load_dt)s, %(load_src)s, %(hk_user_names_hashdiff)s)
                    on conflict(hk_user_names_hashdiff) do nothing;
                    """,
                    {
                    'h_user_pk': h_user_pk,
                    'username': username,
                    'userlogin': userlogin,
                    'load_dt': load_dt,
                    'load_src': load_src,
                    'hk_user_names_hashdiff': hk_user_names_hashdiff
                    }
                )


    def s_product_names_insert(self, h_product_pk:str, name: str, load_dt:datetime, load_src: str, hk_product_names_hashdiff: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.s_product_names (h_product_pk, name, load_dt, load_src, hk_product_names_hashdiff)
                    values (%(h_product_pk)s, %(name)s, %(load_dt)s, %(load_src)s, %(hk_product_names_hashdiff)s)
                    on conflict(hk_product_names_hashdiff) do nothing;
                    """,
                    {
                    'h_product_pk': h_product_pk,
                    'name': name,
                    'load_dt': load_dt,
                    'load_src': load_src,
                    'hk_product_names_hashdiff':  hk_product_names_hashdiff
                    }
                )

    def s_restaurant_names_insert(self, h_restaurant_pk:str, name: str, load_dt:datetime, load_src: str, hk_restaurant_names_hashdiff: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.s_restaurant_names (h_restaurant_pk, name, load_dt, load_src, hk_restaurant_names_hashdiff)
                    values (%(h_restaurant_pk)s, %(name)s, %(load_dt)s, %(load_src)s, %(hk_restaurant_names_hashdiff)s)
                    on conflict(h_restaurant_pk) do nothing;
                    """,
                    {
                    'h_restaurant_pk': h_restaurant_pk,
                    'name': name,
                    'load_dt': load_dt,
                    'load_src': load_src,
                    'hk_restaurant_names_hashdiff':  hk_restaurant_names_hashdiff
                    }
                )

    def s_order_cost_insert(self, h_order_pk:str, cost: float, payment: float, load_dt:datetime, load_src: str, hk_order_cost_hashdiff: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.s_order_cost (h_order_pk, cost, payment, load_dt, load_src, hk_order_cost_hashdiff)
                    values (%(h_order_pk)s, %(cost)s, %(payment)s, %(load_dt)s, %(load_src)s, %(hk_order_cost_hashdiff)s)
                    on conflict(h_order_pk) do nothing;
                    """,
                    {
                    'h_order_pk': h_order_pk,
                    'cost': cost,
                    'payment': payment,
                    'load_dt': load_dt,
                    'load_src': load_src,
                    'hk_order_cost_hashdiff':  hk_order_cost_hashdiff
                    }
                )

    def s_order_status_insert(self, h_order_pk:str, status: str, load_dt:datetime, load_src: str, hk_order_status_hashdiff: str) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.s_order_status (h_order_pk, status, load_dt, load_src, hk_order_status_hashdiff)
                    values (%(h_order_pk)s, %(status)s, %(load_dt)s, %(load_src)s, %(hk_order_status_hashdiff)s)
                    on conflict(h_order_pk) do nothing;
                    """,
                    {
                    'h_order_pk': h_order_pk,
                    'status': status,
                    'load_dt': load_dt,
                    'load_src': load_src,
                    'hk_order_status_hashdiff':  hk_order_status_hashdiff
                    }
                )