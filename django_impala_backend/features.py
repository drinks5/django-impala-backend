from django.db.backends.base.features import BaseDatabaseFeatures


class DatabaseFeatures(BaseDatabaseFeatures):
    can_return_id_from_insert = False
    has_real_datatype = True
    supports_nullable_unique_constraints = False
    supports_partially_nullable_unique_constraints = False
    supports_timezones = False
    supports_transactions = False

    def _supports_transactions(self):
        return False
