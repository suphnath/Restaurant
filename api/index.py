from flask import Flask, request

app = Flask(__name__)

# ===== คลาสแม่ =====
class Food:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"อาหาร: {self.name}"


# ===== คลาสลูก 1 =====
class ThaiFood(Food):
    def info(self):
        return f"อาหารไทย: {self.name} 🍜"


# ===== คลาสลูก 2 =====
class JapaneseFood(Food):
    def info(self):
        return f"อาหารญี่ปุ่น: {self.name} 🍣"


@app.route("/", methods=["GET"])
def home():
    return """
    <html>
        <head>
            <title>Restaurant</title>
        </head>
        <body>
            <h1>เลือกร้านอาหาร</h1>
            <form action="/show" method="post">
                <button name="type" value="thai">อาหารไทย</button>
                <button name="type" value="japan">อาหารญี่ปุ่น</button>
            </form>
        </body>
    </html>
    """


@app.route("/show", methods=["POST"])
def show():
    food_type = request.form.get("type")

    if food_type == "thai":
        food = ThaiFood("ผัดไทย")
    else:
        food = JapaneseFood("ซูชิ")

    return f"""
    <html>
        <body>
            <h2>{food.info()}</h2>
            <a href="/">กลับหน้าแรก</a>
        </body>
    </html>
    """