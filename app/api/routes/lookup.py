from fastapi import APIRouter, HTTPException
from ...services import end_state_data

router = APIRouter()

@router.get("/", include_in_schema=True)
def test():
    return {
        "message": "Domain Lookup API - see /lookup?domain=example.com"
    }

@router.get("/url_lookup", include_in_schema=True)
def get_whois_report(domain_url: str | None = None):
    data = end_state_data(domain_url)
    if not data:
        raise HTTPException(
            status_code=400,
            detail="Invalid URL!",
        )
    return data