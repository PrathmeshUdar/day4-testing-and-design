"""BEFORE and AFTER of a messy function. Commit after each numbered step."""

# ---------- BEFORE: long function, magic numbers, mixed I/O and logic ------
def process(o):
    t = 0
    for i in o:
        t = t + i[0] * i[1]
    if t > 100:
        t = t * 0.9
    t = t + t * 0.2
    print("Total is", t)
    return t


# ---------- AFTER ---------------------------------------------------------
DISCOUNT_THRESHOLD = 100   # step 1: name the magic numbers
DISCOUNT_RATE = 0.10
TAX_RATE = 0.20


def subtotal(items):       # step 2: extract pure functions (one job each)
    return sum(price * qty for price, qty in items)


def apply_discount(amount):
    return amount * (1 - DISCOUNT_RATE) if amount > DISCOUNT_THRESHOLD else amount


def add_tax(amount):
    return amount * (1 + TAX_RATE)


def order_total(items):    # step 3: logic only, no print
    return add_tax(apply_discount(subtotal(items)))


if __name__ == "__main__":  # step 4: I/O lives at the edge
    print("Total is", order_total([(30, 2), (25, 3)]))
