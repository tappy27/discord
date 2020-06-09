# nekobot
discord × ドラクエ10 をする人のためのdiscord bot  
暇なときに新機能を追加するかもしれない

## usage
discordのテキストチャットでコマンドを入力します  
現在用意されているのがこちら   

/neko ... にゃーんと出ます  

/yohou ... つよさ予報を出します 

/souba アイテム名 ... 現在のバザー価格と直近の変動をグラフで出します  
       rank      ... 現在の通泥レア泥の価格ランキングを出します  
　　　　update    ... 現在使っているデータベース(csv)を最新に更新します  

/monster モンスター名 ... そのモンスターの生息地リスト，モンスター情報のリンクを出します(攻略の虎)  

/map マップ名 ... そのマップの地図，地図情報のリンクを出します(攻略の虎)  


## install
python3が動く環境なら動くはずです  
python3.8.1で動作確認済  

1. python3をインストール  
適当にインストールしてください  
win10であれば，https://www.python.org/downloads/windows/ のlatestをインストールすれば良いと思います  
インストーラの途中に出てくる"Add Python 3.x to PATH" にチェックを付けてください  
コマンドプロンプト等を開いて `python --version` と入力し，"Python 3.x.x" と出たらok  

2. パッケージのダウンロード  
まず、このディレクトリごとダウンロードした後，コマンドプロンプト等でダウンロードしたディレクトリに移動してください  
上記の方法でpython3を入れたならpipが入っているはずなので  
`pip install discord`  
`pip install requests`  
`pip install BeautifulSoup4`  
`pip install pandas`  

とやって必要なパッケージをダウンロードしてください  

3. bot作成  
discordにbotアカウントを作ってください  
[この記事](https://note.com/bami55/n/ncc3a68652697)が分かりやすいです  
botが作れたら，何かしらのエディタでneko.pyを開いてください 
プログラムの最初のほうにある`TOKEN = 'your-token'`の your-token を削除してbotのtokenを貼り付けてください．  
`python neko.py`とやって"ログイン完了"の文字が出たら正しく動作しています．  
