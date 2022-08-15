import csv
from enum import Enum

class CATEGORY(Enum):
    FEES = "كهربا وغاز"
    EATING_OUT = "خروجات"
    SELF_DEVELOPMENT = "تطوير ذات وأدوات عمل"
    FOOD = "الأكل"
    HEALTH = "الصحة"
    PHONE = "باقة الموبايل والانترنت"
    CAR = "بنزين واصلاحات"
    CLOTHES = "ملابس"
    MISC = "تكاليف خاصة بالعمل"
    SHOPPING = "تسوق"
    HOUSING = "مصاريف المنزل"
    ENTERTAINMENT = "رفاهية"
    Savings = "مدخرات"
    Investment = "أستثمار"


class IMPORTANCE(Enum):
    SHOULDNT_HAVE = "Shouldn't Have"
    NICE_TO_HAVE = "Nice to Have"
    HAVE_TO_HAVE = "Have to Have"
    ESSENTIAL = "Essential"


class Expense:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.category, self.importance = self._determine_category_and_importance()

    def _determine_category_and_importance(self):
        item = self.item.lower()
        if "fee" in item:
            return CATEGORY.FEES, IMPORTANCE.SHOULDNT_HAVE
        if "uber eats" in item or "pizza" in item or "date" in item:
            return CATEGORY.EATING_OUT, IMPORTANCE.NICE_TO_HAVE
        if "book" in item:
            return CATEGORY.SELF_DEVELOPMENT, IMPORTANCE.NICE_TO_HAVE
        if "groceries" in item:
            return CATEGORY.FOOD, IMPORTANCE.ESSENTIAL
        if "gym" in item:
            return CATEGORY.HEALTH, IMPORTANCE.HAVE_TO_HAVE
        if "phone" in item:
            return CATEGORY.PHONE, IMPORTANCE.ESSENTIAL
        if  "car" in item:
            return CATEGORY.CAR, IMPORTANCE.HAVE_TO_HAVE
        if "clothes" in item:
            return CATEGORY.CLOTHES, IMPORTANCE.NICE_TO_HAVE
        if "movies" in item:
            return CATEGORY.ENTERTAINMENT, IMPORTANCE.NICE_TO_HAVE
        if "ikea" in item:
            return CATEGORY.SHOPPING, IMPORTANCE.NICE_TO_HAVE
        if "house" in item:
            return CATEGORY.HOUSING, IMPORTANCE.ESSENTIAL
        if "internet" in item:
            return CATEGORY.PHONE, IMPORTANCE.ESSENTIAL
        return CATEGORY.MISC, IMPORTANCE.NICE_TO_HAVE


    def __repr__(self) -> str:
        return f"{self.item},{self.category.value},{self.price},{self.importance.value}"

def get_data():
    with open('expenses.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        expenses = []
        for row in reader:
            expenses.append(Expense(row[0], row[1]))

    return expenses