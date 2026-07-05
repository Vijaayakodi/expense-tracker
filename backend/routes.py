from flask import Blueprint, request, jsonify
from models import TransactionModel

transaction_bp = Blueprint("transactions", __name__)


# ==========================
# GET ALL TRANSACTIONS
# ==========================
@transaction_bp.route("/transactions", methods=["GET"])
def get_all_transactions():
    try:
        transactions = TransactionModel.get_all_transactions()

        return jsonify({
            "success": True,
            "count": len(transactions),
            "data": transactions
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# ==========================
# GET SINGLE TRANSACTION
# ==========================
@transaction_bp.route("/transactions/<int:transaction_id>", methods=["GET"])
def get_transaction(transaction_id):

    transaction = TransactionModel.get_transaction_by_id(transaction_id)

    if transaction:
        return jsonify({
            "success": True,
            "data": transaction
        }), 200

    return jsonify({
        "success": False,
        "message": "Transaction not found"
    }), 404


# ==========================
# CREATE TRANSACTION
# ==========================
@transaction_bp.route("/transactions", methods=["POST"])
def create_transaction():
    try:
        data = request.get_json()

        required_fields = [
            "title",
            "amount",
            "type",
            "category",
            "transaction_date"
        ]

        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "message": f"{field} is required"
                }), 400

        transaction_id = TransactionModel.create_transaction(data)

        return jsonify({
            "success": True,
            "message": "Transaction created successfully",
            "transaction_id": transaction_id
        }), 201

    except Exception as e:
        print("CREATE ERROR:", e)

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

# ==========================
# UPDATE TRANSACTION
# ==========================
@transaction_bp.route("/transactions/<int:transaction_id>", methods=["PUT"])
def update_transaction(transaction_id):

    data = request.get_json()

    updated = TransactionModel.update_transaction(transaction_id, data)

    if updated:
        return jsonify({
            "success": True,
            "message": "Transaction updated successfully"
        }), 200

    return jsonify({
        "success": False,
        "message": "Transaction not found"
    }), 404


# ==========================
# DELETE TRANSACTION
# ==========================
@transaction_bp.route("/transactions/<int:transaction_id>", methods=["DELETE"])
def delete_transaction(transaction_id):

    deleted = TransactionModel.delete_transaction(transaction_id)

    if deleted:
        return jsonify({
            "success": True,
            "message": "Transaction deleted successfully"
        }), 200

    return jsonify({
        "success": False,
        "message": "Transaction not found"
    }), 404


# ==========================
# SUMMARY
# ==========================
@transaction_bp.route("/summary", methods=["GET"])
def get_summary():
    try:
        summary = TransactionModel.get_summary()

        return jsonify({
            "success": True,
            "data": summary
        }), 200

    except Exception as e:
        print("SUMMARY ERROR:", e)

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500