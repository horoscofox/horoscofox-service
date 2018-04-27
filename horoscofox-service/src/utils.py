from horoscofox import paolo, branko


def fromDocToJson(document, arguments):
    res = {}
    for arg in arguments:
        if 'date' in arg:
            res[arg] = document[arg].isoformat()
        else:
            res[arg] = document[arg]
    return res
