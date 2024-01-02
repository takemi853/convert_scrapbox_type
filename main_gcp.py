import spacy

# モデルのローカルパスで読み込み
# nlp = spacy.load('/home/takemi/.pyenv/versions/anaconda3-2021.11/envs/lifelog/lib/python3.10/site-packages/ja_core_news_sm')
nlp = spacy.load("ja_core_news_sm")

def convert_scrapbox_type(request):
    # HTTPリクエストからJSONとしてテキストを取得
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'text' in request_json:
        text = request_json['text']
    elif request_args and 'text' in request_args:
        text = request_args['text']
    else:
        return 'No text provided', 400  # 適切なテキストが提供されなかった場合のエラー

    # spaCyでテキストを解析
    doc = nlp(text)
    new_text = ""
    for token in doc:
        if token.pos_ == "NOUN" or token.pos_ == "PROPN":
            new_text += "[" + token.text + "]"
        else:
            new_text += token.text

    return new_text
