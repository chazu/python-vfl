def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i

def value_of_child_with_type(children, _type):
    values = values_of_children_with_type(children, _type)
    return values[0] if values else None

def values_of_children_with_type(children, _type):
    return [child["value"] for child in children
            if child["type"] == _type]
