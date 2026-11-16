
from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re
import os

# Initialize FastAPI
app = FastAPI(
    title="Text Summarizer App",
    description="Text Summarization using T5",
    version="1.0"
)

# Model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "saved_summary_model")

# Select device
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print("Device:", device)

# Load model and tokenizer
print("Loading model...")

tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)

model.to(device)
model.eval()

print("Model loaded successfully!")

# HTML templates folder
templates = Jinja2Templates(directory="templates")


# Input schema
class DialogueInput(BaseModel):
    dialogue: str


# Clean input text
def clean_data(text):

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Remove line breaks
    text = re.sub(r"[\r\n]+", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove leading and trailing spaces
    text = text.strip()

    return text


# Generate summary
def summarize_dialogue(dialogue):

    # Clean text
    dialogue = clean_data(dialogue)

    if not dialogue:
        raise ValueError("Please enter some text.")

    # Prepare T5 input
    input_text = "summarize: " + dialogue

    # Tokenize
    inputs = tokenizer(
        input_text,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    )

    # Move inputs to device
    inputs = inputs.to(device)

    # Generate summary
    with torch.inference_mode():

        summary_ids = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=150,
            num_beams=4,
            early_stopping=True
        )

    # Decode summary
    summary = tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
    )

    return summary


# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


# Summarization API
@app.post("/summarize")
async def summarize(dialogue_input: DialogueInput):

    try:
        summary = summarize_dialogue(dialogue_input.dialogue)

        return {
            "summary": summary
        }

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except Exception as error:
        print("Summarization error:", error)
        raise HTTPException(
            status_code=500,
            detail="Failed to generate summary."
        )


# Run application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
