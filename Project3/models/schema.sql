-- Create a table for users and hashed passwords:
CREATE TABLE IF NOT EXISTS users (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    username    TEXT                NOT NULL,
    hash_password TEXT              NOT NULL
);

-- Create a table for the tasks and the associated user id:
CREATE TABLE IF NOT EXISTS tasks (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER             NOT NULL,
    task        TEXT                NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

