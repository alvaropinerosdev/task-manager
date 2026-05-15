CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    phone VARCHAR(30)
);


CREATE TABLE status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(150) NOT NULL,
    description TEXT,

    status_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,

    started_date DATE NOT NULL,
    active BOOLEAN NOT NULL DEFAULT 1,

    FOREIGN KEY (status_id)
        REFERENCES status(id),

    FOREIGN KEY (category_id)
        REFERENCES categories(id),

    FOREIGN KEY (user_id)
        REFERENCES users(id)
);


CREATE TABLE repeat_rules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    task_id INTEGER NOT NULL UNIQUE,

    active BOOLEAN NOT NULL DEFAULT 1,

    frequency VARCHAR(20) NOT NULL,

    interval INTEGER NOT NULL DEFAULT 1,

    repeat_days TEXT,

    FOREIGN KEY (task_id)
        REFERENCES tasks(id),

    CHECK (
        frequency IN (
            'daily',
            'weekly',
            'monthly',
            'yearly'
        )
    )
);


CREATE TABLE task_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    task_id INTEGER NOT NULL,

    date DATE NOT NULL,

    completed BOOLEAN NOT NULL DEFAULT 0,

    FOREIGN KEY (task_id)
        REFERENCES tasks(id),

    UNIQUE(task_id, date)
);


INSERT INTO status (name)
VALUES
    ('pending'),
    ('completed'),
    ('cancelled');


INSERT INTO categories (name)
VALUES
    ('Work'),
    ('Study'),
    ('Personal'),
    ('Health'),
    ('Gym');