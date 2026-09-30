from collections import Counter

def reduce_results(partials):
    combined = {
        "total": 0,
        "methods": Counter(),
        "statuses": Counter(),
        "urls": Counter(),
        "ips": Counter(),
        "invalid_lines": 0,
    }
    for part in partials:
        combined["total"] += part["total"]
        combined["methods"].update(part["methods"])
        combined["statuses"].update(part["statuses"])
        combined["urls"].update(part["urls"])
        combined["ips"].update(part["ips"])
        combined["invalid_lines"] += part["invalid_lines"]
    return combined
