from magento import MagentoAPI
#  https://pypi.org/project/python-magento/
from tap_magento.context import Context
from tap_magento.streams.base import Stream


# Create an instance of API
client = MagentoAPI("magentohost.com", 80, "test_api_user", "test_api_key")

class Invoice(Stream):
    name = 'invoice'
    replication_object = client.invoice

Context.stream_objects['invoice'] = Invoice