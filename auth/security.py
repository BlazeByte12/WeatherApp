from fastapi import Header, HTTPException

def api_key_header(api_key: str = Header(None, alias="api-key")):
    if api_key is None:
        raise HTTPException(status_code=401, detail="You must login first")
    return api_key
