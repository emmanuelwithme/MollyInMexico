# MollyInMexico Flask App

這是一個簡單的 Flask 應用程序，用於顯示一段熱烈的抒情文，表達強烈的愛意。

## 功能

- 顯示一段抒情文，該消息從 `content.txt` 文件中獲取。
- 使用 Google 字體美化文本。
- 有一個 YouTube 背景音樂播放器。

## 設定

以下是一些主要的設定選項，你可以在 `/templates/MollyInMexico.html` 文件中找到它們：

- **字體大小**: 透過 CSS 變數 `--font-size` 進行設定。預設值為 `30px`。
- **段落左右留白**: 透過 CSS 變數 `--text-padding` 進行設定。預設值為 `30px`。
- **打字機打字速度**: 在 JavaScript 部分透過 `typingSpeed` 變數進行設定。預設值每個字輸出速度為 `200`（毫秒）。

## 檔案結構

```
/MollyInMexico/
    app.py
    Procfile
    README.md
    requirements.txt
    runtime.txt
    /letter/
        content.txt
    /templates/
        MollyInMexico.html
```

## 安裝和運行

1. 克隆此存儲庫：

```bash
git clone [你的存儲庫URL]
cd MollyInMexico
```

2. 安裝所需的依賴項：

```bash
pip install -r requirements.txt
```

3. 運行 Flask 應用程序：

```bash
python app.py
```

你的應用程序現在應該在 `http://127.0.0.1:5000/` 上運行。

## 部署

此應用程序包含一個 `Procfile`，這意味著它可以輕鬆地部署到 [Heroku](https://www.heroku.com/) 或其他平台。

## 貢獻

如果你有任何建議或更改，請提交 pull 請求或開放問題。

## 許可證

此項目使用 MIT 許可證。有關詳細信息，請參見 `LICENSE` 文件。
