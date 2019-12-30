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
        self.referent_type = None
        self.value = self._init_value(predicate_value)


    def _init_referent_type(self, predicate_value):
        """Return the referent type - infer if necessary."""
        return REFERENT_TYPES[type(predicate_value)]

    def _init_value(self, predicate_value):
        """Return the value for the 'value' slot."""
        if type(predicate_value) == 'int':
            return predicate_value
        else:
            return None
