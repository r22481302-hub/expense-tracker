import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_MYSQL_PASSWORD",
    "database": "expense_tracker"
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def add_expense():
    expense_date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (expense_date, category, amount, description) VALUES (%s, %s, %s, %s)",
        (expense_date, category, amount, description)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("Expense added successfully.")

def view_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, expense_date, category, amount, description FROM expenses ORDER BY expense_date DESC, id DESC")
    rows = cursor.fetchall()

    if not rows:
        print("No expenses found.")
    else:
        print("\nID | Date | Category | Amount | Description")
        print("-" * 75)
        for row in rows:
            print(row)

    cursor.close()
    conn.close()

def search_by_category():
    category = input("Enter category: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, expense_date, category, amount, description FROM expenses WHERE category = %s ORDER BY expense_date DESC",
        (category,)
    )
    rows = cursor.fetchall()

    if not rows:
        print("No expenses found for this category.")
    else:
        for row in rows:
            print(row)

    cursor.close()
    conn.close()

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM expenses WHERE DATE_FORMAT(expense_date, '%Y-%m') = %s",
        (month,)
    )
    total = cursor.fetchone()[0]
    print(f"Total expenses for {month}: ₹{total:.2f}")
    cursor.close()
    conn.close()

def delete_expense():
    expense_id = int(input("Enter expense ID to delete: "))
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
    conn.commit()
    print("Expense deleted successfully." if cursor.rowcount else "Expense not found.")
    cursor.close()
    conn.close()

def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Monthly Summary")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                add_expense()
            elif choice == "2":
                view_expenses()
            elif choice == "3":
                search_by_category()
            elif choice == "4":
                monthly_summary()
            elif choice == "5":
                delete_expense()
            elif choice == "6":
                print("Program exited.")
                break
            else:
                print("Invalid choice.")
        except mysql.connector.Error as error:
            print("Database error:", error)
        except ValueError:
            print("Please enter valid values.")

if __name__ == "__main__":
    main()
