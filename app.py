from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app1 = Flask(__name__)

# 加載.env文件
load_dotenv()

# 從環境變量中獲取 Spotify 客戶端ID和密鑰
CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

# 設置Spotify API認證
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

@app1.route('/')
def index():
    # 獲取Spotify歌曲的URL
    track_url = get_spotify_track_url('Lauv - Molly In Mexico')
    return render_template('MollyInMexico.html', track_url=track_url)

def get_spotify_track_url(track_name):
    results = sp.search(q=track_name, limit=1)
    track = results['tracks']['items'][0]
    return track['external_urls']['spotify']

# 定義一個新路由，用於從content.txt文件中獲取內容
@app1.route('/get-content', methods=['GET'])
def get_content():
    try:
        # 使用with語句打開文件，這樣可以確保文件在讀取後被正確關閉
        with open(os.path.join('letter', 'content.txt'), 'r', encoding='utf-8') as file:
            content = file.read()
        # 返回文件內容作為JSON響應
        return jsonify({'content': content}), 200
    except Exception as e:
        # 如果出現任何錯誤，返回錯誤消息
        return jsonify({'error': str(e)}), 500

# 啟動Flask應用程序
if __name__ == '__main__':
    app1.run(debug=True)
