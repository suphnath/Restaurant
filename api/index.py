from flask import Flask, render_template, request

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

class Food:
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"อาหาร: {self.name}"

class ThaiFood(Food):
    def show(self):
        return f"อาหารไทย: {self.name} 🍜"

class ItalianFood(Food):
    def show(self):
        return f"อาหารอิตาลี: {self.name} 🍕"

@app.route("/", methods=["GET", "POST"])
def home():
    message = None

    if request.method == "POST":
        food_type = request.form.get("type")

        if food_type == "thai":
            food = ThaiFood("ผัดไทย")
        else:
            food = ItalianFood("พิซซ่า")

        message = food.show()

    return render_template("index.html", message=message)