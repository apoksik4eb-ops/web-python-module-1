create table departments (
	id serial primary key,
	name text not null unique
);

create table employees (
	id serial primary key,
	name text not null,
	salary numeric(10, 2) check (salary > 0),
	department_id int references departments(id),
	hired_at date default current_date
);

create table projects (
	id serial primary key,
	name text not null,
	employee_id int references employees(id),
	budget numeric (12, 2) check (budget >= 0),
	is_active boolean default true
);

-- ----------------------------------------------

insert into departments (name)
values
	('IT'),
	('HR'),
	('Finance'),
	('Marketing');

insert into employees (name, salary, department_id, hired_at)
values
	('Анна Иванова', 150000, 1, '2023-01-15'),
	('Иван Петров', 90000, 1, '2023-03-10'),
	('Мария Смирнова', 110000, 2, '2022-11-20'),
	('Олег Кузнецов', 130000, 3, '2021-06-05'),
	('Мария Смирнова', 110000, 2, '2022-11-20'),
	('Алексей Орлов', 70000, NULL, '2024-02-01'),
	('Елена Соколова', 160000, 2, '2020-09-12');

insert into projects (name, employee_id, budget, is_active)
values
	('CRM System', 1, 500000, TRUE),
	('Website Redesign', 2, 200000, TRUE),
	('Hiring Platform', 3, 300000, TRUE),
	('Accointing Automation', 4, 500000, FALSE),
	('Internal Chat', 1, 150000, TRUE);

-- ----------------------------------------------

select
	name,
	salary,
	case
		when salary >= 150000 then 'high'
		when salary >= 100000 then 'middle'
		else 'low'
	end as salary_level
from employees;

-- ----------------------------------------------

select
	e.name as employee_name,
	coalesce(d.name, 'Без отдела') as department_name
from employees e
left join departments d on e.department_id = d.id;

-- ----------------------------------------------

select
	d.id,
	d.name
from departments d
where exists (
	select 1 from employees e
	where e.department_id = d.id
);

-- ----------------------------------------------

select
	e.id,
	e.name
from employees e
where exists (
	select 1 from projects p
	where p.employee_id = e.id
);

-- ----------------------------------------------

select
	name as project_name,
	budget,
	case	
		when is_active = true then 'active'
		else 'close'
	end as project_status
from projects;


-- ----------------------------------------------

select
	e.name as employee_name,
	COUNT(p.id) as projects_count
from employees e
left join projects p on p.employee_id = e.id
group by e.id, e.name
order by projects_count desc;

-- ----------------------------------------------

UPDATE projects
SET budget = budget + 50000
WHERE is_active = true
returning
	name as project_name,
	budget as new_budget;
	
-- ----------------------------------------------

delete from projects
where is_active = false
returning name;

-- ----------------------------------------------

create table employee_profiles (
	id SERIAL primary key,
	employee_id INT unique references employees(id),
	phone TEXT unique,
	address TEXT,
	birth_date DATE
);

insert into employee_profiles (employee_id, phone, address, birth_date)
values
	(1, '+79001234567', 'address-1', '1980-05-25'),
	(2, '+79001234555', 'address-1', '1981-05-25'),
	(3, '+79001234577', 'address-1', '1982-05-25');

select
	e.name as employee_name,
	ep.phone,
	ep.address,
	ep.birth_date
from employees e
join employee_profiles ep on ep.employee_id = e.id;

insert into employee_profiles(employee_id, phone, address, birth_date)
values
	(1, '79001234577', 'address-4', '1995-05-25');

------------------------------------------------
-- N - N
create table skills (
	id SERIAL primary key,
	name TEXT not null unique
);


create table employee_skills (
	employee_id INT references employees(id),
	skill_id INT references skills(id),
	primary key (employee_id, skill_id)
);

insert into skills (name)
values
	('SQL'),
	('PostreSQL'),
	('MySQL'),
	('Excel');

insert into employee_skills (employee_id, skill_id)
values
	(1, 1),
	(2, 1),
	(3, 1),
	(1, 2),
	(2, 2),
	(3, 2),
	(1, 4);

select
	e.name as employee_name,
	s.name as skill_name
from employee_skills es
join employees e on es.employee_id = e.id
join skills s on es.skill_id = s.id
order by e.name, s.name;

-- ----------------------------------------------

select
	e.name as employee_name,
	e.salary,
	d.name as department_name,
	ep.phone,
	ep.address,
	p.name as project_name,
	s.name as skill_name
from employees e
left join departments d on e.department_id = d.id
left join employee_profiles ep on ep.employee_id = e.id
left join projects p on p.employee_id = e.id
left join employee_skills es on es.employee_id = e.id
left join skills s on es.skill_id = s.id
order by e.name, p.name, s.name;

-- ----------------------------------------------

select
	e.name as employee_name,
	coalesce(sum(p.budget), 0) as total_budget
from employees e
left join projects p on p.employee_id = e.id
group by e.name, p.budget
order by e.name;

-- ----------------------------------------------

select 
	p.name as project_name,
	p.budget,
	e.name as employee_name,
	d.name as department_name
from projects p
join employees e on p.employee_id = e.id
join departments d on e.department_id = d.id
WHERE p.is_active = true and p.budget > 200000
order by p.budget desc;

-- ----------------------------------------------

select
	e.name as emp_name,
	e.salary,
	d.name as dep_name,
	p.name as proj_name,
	p.budget
from employees e
join departments d on e.department_id = e.id 
join projects p on p.employee_id = e.id;