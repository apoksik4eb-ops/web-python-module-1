## 1. База данных

### `CREATE`
Создает объект: таблица, база, индекс
```sql
CREATE TABLE employess(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    salary NUMERIC
);
```

### `TABLE`
Указывает что создается изменяется таблица
```sql
CREATE TABLE departments(
    id SERIAL PRIMARY KEY,
    name TEXT
);
```

### `ALTER`
Изменяет существующий объект
```sql
ALTER TABLE employess
ADD COLUMN email TEXT;
```

### `ADD`
Добавляет колонку, ограничения
```sql
ALTER TABLE employess
ADD COLUMN phone TEXT;
```

### `DROP`
Удаляет объект(таблицу)
```sql
DROP TABLE projects;
```

### `IF EXISTS`
Позволяет избежать ошибки если объекта нет
```sql
DROP TABLE IF EXISTS old_projects;
```

### `IF NOT EXISTS`
Создает объект только если он не существует
```sql
CREATE TABLE IF NOT EXISTS departments(
    id SERIAL PRIMARY KEY,
    name TEXT
);
```

### `RENAME`
Переименовывает объект
```sql
ALTER TABLE employees
RENAME COLUMN name to full_name;
```

### `TRUNCATE`
Быстро очищает таблицу
```sql
TRUNCATE TABLE projects;
```

## 2. Работа с данными
### `SELECT`
Выбирает данные
```sql
SELECT name, salary FROM employees;
```

### `FROM`
Указывает источник данных
```sql
SELECT name, salary FROM employees;
```

### `INSERT`
Добавляет строки
```sql
INSERT INTO departments(name)
VALUES ('it'), ('HR'), ('Finance');
```

### 'INTO'
Указывает куда вставлять данные
```sql
INSERT INTO employees(name, salary, department_id)
VALUES ('Анна', 12000, 1);
```

### `VALUES`
Передает конкретные значения
```sql
INSERT INTO project(name, employee_id, budget)
VALUES ('CRM System', 1, 500000);
```

### `UPDATE`
Обновляет строки
```sql
UPDATE employees
SET salary = salary *1.10
WHERE departament_id = 1;
```

### `SET`
Задает новые значения при `UPDATE`
```sql
UPDATE projects
SET is_active = FALSE
    is_active_2 = FALSE
WHERE budget < 100000;
```

### `DELETE`
Удаляет строки
```sql
DELETE FROM employees
WHERE salary < 50000;
```

## 3. Фильтрация данных

### `WHERE`
Фильтрует строки
```sql
SELECT *
FROM employees
WHERE salary > 100000
```

### `AND`
Оба условия должны быть истины
```sql
SELECT *
FROM employees
WHERE salary > 100000
    AND departament_id = 1;
```

### `OR`
Хотя бы одно условие должно быть истинным
```sql
SELECT *
FROM employees
WHERE salary > 100000
    OR departament_id = 1;
```

### `NOT`
Отрицание условия.
```sql
SELECT *
FROM project
WHERE NOT is_active
```

### `IN`
Проверяет, что значения входят в список
```sql
SELECT *
FROM employees
WHERE depatament_id IN (1, 2);
```

### `NOT IN`
Проверяет, что значения не входят в список
```sql
SELECT *
FROM employees
WHERE depatament_id NOT IN (1, 2);
```

### `BETWEEN`
Проверяет диапазон
```sql
SELECT *
FROM employees
WHERE salary BETWEEN 80000 AND 150000 
```

### `LIKE`
Поиск по шаблону
```sql
SELECT *
FROM employees
WHERE name LIKE "A%";
```

### `ILIKE`
Поиск по шаблону без регистра букв
```sql
SELECT *
FROM employees
WHERE name ILIKE "a%";
```

### `IS NULL`
Проверяет значения на `NULL`
```sql
SELECT *
FROM employees
WHERE departament_id IS NULL;
```

### `IS NOT NULL`
Проверяет значение что не `NULL`
```sql
SELECT *
FROM employees
WHERE departament_id IS NOT NULL;
```

### `EXISTS`
Проверяет существование
```sql
SELECT *
FROM departments AS d
WHERE EXISTS (
    SELECT 1
    FROM employees AS e
    WHERE e.departments_id = d.id
);
```

## 4. Сортировка и ограничение результата

