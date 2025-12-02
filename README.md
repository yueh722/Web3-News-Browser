# Web3 News Browsing App

一個簡潔的 Web3 新聞瀏覽應用程式，每日最多顯示 10 則精選新聞。

## 功能特色

- 📰 自動載入當日新聞
- 🔢 最多顯示 10 則新聞
- 📅 可選擇日期查看歷史新聞
- 🎨 深色主題界面
- 📱 支援手機瀏覽

## 如何使用

### 本地運行

```bash
# 安裝依賴
pip install -r requirements.txt

# 運行應用
streamlit run NewsBrowsingApp.py
```

### 部署到 Streamlit Cloud

1. 將此 repository 推送到 GitHub
2. 前往 [share.streamlit.io](https://share.streamlit.io)
3. 使用 GitHub 帳號登入
4. 點擊 "New app"
5. 選擇此 repository
6. 主文件路徑設定為：`NewsBrowsingApp.py`
7. 點擊 "Deploy"

## 檔案結構

- `NewsBrowsingApp.py` - 主應用程式
- `news_service.py` - 新聞服務 API
- `utils.py` - 工具函數（CSS、滑動偵測）
- `requirements.txt` - Python 依賴套件

## 技術棧

- Streamlit - Web 應用框架
- Requests - HTTP 請求
- n8n - 後端 API 服務
