session = HTMLSession()

query = {
    'lotto_type': 'lotto',
    'year': 2021
}

macOs_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

lotto = query['lotto_type']
lotto_year = query['year']
query_url = f'https://za.national-lottery.com/{lotto}/results/{lotto_year}-archive'
req = session.get(query_url, headers={
    'user-agent': macOs_agent
})
draw_date = req.html.find('td.noBefore.colour')
results = req.html.find('td.noBefore.nowrap')

draw_dates = [date.text for date in draw_date]
list_of_results = [result.text for result in results]
lotto_size = len(draw_dates)
for index in range(lotto_size):
    print(f'date: {draw_dates[index]} - numbers:{list_of_results[index]}')
