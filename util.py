def normalize_window(points, app):
    if points[1][0] < points[0][0]: # Q
        return app.make_window(points[1][0], points[1][1],
                    points[0][0] - points[1][0], points[0][1] - points[1][1])
    else:
        return app.make_window(points[0][0], points[0][1],
                    points[1][0] - points[0][0], points[1][1] - points[0][1])

def normalize_points(point0, point1):
    return [[min(point0[0], point1[0]), min(point0[1], point1[1])],
            [max(point0[0], point1[0]), max(point0[1], point1[1])]]

def predicate_for_node_type(node_type):
    """
    Return a callable predicate which detects parse nodes of the given
    type.
    """
    return lambda x: type(x) == dict and x['type'] == node_type
