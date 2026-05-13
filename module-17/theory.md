# База данных

### `CREATE`
Создает объект: таблица, база, индекс
```sql
CREATE TABLE employess (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  salary NUMERIC
);
```

### `TABLE`
Указывает что создается изменяется таблица
```sql
CREATE TABLE departments (
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
CREATE TABLE IF NOT EXISTS departments (
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