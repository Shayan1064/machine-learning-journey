from flask import Flask, render_template, request
import torch
import torch.nn.functional as F
from PIL import Image
import torchvision.transforms as transforms

from model import CNN


app = Flask(__name__)


# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# Create model
model = CNN()

# Load trained model
model.load_state_dict(
    torch.load("cnn_model.pth", map_location=device)
)

model = model.to(device)
model.eval()


# CIFAR-10 classes
classes = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck"
]


# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize(
        (0.5, 0.5, 0.5),
        (0.5, 0.5, 0.5)
    )
])


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None

    if request.method == "POST":

        file = request.files["image"]

        if file:

            image = Image.open(file).convert("RGB")

            image_tensor = transform(image)

            image_tensor = image_tensor.unsqueeze(0)

            image_tensor = image_tensor.to(device)

            with torch.no_grad():

                output = model(image_tensor)

                probabilities = F.softmax(output, dim=1)

                confidence_value, predicted_class = torch.max(
                    probabilities, 1
                )

            prediction = classes[predicted_class.item()]

            confidence = round(
                confidence_value.item() * 100,
                2
            )

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)