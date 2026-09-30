from dataclasses import dataclass

@dataclass
class LogEntry:
    ip: str
    method: str
    url: str
    status: int

def parse_log_line(line: str):
    parts = line.strip().split()
    if len(parts) != 4:
        return None
    ip, method, url, status_text = parts
    try:
        status = int(status_text)
    except ValueError:
        return None
    return LogEntry(ip=ip, method=method.upper(), url=url, status=status)
