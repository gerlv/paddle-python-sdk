from dataclasses import asdict, dataclass

from paddle_billing.Undefined       import Undefined
from paddle_billing.Entities.Shared import CatalogType, CustomData, Money, PriceQuantity, TaxMode, TimePeriod, UnitPriceOverride


@dataclass
class CreatePrice:
    description:          str
    product_id:           str
    unit_price:           Money
    name:                 str                     | None | Undefined = Undefined()
    type:                 CatalogType             | None | Undefined = Undefined()
    unit_price_overrides: list[UnitPriceOverride] | None | Undefined = Undefined()
    tax_mode:             TaxMode                 | None | Undefined = Undefined()
    trial_period:         TimePeriod              | None | Undefined = Undefined()
    billing_cycle:        TimePeriod              | None | Undefined = Undefined()
    quantity:             PriceQuantity           | None | Undefined = Undefined()
    custom_data:          CustomData              | None | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
