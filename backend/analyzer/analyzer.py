from collections import Counter


def detect_issue(log):
    message = log["message"].lower()

    if "database" in message or "db" in message:
        return "DATABASE"

    if "redis" in message:
        return "REDIS"

    if "timeout" in message:
        return "TIMEOUT"

    if "disk" in message:
        return "DISK"

    if "memory" in message:
        return "MEMORY"

    if "connection" in message or "connect" in message:
        return "CONNECTION"

    return "GENERAL"


def analyze_logs(logs):

    level_counts = Counter()

    errors = []
    warnings = []
    issues = []

    for log in logs:

        level = log["level"]

        level_counts[level] += 1

        if level == "ERROR":
            issue_type = detect_issue(log)

            error = {
                **log,
                "issue_type": issue_type
            }

            errors.append(error)
            issues.append(error)

        elif level == "WARNING":
            warnings.append(log)

    return {
        "total_logs": len(logs),

        "errors": errors,

        "warnings": warnings,

        "issues": issues,

        "statistics": {
            "error_count": level_counts.get("ERROR", 0),
            "warning_count": level_counts.get("WARNING", 0),
            "info_count": level_counts.get("INFO", 0),
        }
    }