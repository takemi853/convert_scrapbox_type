from fastapi import FastAPI
from pydantic import BaseModel
import spacy
# spaCyの言語モデルをロード
nlp = spacy.load("ja_core_news_sm")

app = FastAPI()

class Item(BaseModel):
    text: str

@app.post("/customize/")
async def customize(item: Item):
    doc = nlp(item.text)  # spaCyでテキストを解析
    new_text = ""
    for token in doc:
        if token.pos_ == "NOUN" or token.pos_ == "PROPN":
            new_text += "[" + token.text + "]"
        else:
            new_text += token.text
    return {"customized_text": new_text}
