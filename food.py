from flask import Flask, render_template_string, request

app = Flask(__name__)

class Food:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def category(self):
        return "อาหารทั่วไป"

class MainCourse(Food):
    def category(self):
        return "อาหารจานหลัก"


class Dessert(Food):
    def category(self):
        return "ของหวาน"

foods = [
    MainCourse("ผัดไทย", "เส้นจันท์ผัดกุ้งสด"),
    MainCourse("ข้าวมันไก่", "ไก่นุ่ม น้ำจิ้มสูตรเด็ด"),
    Dessert("บัวลอย", "กะทิหวานหอม"),
    Dessert("ไอศกรีม", "วานิลลาหอมสดชื่น")
]

@app.route("/", methods=["GET", "POST"])
def home():
    selected = None

    if request.method == "POST":
        food_name = request.form.get("food")
        for food in foods:
            if food.name == food_name:
                selected = food

    with open("index.html", encoding="utf-8") as f:
        template = f.read()

    return render_template_string(template, foods=foods, selected=selected)