### `ORDER BY`
Сортирует результат
```sql
SELECT *
FROM employees
ORDER BY salary;
```

### `ASC`
Сортировка по возрастанию
```sql
SELECT *
FROM employees
ORDER BY salary ASC;
```

### `DESC`
Сортировка по убыванию
```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

### `LIMIT`
Ограничивет количество строк
```sql
SELECT *
FROM employees
ORDER BY salary
LIMIT 5;
```

### `OFFSET`
Пропускает указанное количество строк
```sql
SELECT *
FROM employees
ORDER BY id
LIMIT 10 OFFSET 20;
```

## 5. Группировка и агрегаты

### `GROUP BY`
Группирует строки
```sql
SELECT department_id, COUNT(*) as employee_count
FROM employees
GROUP BY department_id;
```

### `HAVING`
Фильтрует группы после `GROUP BY`
```sql
SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 100000;
```

### `COUNT`
Считает количество строк
```sql
SELECT COUNT(*)
FROM employees;
```

### `SUM`
Суммирует значения
```sql
SELECT SUM(budget)
FROM projects;
```

### `AVG`
Считает среднюю сумму
```sql
SELECT AVG(salary)
FROM employees;
```

### `MIN`
Минимальное значение
```sql
SELECT MIN(salary)
FROM employees;
```

### `MAX`
Максимальное значение
```sql
SELECT MAX(salary)
FROM employees;
```

### `DISTINCT`
Убирает дубликаты
```sql
SELECT DISTINCT department_id
FROM employees;
```

## 6. Соединение таблиц

### `JOIN`
Соединяет таблицы
```sql
SELECT e.name, d.name AS department
FROM employees AS e
JOIN departments d ON e.department_id = d.id;
```

### `INNER JOIN`
То же, что и обычный `JOIN`: показывает совпавшие строки
```sql
SELECT e.name, p.name AS project
FROM employees AS e
INNER JOIN projects p ON p.employee_id = e.id;
```

### `LEFT JOIN`
Показывает все строки из левой таблицы, даже если справа нет совпадений
```sql
SELECT e.name, p.name AS project
FROM employees AS e
LEFT JOIN projects p ON p.employee_id = e.id;
```

### `RIGHT JOIN`
Показывает все строки из правой таблицы, даже если слева нет совпадений
```sql
SELECT e.name, p.name AS project
FROM employees AS e
RIGHT JOIN projects p ON p.employee_id = e.id;
```

### `FULL JOIN`
Показывает все строки из обеих таблиц
```sql
SELECT e.name, p.name AS project
FROM employees AS e
FULL JOIN projects p ON p.employee_id = e.id;
```

### `ON`
Условие соединения
```sql
SELECT *
FROM employees AS e
JOIN departments d ON e.department_id = d.id;
```

## 7. Алиасы

### `AS`
Дает псевдоним колонки или таблицы
```sql
SELECT name AS employee_name,
    salary AS monthly_salary
FROM employees AS e;
```

```sql
SELECT e.name
FROM employees e;
```

## 8. Ограничение таблиц

### `PRIMARY KEY`
Главный ключ
```sql
CREATE TABLE departments(
    id SERIAL PRIMARY KEY,
    name TEXT
);
```

### `FOREIGN KEY`
Внешний ключ
```sql
CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    name TEXT,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```

### `REFERENCES`
Указывает на какую таблицу и колонку ссылается 
```sql
department_id INT REFERENCES departments(id);
```

### `NOT NULL`
Запрещает `NULL`
```sql
name TEXT NOT NULL;
```

### `NULL`
Отсутствует значение
```sql
INSERT INTO employees (name, salary, department_id)
VALUES ('Иван', NULL, 1);
```

### `UNIQUE`
Значение должно быть уникальным
```sql
ALTER TABLE employees
ADD CONSTRAINT unique_employee_email UNIQUE (email);
```

### `CONSTRAINT`
Дает имя ограничению
```sql
ALTER TABLE employees
ADD CONSTRAINT salary_positive CHECK (salary > 0);
```

### `CHECK`
Проверяет условие
```sql
ALTER TABLE employees
ADD CONSTRAINT salary_positive CHECK (salary > 0);
```

### `DEFAULT`
Значение по умолчанию
```sql
ALTER TABLE projects
ALTER COLUMN is_active SET DEFAULT TRUE;
```