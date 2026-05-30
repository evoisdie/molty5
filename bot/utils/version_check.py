"""
Version check — GET /api/version and X-Version header management.
Returns 426 VERSION_MISMATCH if outdated.
"""
import httpx
from bot.config import get_server_version
from bot.utils.logger import get_logger

log = get_logger(__name__)


async def check_version(client: httpx.AsyncClient) -> str:
    """Return the cached server version (already fetched at startup)."""
    return get_server_version()


def get_version_header() -> dict:
    """Return X-Version header dict using the live server version."""
    return {"X-Version": get_server_version()}
