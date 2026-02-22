import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from tensorflow.keras.preprocessing import image

model = MobileNetV2(weights="imagenet")


def predict_food(image_path: str):
    try:
        img = image.load_img(image_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        decoded = decode_predictions(preds, top=1)

        label = decoded[0][0][1]  # predicted label
        confidence = float(decoded[0][0][2])

        return label, confidence
    except Exception as e:
        print(f"Error processing image: {e}")
        return "unknown", 0.0


nutrition_db = {
    "pizza": {"calories": 285, "protein": 12, "carbs": 33, "fat": 10},
    "burger": {"calories": 295, "protein": 17, "carbs": 30, "fat": 14},
    "apple": {"calories": 95, "protein": 0.5, "carbs": 25, "fat": 0.3},
    "banana": {"calories": 105, "protein": 1.3, "carbs": 27, "fat": 0.4},
    "salad": {"calories": 150, "protein": 5, "carbs": 20, "fat": 6}
}


def get_nutrition(label: str):
    for key in nutrition_db:
        if key in label.lower():
            return nutrition_db[key]
    return {
        "calories": 200,
        "protein": 5,
        "carbs": 25,
        "fat": 8
    }