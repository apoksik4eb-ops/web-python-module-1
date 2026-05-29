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

-- Задание 1 ------------------------------------

select *
from vegetables_fruits
where type = 'овощ'
  and calories < 50;

-- ----------------------------------------------

select *
from vegetables_fruits
where type = 'фрукт'
  and calories between 50 and 100;

-- ----------------------------------------------

select *
from vegetables_fruits
where type = 'овощ'
  and name ilike '%перец%';

-- ----------------------------------------------

select *
from vegetables_fruits
where description ilike '%много%';

-- ----------------------------------------------

select *
from vegetables_fruits
where color in ('желтый', 'красный');

-- Задание 2 ------------------------------------

select count(*) as vegetables_count
from vegetables_fruits
where type = 'овощ';

-- ----------------------------------------------

select count(*) as fruits_count
from vegetables_fruits
where type = 'фрукт';

-- ----------------------------------------------

select count(*) as color_count
from vegetables_fruits
where color = 'красный';

-- ----------------------------------------------

select color, count(*) as total
from vegetables_fruits
group by color;

-- ----------------------------------------------

select color, count(*) as total
from vegetables_fruits
group by color
order by total asc
limit 1;

-- ----------------------------------------------

select color, count(*) as total
from vegetables_fruits
group by color
order by total desc
limit 1;

-- ----------------------------------------------

select min(calories) as min_calories
from vegetables_fruits;

-- ----------------------------------------------

select max(calories) as max_calories
from vegetables_fruits;

-- ----------------------------------------------

select avg(calories) as avg_calories
from vegetables_fruits;

-- ----------------------------------------------

select *
from vegetables_fruits
where type = 'фрукт'
order by calories asc
limit 1;

-- ----------------------------------------------

select *
from vegetables_fruits
where type = 'фрукт'
order by calories desc
limit 1;