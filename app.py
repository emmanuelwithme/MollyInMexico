from flask import Flask, jsonify, render_template, request
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
    return render_template('index.html')

@app1.route('/ForRuth')
def ForRuth():
    # 獲取Spotify歌曲的URL
    track_url = get_spotify_track_url('Lauv - Molly In Mexico')
    return render_template('ForRuth.html', track_url=track_url)

@app1.route('/ForChin')
def ForTiffany():
    return render_template('ForChin.html')

def get_spotify_track_url(track_name):
    results = sp.search(q=track_name, limit=1)
    track = results['tracks']['items'][0]
    return track['external_urls']['spotify']

# 定義一個新路由，用於從letter/*.txt文件中獲取內容
@app1.route('/get-content', methods=['GET'])
def get_content():
    # 從GET請求的查詢參數中獲取文件路徑。
    # 例如，當前端發送請求到 /get-content?file_path=letter/content.txt，則 file_path 將會是 "letter/content.txt"
    file_path = request.args.get('file_path')
    
    # 安全檢查：確保請求的文件路徑是在 'letter/' 目錄下。
    # 這是為了防止使用者嘗試訪問其他不應被許可的目錄或文件。
    if not file_path.startswith('letter/'):
        return jsonify({'error': 'Invalid file path'}), 400

    try:
        # 使用with語句確保文件在操作後被正確關閉。
        with open(file_path, 'r', encoding='utf-8') as file:
            # 讀取文件內容
            content = file.read()
        # 返回文件內容作為JSON響應
        return jsonify({'content': content}), 200
    except Exception as e:
        # 如果讀取文件過程中出現錯誤，返回錯誤信息
        return jsonify({'error': str(e)}), 500

# 啟動Flask應用程序
if __name__ == '__main__':
    app1.run(debug=True)
