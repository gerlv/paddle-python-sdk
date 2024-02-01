from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Entities.Entity             import Entity

from paddle_billing.Entities.Collections.PriceCollection import PriceCollection

from paddle_billing.Entities.Shared.CatalogType import CatalogType
from paddle_billing.Entities.Shared.CustomData  import CustomData
from paddle_billing.Entities.Shared.ImportMeta  import ImportMeta
from paddle_billing.Entities.Shared.Status      import Status
from paddle_billing.Entities.Shared.TaxCategory import TaxCategory


@dataclass
class Product(Entity):
    id:           str
    name:         str
    status:       Status
    tax_category: TaxCategory
    description:  str             | None
    image_url:    str             | None
    created_at:   datetime        | None = None
    custom_data:  CustomData      | None = None
    import_meta:  ImportMeta      | None = None
    prices:       PriceCollection | None = None
    type:         CatalogType     | None = None


    @classmethod
    def from_dict(cls, data: dict) -> Product:
        return Product(
            description  = data.get('description'),
            id           = data['id'],
            image_url    = data.get('image_url'),
            name         = data['name'],
            status       = Status(data['status']),
            tax_category = TaxCategory(data['tax_category']),
            prices       = PriceCollection(data['prices'])            if data.get('prices')      else [],
            type         = CatalogType(data['type'])                  if data.get('type')        else None,
            custom_data  = CustomData(data['custom_data'])            if data.get('custom_data') else None,
            created_at   = datetime.fromisoformat(data['created_at']) if data.get('created_at')  else None,
            import_meta  = ImportMeta.from_dict(data['import_meta'])  if data.get('import_meta') else None,
        )
