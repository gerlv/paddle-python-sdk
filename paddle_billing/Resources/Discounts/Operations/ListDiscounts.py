from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.HasParameters import HasParameters

from paddle_billing.Entities.Shared import Status

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Shared.Operations import Pager


class ListDiscounts(HasParameters):
    def __init__(
        self,
        pager:    Pager        = None,
        ids:      list[str]    = None,
        statuses: list[Status] = None,
        codes:    list[str]    = None,
    ):
        self.pager    = pager
        self.ids      = ids      if ids      is not None else []
        self.statuses = statuses if statuses is not None else []
        self.codes    = codes    if codes    is not None else []

        # Validation
        for field_name, field_value, field_type in [
            ('ids',      self.ids,      str),
            ('statuses', self.statuses, Status),
            ('codes',    self.codes,    str),
        ]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException(field_name, field_type.__name__, invalid_items)


    def get_parameters(self) -> dict:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.ids:
            parameters['id'] = ','.join(self.ids)
        if self.statuses:
            parameters['status'] = ','.join(map(enum_stringify, self.statuses))
        if self.codes:
            parameters['code'] = ','.join(self.codes)

        return parameters
