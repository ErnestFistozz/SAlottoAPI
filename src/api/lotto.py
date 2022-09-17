class LottoObject:
    def __init__(self, type: str, date: dict, results: list[int]):
        self._lotto_type = type
        self._draw_date = date
        self._results = results

    def format_lotto(self):
        return f'{self._draw_date}, {self._results}'
