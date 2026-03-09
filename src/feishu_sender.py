"""
Feishu Sender Module
Send messages to Feishu
"""
import requests
from typing import Optional

def get_tenant_access_token(app_id: str, app_secret: str) -> Optional[str]:
    """Get Feishu tenant access token"""
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    data = {
        "app_id": app_id,
        "app_secret": app_secret
    }
    
    try:
        response = requests.post(url, json=data, timeout=30)
        if response.status_code == 200:
            result = response.json()
            if result.get("code") == 0:
                return result.get("tenant_access_token")
    except Exception as e:
        print(f"Error getting Feishu token: {e}")
    return None

def send_message(
    token: str,
    user_id: str,
    message: str,
    msg_type: str = "text"
) -> bool:
    """Send message to Feishu user"""
    url = "https://open.feishu.cn/open-apis/im/v1/messages"
    params = {"receive_id_type": "open_id"}
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    
    data = {
        "receive_id": user_id,
        "msg_type": msg_type,
        "content": '{"text": "' + message.replace('"', '\\"') + '"}'
    }
    
    try:
        response = requests.post(url, params=params, json=data, headers=headers, timeout=30)
        return response.status_code == 200 and response.json().get("code") == 0
    except Exception as e:
        print(f"Error sending Feishu message: {e}")
        return False

def send_file(
    token: str,
    user_id: str,
    file_path: str
) -> bool:
    """Send file to Feishu user"""
    # Step 1: Upload file
    upload_url = "https://open.feishu.cn/open-apis/im/v1/files"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(upload_url, headers=headers, files=files, timeout=60)
        
        if response.status_code != 200:
            return False
        
        file_key = response.json().get("data", {}).get("file_key")
        if not file_key:
            return False
        
        # Step 2: Send file message
        msg_url = "https://open.feishu.cn/open-apis/im/v1/messages"
        params = {"receive_id_type": "open_id"}
        data = {
            "receive_id": user_id,
            "msg_type": "file",
            "content": f'{{"file_key": "{file_key}"}}'
        }
        
        response = requests.post(msg_url, params=params, json=data, headers=headers, timeout=30)
        return response.status_code == 200
    
    except Exception as e:
        print(f"Error sending file: {e}")
        return False

if __name__ == "__main__":
    print("Feishu Sender ready")
