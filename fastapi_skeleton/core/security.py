

import secrets
from typing import Optional

from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from fastapi_skeleton.core import config
from fastapi_skeleton.core.messages import AUTH_REQ, NO_API_KEY

api_key = APIKeyHeader(name="token", auto_error=False)


def validate_request(header: Optional[str] = Security(api_key)) -> bool:
    authentication_status = False
    if header is None:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=NO_API_KEY, headers={}
        )
    for api_keys in str(config.API_KEY).split(','):
        if secrets.compare_digest(header, api_keys):
            authentication_status = True
    if not authentication_status:
        raise HTTPException(
                    status_code=HTTP_401_UNAUTHORIZED, detail=AUTH_REQ, headers={}
                )
    else:
        return True
