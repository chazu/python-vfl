REFERENT_TYPES = {
    "int": "CONSTANT",
    "str": "VIEW_NAME"
}

class Predicate:

    __slots__ = (
        "children",
        "relation",
        "referent",
        "priority",
        "referent_type",
        "value"
    )

    def __init__(self, predicate_value):
        self.relation = None
        self.referent = None
        self.priority = None
        self.referent_type = self._init_referent_type(predicate_value)
        self.value = self._init_value(predicate_value)

    def _init_referent_type(self, predicate_value):
        """Return the referent type - infer if necessary."""
        return "CONSTANT" if isinstance(predicate_value, int) else "VIEW_NAME"

    def _init_value(self, predicate_value):
        """Return the value for the 'value' slot."""
        if isinstance(predicate_value, int):
            return predicate_value
        else:
            return None
