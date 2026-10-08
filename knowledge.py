"""Static reference content: vitamin info, food suggestions and food groups."""

VITAMINS = {
    "A": {
        "name": "Vitamin A", "icon": "🥕", "color": "#f59e0b",
        "role": "Supports vision, immunity and healthy skin.",
        "symptoms": "Night blindness, dry eyes, rough skin, frequent infections.",
        "foods": ["Carrots", "Sweet potato", "Spinach", "Mango", "Papaya", "Eggs", "Fortified milk"],
    },
    "B": {
        "name": "Vitamin B (B12)", "icon": "🥚", "color": "#ec4899",
        "role": "Needed for red blood cells, nerves and energy metabolism.",
        "symptoms": "Fatigue, tingling hands or feet, pale skin, poor memory.",
        "foods": ["Eggs", "Milk and curd", "Paneer", "Fish", "Chicken", "Fortified cereals"],
    },
    "C": {
        "name": "Vitamin C", "icon": "🍊", "color": "#f97316",
        "role": "Helps wound healing, iron absorption and immune defence.",
        "symptoms": "Bleeding gums, easy bruising, slow healing, tiredness.",
        "foods": ["Amla (gooseberry)", "Guava", "Oranges", "Lemon", "Bell peppers", "Kiwi", "Strawberries"],
    },
    "D": {
        "name": "Vitamin D", "icon": "☀️", "color": "#eab308",
        "role": "Keeps bones and muscles strong by aiding calcium absorption.",
        "symptoms": "Bone or back pain, muscle weakness, low mood, frequent illness.",
        "foods": ["Safe morning sunlight", "Fatty fish (salmon, sardines)", "Egg yolk", "Fortified milk", "Mushrooms"],
    },
    "E": {
        "name": "Vitamin E", "icon": "🌰", "color": "#84cc16",
        "role": "An antioxidant that protects cells and supports skin and immunity.",
        "symptoms": "Muscle weakness, vision problems, numbness, dry skin.",
        "foods": ["Almonds", "Sunflower seeds", "Peanuts", "Avocado", "Spinach", "Vegetable oils"],
    },
    "K": {
        "name": "Vitamin K", "icon": "🥬", "color": "#10b981",
        "role": "Essential for blood clotting and bone health.",
        "symptoms": "Easy bruising, nosebleeds, heavy bleeding, slow clotting.",
        "foods": ["Spinach", "Fenugreek (methi) leaves", "Broccoli", "Cabbage", "Kale", "Soybeans"],
    },
}

ORDER = ["A", "B", "C", "D", "E", "K"]

# Group ids come from the training dataset (data/food_groups.csv).
FOOD_GROUPS = {
    1: ("Fruits & dry fruits", "🍎", "Fresh seasonal fruit plus nuts and dried fruit."),
    2: ("Plant-based variety", "🥗", "Fruits, vegetables, cereals, millets and dry fruits."),
    3: ("Dairy, protein & dry fruits", "🥛", "Milk, curd, cheese, eggs or meat with dry fruits."),
    4: ("Full balanced plate", "🍽️", "Fruits, vegetables, whole grains, millets, dry fruits, dairy and protein."),
    5: ("Grains, veg, dairy & protein", "🌾", "Cereals, millets, vegetables, dry fruits, dairy and protein."),
    6: ("Grains, veg & dry fruits", "🥦", "Whole cereals, millets, vegetables and dry fruits."),
}

DISCLAIMER = (
    "This tool gives an educational estimate from a machine-learning model trained on a "
    "sample dataset. It is not a medical diagnosis. Please confirm any result with a "
    "laboratory test and consult a qualified doctor or dietitian before changing your diet "
    "or taking supplements."
)
