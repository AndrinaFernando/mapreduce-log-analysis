from collections import Counter
from log_parser import parse_log_line

def map_file(file_path: str):
    result = {
        "total": 0,
        "methods": Counter(),
        "statuses": Counter(),
        "urls": Counter(),
        "ips": Counter(),
        "invalid_lines": 0,
    }
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            entry = parse_log_line(line)
            if entry is None:
                result["invalid_lines"] += 1
                continue
            result["total"] += 1
            result["methods"][entry.method] += 1
            result["statuses"][entry.status] += 1
            result["urls"][entry.url] += 1
            result["ips"][entry.ip] += 1
    return result
