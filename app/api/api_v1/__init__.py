from fastapi import Depends, APIRouter

from . import flexit_auth, flexit_queries

api_router = APIRouter()
api_router.include_router(flexit_auth.router)
api_router.include_router(
    flexit_queries.router,
    prefix="/queries",
    dependencies=[Depends(flexit_auth.get_current_active_user)],
)
