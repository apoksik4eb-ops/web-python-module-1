create database Birds;

-- ----------------------------------------------

alter database Birds rename to Cats;

-- ----------------------------------------------

drop database Cats;

-- ----------------------------------------------
create type food_type AS ENUM ('овощ', 'фрукт');

create table vegetables_fruits (
	id serial primary key,
	name text not null,
	type food_type not null,
	color text not null,
    calories int check (calories >= 0),
    description text
);

insert into vegetables_fruits (name, type, color, calories, description)
values
	('банан', 'фрукт', 'желтый', 50, 'богатый белком'),
	('огурец', 'овощ', 'зеленый', 20, 'полезный перекус'),
	('помидор', 'овощ', 'красный', 70, 'незаменим для салата'),
	('перец', 'овощ', 'красный', 30, 'очень полезен'),
	('яблоко', 'фрукт', 'зеленый', 90, 'много железа'),
	('хурма', 'фрукт', 'желтый', 120, 'иногда вяжет');

-- ----------------------------------------------

select *
from vegetables_fruits;

-- ----------------------------------------------

select *
from vegetables_fruits
where type = 'овощ';

-- ----------------------------------------------

select *
from vegetables_fruits
where type = 'фрукт';

-- ----------------------------------------------

select name
from vegetables_fruits;

-- ----------------------------------------------

select distinct color
from vegetables_fruits;

-- ----------------------------------------------

select *
from vegetables_fruits
where type = 'фрукт' and color = 'желтый';

-- ----------------------------------------------

select *
from vegetables_fruits
where type = 'овощ' and color = 'красный';