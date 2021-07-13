CREATE TABLE IF NOT EXISTS tb_customer (
	cust_id text PRIMARY KEY,
	cust_name text
);

CREATE TABLE IF NOT EXISTS tb_restaurant (
    rest_id text PRIMARY KEY,
    rest_name text
);

CREATE TABLE IF NOT EXISTS tb_menu (
    menu_id text PRIMARY KEY,
    rest_id text,
    item_name text
);


CREATE TABLE IF NOT EXISTS tb_order (
    order_id text,
    cust_id text,
    items text,
    quantity integer,
    price integer
);


INSERT INTO tb_customer(cust_id, cust_name) VALUES(1, 'paul');

INSERT INTO tb_restaurant(rest_id, rest_name) VALUES(1, 'KFC');
INSERT INTO tb_restaurant(rest_id, rest_name) VALUES(2, 'McDonald');

INSERT INTO tb_menu(menu_id, rest_id, item_name) VALUES(1,1,'chicken strips');
INSERT INTO tb_menu(menu_id, rest_id, item_name) VALUES(2,1,'chicken popcorn');
INSERT INTO tb_menu(menu_id, rest_id, item_name) VALUES(3,2,'pizza');
INSERT INTO tb_menu(menu_id, rest_id, item_name) VALUES(4,2,'burger');

