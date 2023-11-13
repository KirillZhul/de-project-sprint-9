-- DROP TABLE stg.order_events;

CREATE TABLE stg.order_events (
	id serial4 NOT NULL,
	object_id int4 NOT NULL,
	payload json NOT NULL,
	object_type varchar NOT NULL,
	sent_dttm timestamp NOT NULL,
	CONSTRAINT order_events_object_id_key UNIQUE (object_id),
	CONSTRAINT order_events_pkey PRIMARY KEY (id)
);
