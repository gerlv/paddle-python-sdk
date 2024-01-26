from paddle_billing_python_sdk.FiltersNone   import FiltersNone
from paddle_billing_python_sdk.HasParameters import HasParameters

from paddle_billing_python_sdk.Resources.Shared.Operations.List.OrderBy import OrderBy


class Pager(HasParameters):
    def __init__(
        self,
        after:       str     = None,
        order_by:    OrderBy = None,
        per_page:    int     = 50,
    ):
        self.after    = after
        self.order_by = order_by if order_by is not None else OrderBy.id_ascending()
        self.per_page = per_page


    def get_parameters(self) -> dict:
        return FiltersNone.filter_none_values({
            'after':    self.after,
            'order_by': str(self.order_by),
            'per_page': self.per_page
        })
