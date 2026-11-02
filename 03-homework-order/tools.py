# הפעולות בעולם האמיתי.
# המודל לעולם לא נכנס לכאן. הוא רק מבקש שנריץ.

import json

ORDERS = {
    "88": {
        "order_id": "88",
        "status": "במסירה",
        "city": "תל אביב",
        "eta": "היום עד 18:00",
    },
    "21": {
        "order_id": "21",
        "status": "הוכנה במחסן",
        "city": "חיפה",
        "eta": "מחר",
    },
}

SHIPPING = {
    "88": "שליח בדרך לתל אביב. אפשר ליצור קשר עד 18:00.",
    "21": "החבילה במחסן. תצא מחר בבוקר.",
}


def lookup_order(order_id: str) -> str:
    key = order_id.strip()
    data = ORDERS.get(key, {"order_id": key, "error": "ההזמנה לא במאגר"})
    return json.dumps(data, ensure_ascii=False)


def lookup_shipping(order_id: str) -> str:
    key = order_id.strip()
    info = SHIPPING.get(key, "לא נמצא מידע משלוח.")
    return json.dumps({"order_id": key, "shipping": info}, ensure_ascii=False)


def run_action(name: str, action_input: str) -> str:
    if name == "lookup_order":
        return lookup_order(action_input)
    if name == "lookup_shipping":
        return lookup_shipping(action_input)
    return json.dumps({"error": f"פעולה לא מוכרת: {name}"}, ensure_ascii=False)
