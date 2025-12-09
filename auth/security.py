from fastapi import Header, HTTPException

API_KEY_NAME = "X-API-KEY"

def api_key_header(api_key: str = Header(None)):
    if api_key is None:
        raise HTTPException(status_code=401, detail="API key is missing.")
    return api_key
