import random
import socket
from typing import Any, List, Optional, Tuple

from proxy.common.utils import new_socket_connection
from proxy.http.parser import HttpParser
from proxy.plugin.proxy_pool import ProxyPoolPlugin

from utils import ProxyList


class ProxyPool(ProxyPoolPlugin):
    """Proxy incoming requests separating each tab from the browser by tab.id"""

    UPSTREAM_PROXY_POOL: List[Tuple[str, int]] = []
    conn: Optional[socket.socket]
    active_sockets: List[str]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        proxy_list = ProxyList()
        self.UPSTREAM_PROXY_POOL = proxy_list.get_proxies()

    def _is_active_socket(self):
        pass

    def before_upstream_connection(self, request: HttpParser) -> Optional[HttpParser]:
        """
        Establish connection to random proxy from `proxy_list`
        """
        self.conn = new_socket_connection(
            random.choice(self.UPSTREAM_PROXY_POOL))
        return None
