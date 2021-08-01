import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.next1step.com/category/python/scraping_sample_page/'

# 指定したURLにrequestsを出す（成功すると200番が返る）
res = requests.get(url)

# BeautifulSoupでhtml構造をパースする
soup = BeautifulSoup(res.text, 'html.parser')

# 要素を指定して、情報を取得する
## タグ指定：h2要素を取得する
elems = soup.find_all('h2')
elem = elems[0]

print(elem.text)

## class指定：
elem = soup.find('div', class_='ep-box')
print(elem.text)

## liの取得
elems = soup.find_all('li')

for elem in elems:
    print(elem.text)

elems = soup.find('article').find_all('li')

for elem in elems:
    print(elem.text)

# 画像をダウンロードする
elem = soup.find('img', alt='へびせんせいのサンプル画像')
img_url = url + elem.get('src')

img = requests.get(img_url).content

with open('./sample.png', 'wb') as f:
    f.write(img)

# テーブルの情報を取得する
dfs = pd.read_html(url)
df = dfs[0]

df.to_csv('./sample.csv', index=False)
print(df)

# テキストボックスに文字を入力し、ボタンを押す
data = {
    'name' : 'かばくん',
    'mail' : 'kabakun@xxxxxx.xx'
}

next_url = 'https://www.next1step.com/category/python/scraping_sample_page/sample.php'
ses = requests.Session()
res = ses.post(next_url, data=data)

print(res.text)