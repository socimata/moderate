from ..store import Endpoint


def new_client(endpoint: Endpoint):
    from httpx import AsyncClient

    return AsyncClient(base_url=str(endpoint["base_url"]), headers={"Authorization": f"Bearer {endpoint['api_key']}"}, timeout=60, http2=True, follow_redirects=True)
