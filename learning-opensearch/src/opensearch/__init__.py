from .config import Config
from opensearchpy import OpenSearch

# Create our client for OpenSearch
client = OpenSearch(
    hosts = [{'host': Config.host, 'port': Config.port}],
    http_compress = True,
    http_auth = Config.auth,
    use_ssl = False # Don't use SSL for this one
)
