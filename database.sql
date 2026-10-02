CREATE DATABASE IF NOT EXISTS expense_tracker;
USE expense_tracker;

CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE NOT NULL,
    category VARCHAR(50) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    description VARCHAR(255)
);

INSERT INTO expenses (expense_date, category, amount, description)
VALUES
('2026-10-01', 'Food', 250.00, 'Lunch'),
('2026-10-01', 'Travel', 120.00, 'Bus fare');
