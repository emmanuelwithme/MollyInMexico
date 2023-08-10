from flask import Flask, jsonify, render_template
import os

app1 = Flask(__name__)

# 定義根路由，這將渲染HTML模板
@app1.route('/')
def index():
    return render_template('MollyInMexico.html')

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
