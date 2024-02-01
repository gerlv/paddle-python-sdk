from typing import TYPE_CHECKING

from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Price                       import Price
from paddle_billing.Entities.Collections.Paginator       import Paginator
from paddle_billing.Entities.Collections.PriceCollection import PriceCollection
from paddle_billing.Entities.Shared.Status               import Status

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Prices.Operations.CreatePrice   import CreatePrice
from paddle_billing.Resources.Prices.Operations.ListPrices    import ListPrices
from paddle_billing.Resources.Prices.Operations.UpdatePrice   import UpdatePrice
from paddle_billing.Resources.Prices.Operations.List.Includes import Includes


if TYPE_CHECKING:
    from paddle_billing.Client import Client


class PricesClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, operation: ListPrices = None) -> PriceCollection:
        if operation is None:
            operation = ListPrices()

        self.response = self.client.get_raw('/prices', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return PriceCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), PriceCollection)
        )


    def get(self, price_id: str, includes = None) -> Price:
        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, Includes)]
        if invalid_items:
            raise InvalidArgumentException('includes', Includes.__name__, invalid_items)

        params        = {'include': ','.join(include.value for include in includes)} if includes else {}
        self.response = self.client.get_raw(f"/prices/{price_id}", params)
        parser        = ResponseParser(self.response)

        return Price.from_dict(parser.get_data())


    def create(self, operation: CreatePrice) -> Price:
        self.response = self.client.post_raw('/prices', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Price.from_dict(parser.get_data())


    def update(self, price_id: str, operation: UpdatePrice) -> Price:
        self.response = self.client.patch_raw(f"/prices/{price_id}", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Price.from_dict(parser.get_data())


    def archive(self, price_id: str) -> Price:
        return self.update(price_id, UpdatePrice(status=Status.Archived))