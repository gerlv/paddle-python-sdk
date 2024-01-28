from __future__ import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Entity  import Entity
from paddle_billing_python_sdk.Entities.Product import Product

from paddle_billing_python_sdk.Entities.Shared.CatalogType       import CatalogType
from paddle_billing_python_sdk.Entities.Shared.CustomData        import CustomData
from paddle_billing_python_sdk.Entities.Shared.Money             import Money
from paddle_billing_python_sdk.Entities.Shared.PriceQuantity     import PriceQuantity
from paddle_billing_python_sdk.Entities.Shared.Status            import Status
from paddle_billing_python_sdk.Entities.Shared.TaxMode           import TaxMode
from paddle_billing_python_sdk.Entities.Shared.TimePeriod        import TimePeriod
from paddle_billing_python_sdk.Entities.Shared.UnitPriceOverride import UnitPriceOverride


@dataclass
class PriceWithIncludes(Entity):
    id:                   str
    product_id:           str
    description:          str
    unit_price:           Money
    unit_price_overrides: list[UnitPriceOverride]
    quantity:             PriceQuantity
    status:               Status
    name:                 str         | None
    type:                 CatalogType | None
    billing_cycle:        TimePeriod  | None
    trial_period:         TimePeriod  | None
    tax_mode:             TaxMode     | None
    custom_data:          CustomData  | None
    product:              Product     | None


    @classmethod
    def from_dict(cls, data: dict) -> PriceWithIncludes:
        return PriceWithIncludes(
            id                   = data['id'],
            product_id           = data['product_id'],
            name                 = data.get('name'),
            description          = data['description'],
            unit_price           = Money.from_dict(data['unit_price']),
            quantity             = PriceQuantity.from_dict(data['quantity']),
            status               = Status(data['status']),
            unit_price_overrides = [UnitPriceOverride.from_dict(override) for override in data.get('unit_price_overrides', [])],
            type                 = CatalogType(data['type'])                   if data.get('type')          else None,
            billing_cycle        = TimePeriod.from_dict(data['billing_cycle']) if data.get('billing_cycle') else None,
            trial_period         = TimePeriod.from_dict(data['trial_period'])  if data.get('trial_period')  else None,
            tax_mode             = TaxMode(data['tax_mode'])                   if data.get('tax_mode')      else None,
            custom_data          = CustomData(data['custom_data'])             if data.get('custom_data')   else None,
            product              = Product.from_dict(data['product'])          if data.get('product')       else None,
        )
