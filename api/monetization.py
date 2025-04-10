# api/monetization.py

from flask import Blueprint, jsonify, request
import stripe
import os
from dotenv import load_dotenv

load_dotenv()
monetization_bp = Blueprint("monetization", __name__)

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@monetization_bp.route("/api/create-checkout-session", methods=["POST"])
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="subscription",
            line_items=[
                {
                    "price": os.getenv("STRIPE_PRICE_ID"),
                    "quantity": 1,
                }
            ],
            success_url=request.json.get("success_url"),
            cancel_url=request.json.get("cancel_url"),
        )
        return jsonify({"sessionId": session.id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
