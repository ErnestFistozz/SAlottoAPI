from requests_html import HTMLSession


class LottoScrapper:
    def __init__(self, agent_str: str, lotto_type:  str, lotto_year: int, session: HTMLSession):
        self.agent_str = agent_str
        self.lotto_name = lotto_type
        self.draw_year = lotto_year
        self.url = f'https://za.national-lottery.com/{self.lotto_name}/results/{self.draw_year}-archive'
        self.session = session

    def lotto_results(self):
        req = self.session.get(
            self.url, headers={'user-agent': self.agent_str})
        return req.html.find('td.noBefore.balls')

    def draw_dates(self):
        req = self.session.get(
            self.url, headers={'user-agent': self.agent_str})
        return req.html.find('td.noBefore.colour')

    def lotto_outcomes(self):
        req = self.session.get(
            self.url, headers={'user-agent': self.agent_str})
        return req.html.find('td data-title:Jackpot')

    def lotto_jackpot(self):
        req = self.session.get(
            self.url, headers={'user-agent': self.agent_str})
        return req.html.find('td data-title:Outcome')
