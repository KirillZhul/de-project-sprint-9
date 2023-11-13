-- DROP TABLE cdm.user_category_counters;

CREATE TABLE cdm.user_category_counters (
	id serial4 NOT NULL,
	user_id uuid NOT NULL,
	category_id uuid NOT NULL,
	category_name varchar NOT NULL,
	order_cnt int4 NOT NULL,
	CONSTRAINT user_category_counters_order_cnt_check CHECK ((order_cnt >= 0)),
	CONSTRAINT user_category_counters_pkey PRIMARY KEY (id)
);
CREATE UNIQUE INDEX idx_unique_user_category ON cdm.user_category_counters USING btree (user_id, category_id);


-- DROP TABLE cdm.user_product_counters;

CREATE TABLE cdm.user_product_counters (
	id serial4 NOT NULL,
	user_id uuid NOT NULL,
	product_id uuid NOT NULL,
	product_name varchar NOT NULL,
	order_cnt int4 NOT NULL,
	CONSTRAINT user_product_counters_order_cnt_check CHECK ((order_cnt >= 0)),
	CONSTRAINT user_product_counters_pkey PRIMARY KEY (id)
);
CREATE UNIQUE INDEX idx_unique_user_product ON cdm.user_product_counters USING btree (user_id, product_id);
