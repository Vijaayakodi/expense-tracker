from database import get_db_connection


class TransactionModel:

    @staticmethod
    def get_all_transactions():
        connection = get_db_connection()

        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT *
        FROM transactions
        ORDER BY transaction_date DESC, id DESC
        """

        cursor.execute(query)

        transactions = cursor.fetchall()

        cursor.close()
        connection.close()

        return transactions

    @staticmethod
    def get_transaction_by_id(transaction_id):
        connection = get_db_connection()

        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM transactions WHERE id = %s"

        cursor.execute(query, (transaction_id,))

        transaction = cursor.fetchone()

        cursor.close()
        connection.close()

        return transaction

    @staticmethod
    def create_transaction(data):
        connection = get_db_connection()

        cursor = connection.cursor()

        query = """
        INSERT INTO transactions
        (title, amount, type, category, transaction_date, notes)
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        values = (
            data["title"],
            data["amount"],
            data["type"],
            data["category"],
            data["transaction_date"],
            data.get("notes", "")
        )

        cursor.execute(query, values)

        connection.commit()

        transaction_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return transaction_id

    @staticmethod
    def update_transaction(transaction_id, data):
        connection = get_db_connection()

        cursor = connection.cursor()

        query = """
        UPDATE transactions
        SET
            title=%s,
            amount=%s,
            type=%s,
            category=%s,
            transaction_date=%s,
            notes=%s
        WHERE id=%s
        """

        values = (
            data["title"],
            data["amount"],
            data["type"],
            data["category"],
            data["transaction_date"],
            data.get("notes", ""),
            transaction_id
        )

        cursor.execute(query, values)

        connection.commit()

        affected = cursor.rowcount

        cursor.close()
        connection.close()

        return affected

    @staticmethod
    def delete_transaction(transaction_id):
        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM transactions WHERE id=%s",
            (transaction_id,)
        )

        connection.commit()

        affected = cursor.rowcount

        cursor.close()
        connection.close()

        return affected

    @staticmethod
    def get_summary():
        connection = get_db_connection()

        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                COALESCE(SUM(CASE WHEN type='Income' THEN amount END),0) AS total_income,
                COALESCE(SUM(CASE WHEN type='Expense' THEN amount END),0) AS total_expense
            FROM transactions
        """)

        summary = cursor.fetchone()

        summary["balance"] = (
            float(summary["total_income"])
            - float(summary["total_expense"])
        )

        cursor.close()
        connection.close()

        return summary