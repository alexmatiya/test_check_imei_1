from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import APIKeyHeader
from ..core.imei_validator import IMEIValidator
from ..core.imei_service import IMEIService
from ..core.config import settings

router = APIRouter()
api_key_header = APIKeyHeader(name="X-API-Token")


async def verify_token(api_key: str = Depends(api_key_header)):
    if api_key not in settings.API_ACCESS_TOKENS:
        raise HTTPException(status_code=403, detail="Invalid API token")
    return api_key


@router.post("/check-imei")
async def check_imei(imei: str, token: str = Depends(verify_token)):
    """
    Проверка IMEI устройства.
    
    Args:
        imei: IMEI номер устройства (15 цифр)
        token: Токен для авторизации
    
    Returns:
        dict: Информация об устройстве
    """
    if not IMEIValidator.is_valid(imei):
        raise HTTPException(status_code=400, detail="Неверный формат IMEI. Пожалуйста, проверьте номер. Пример правильного ввода: 356735111052198")

    imei_service = IMEIService()
    result = await imei_service.check_imei(imei)
    return result


@router.get("/health")
async def health_check():
    """
    Проверка работоспособности сервиса.
    """
    return {"status": "ok"}
