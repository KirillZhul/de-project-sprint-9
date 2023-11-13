-- DROP TABLE dds.h_category;

CREATE TABLE dds.h_category (
	h_category_pk uuid NOT NULL,
	category_name varchar NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	CONSTRAINT h_category_pkey PRIMARY KEY (h_category_pk)
);


-- DROP TABLE dds.h_order;

CREATE TABLE dds.h_order (
	h_order_pk uuid NOT NULL,
	order_id int4 NOT NULL,
	order_dt timestamp NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	CONSTRAINT h_order_pkey PRIMARY KEY (h_order_pk)
);


-- DROP TABLE dds.h_product;

CREATE TABLE dds.h_product (
	h_product_pk uuid NOT NULL,
	product_id varchar NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	CONSTRAINT h_product_pkey PRIMARY KEY (h_product_pk)
);


-- DROP TABLE dds.h_restaurant;

CREATE TABLE dds.h_restaurant (
	h_restaurant_pk uuid NOT NULL,
	restaurant_id varchar NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	CONSTRAINT h_restaurant_pkey PRIMARY KEY (h_restaurant_pk)
);


-- DROP TABLE dds.h_user;

CREATE TABLE dds.h_user (
	h_user_pk uuid NOT NULL,
	user_id varchar NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	CONSTRAINT h_user_pkey PRIMARY KEY (h_user_pk)
);


-- DROP TABLE dds.l_order_product;

CREATE TABLE dds.l_order_product (
	hk_order_product_pk uuid NOT NULL,
	h_order_pk uuid NOT NULL,
	h_product_pk uuid NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	CONSTRAINT l_order_product_pkey PRIMARY KEY (hk_order_product_pk)
);


-- DROP TABLE dds.l_order_user;

CREATE TABLE dds.l_order_user (
	hk_order_user_pk uuid NOT NULL,
	h_order_pk uuid NOT NULL,
	h_user_pk uuid NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	CONSTRAINT l_order_user_pkey PRIMARY KEY (hk_order_user_pk)
);


-- DROP TABLE dds.l_product_category;

CREATE TABLE dds.l_product_category (
	hk_product_category_pk uuid NOT NULL,
	h_category_pk uuid NOT NULL,
	h_product_pk uuid NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	CONSTRAINT l_product_category_pkey PRIMARY KEY (hk_product_category_pk)
);


-- DROP TABLE dds.l_product_restaurant;

CREATE TABLE dds.l_product_restaurant (
	hk_product_restaurant_pk uuid NOT NULL,
	h_restaurant_pk uuid NOT NULL,
	h_product_pk uuid NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	CONSTRAINT l_product_restaurant_pkey PRIMARY KEY (hk_product_restaurant_pk)
);


-- DROP TABLE dds.s_order_cost;

CREATE TABLE dds.s_order_cost (
	h_order_pk uuid NOT NULL,
	"cost" numeric(19, 5) NOT NULL DEFAULT 0,
	payment numeric(19, 5) NOT NULL DEFAULT 0,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	hk_order_cost_hashdiff uuid NOT NULL,
	CONSTRAINT s_order_cost_cost_check CHECK ((cost >= (0)::numeric)),
	CONSTRAINT s_order_cost_hk_order_cost_hashdiff_key UNIQUE (hk_order_cost_hashdiff),
	CONSTRAINT s_order_cost_payment_check CHECK ((payment >= (0)::numeric)),
	CONSTRAINT s_order_cost_pkey PRIMARY KEY (h_order_pk)
);

-- dds.s_order_cost foreign keys

ALTER TABLE dds.s_order_cost ADD CONSTRAINT s_order_cost_h_order_pk_fkey FOREIGN KEY (h_order_pk) REFERENCES dds.h_order(h_order_pk);


-- DROP TABLE dds.s_order_status;

CREATE TABLE dds.s_order_status (
	h_order_pk uuid NOT NULL,
	status varchar NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	hk_order_status_hashdiff uuid NOT NULL,
	CONSTRAINT s_order_status_hk_order_status_hashdiff_key UNIQUE (hk_order_status_hashdiff),
	CONSTRAINT s_order_status_pkey PRIMARY KEY (h_order_pk)
);

-- dds.s_order_status foreign keys

ALTER TABLE dds.s_order_status ADD CONSTRAINT s_order_status_h_order_pk_fkey FOREIGN KEY (h_order_pk) REFERENCES dds.h_order(h_order_pk);


-- DROP TABLE dds.s_product_names;

CREATE TABLE dds.s_product_names (
	h_product_pk uuid NOT NULL,
	"name" varchar NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	hk_product_names_hashdiff uuid NOT NULL,
	CONSTRAINT s_product_names_hk_product_names_hashdiff_key UNIQUE (hk_product_names_hashdiff),
	CONSTRAINT s_product_names_pkey PRIMARY KEY (h_product_pk)
);

-- dds.s_product_names foreign keys

ALTER TABLE dds.s_product_names ADD CONSTRAINT s_product_names_h_product_pk_fkey FOREIGN KEY (h_product_pk) REFERENCES dds.h_product(h_product_pk);


-- DROP TABLE dds.s_restaurant_names;

CREATE TABLE dds.s_restaurant_names (
	h_restaurant_pk uuid NOT NULL,
	"name" varchar NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	hk_restaurant_names_hashdiff uuid NOT NULL,
	CONSTRAINT s_restaurant_names_hk_restaurant_names_hashdiff_key UNIQUE (hk_restaurant_names_hashdiff),
	CONSTRAINT s_restaurant_names_pkey PRIMARY KEY (h_restaurant_pk)
);

-- dds.s_restaurant_names foreign keys

ALTER TABLE dds.s_restaurant_names ADD CONSTRAINT s_restaurant_names_h_restaurant_pk_fkey FOREIGN KEY (h_restaurant_pk) REFERENCES dds.h_restaurant(h_restaurant_pk);


-- DROP TABLE dds.s_user_names;

CREATE TABLE dds.s_user_names (
	h_user_pk uuid NOT NULL,
	username varchar NOT NULL,
	userlogin varchar NOT NULL,
	load_dt timestamp NOT NULL,
	load_src varchar NOT NULL,
	hk_user_names_hashdiff uuid NOT NULL,
	CONSTRAINT s_user_names_hk_user_names_hashdiff_key UNIQUE (hk_user_names_hashdiff),
	CONSTRAINT s_user_names_pkey PRIMARY KEY (h_user_pk, load_dt)
);

-- dds.s_user_names foreign keys

ALTER TABLE dds.s_user_names ADD CONSTRAINT s_user_names_h_user_pk_fkey FOREIGN KEY (h_user_pk) REFERENCES dds.h_user(h_user_pk);
