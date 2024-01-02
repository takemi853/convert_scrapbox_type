from convert_scrapbox_type.main_gcp import convert_scrapbox_type

class MockRequest:
    def __init__(self, json_body, args=None):
        self._json = json_body
        self.args = args or {}

    def get_json(self, silent=False):
        return self._json

# JSONを使ってテスト
test_request_json = MockRequest({"text": "テスト用のテキスト"})
print(convert_scrapbox_type(test_request_json))

# URLパラメータを使ってテスト（必要に応じて）
test_request_args = MockRequest({}, {"text": "テスト用のテキスト"})
print(convert_scrapbox_type(test_request_args))
