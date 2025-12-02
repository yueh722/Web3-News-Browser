import requests
import streamlit as st
import traceback

class NewsService:
    def __init__(self):
        self.N8N_WEBHOOK_READ = "https://n8n.defintek.io/webhook/read_news"
        self.N8N_WEBHOOK_UPDATE = "https://n8n.defintek.io/webhook/update_news"

    def fetch_news(self, date_str):
        """Fetch news for a specific date. Returns max 10 news items."""
        try:
            response = requests.get(self.N8N_WEBHOOK_READ, params={"date": date_str})
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and data:
                    if len(data) == 1 and "message" in data[0]:
                        return {"status": "success", "message": data[0]["message"], "data": []}
                    else:
                        # Normalize data structure and limit to 10 items
                        normalized_data = [item.get("json", item) for item in data]
                        limited_data = normalized_data[:10]  # Only take first 10 items
                        return {"status": "success", "data": limited_data}
                else:
                    return {"status": "warning", "message": "n8n 回傳資料為空"}
            else:
                return {"status": "error", "message": f"n8n 回應錯誤: {response.text}"}
        except Exception as e:
            return {"status": "error", "message": f"無法連線到 n8n 更新 : {e}", "traceback": traceback.format_exc()}
