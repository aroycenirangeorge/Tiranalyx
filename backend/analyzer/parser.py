def parse_log(file):
    logs = []

    for line in file:
        line = line.decode("utf-8").strip()

        if not line:
            continue

        parts = line.split(" ", 3)

        if len(parts) < 4:
            continue

        timestamp = f"{parts[0]} {parts[1]}"
        level = parts[2]
        message = parts[3]

        logs.append({
            "timestamp": timestamp,
            "level": level,
            "message": message
        })

    return logs


def extract_timestamp(line):
    """
    Extract timestamp from a log line.
    
    Args:
        line (str): Log line
        
    Returns:
        str: Extracted timestamp or None
    """
    import re
    
    # Common timestamp patterns
    patterns = [
        r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',  # YYYY-MM-DD HH:MM:SS
        r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}',  # MM/DD/YYYY HH:MM:SS
        r'\d{2}:\d{2}:\d{2}',  # HH:MM:SS
    ]
    
    for pattern in patterns:
        match = re.search(pattern, line)
        if match:
            return match.group()
    
    return None
