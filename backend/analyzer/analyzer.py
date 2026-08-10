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


def determine_severity(issue_type):
    high_severity = {
        "DATABASE",
        "REDIS",
        "TIMEOUT",
        "MEMORY",
        "CONNECTION"
    }

    if issue_type in high_severity:
        return "HIGH"

    if issue_type == "DISK":
        return "MEDIUM"

    return "MEDIUM"

def determine_impact(issue_type):

    impacts = {
        "DATABASE": "Application may be unable to read or write data.",
        "REDIS": "Caching or session-related operations may fail.",
        "TIMEOUT": "Application requests may experience delays or failures.",
        "MEMORY": "Application performance may degrade or services may crash.",
        "CONNECTION": "Communication with a dependent service may fail.",
        "DISK": "Application may experience storage-related failures.",
        "GENERAL": "Application functionality may be affected."
    }

    return impacts.get(
        issue_type,
        "Application functionality may be affected."
    )

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
            severity = determine_severity(issue_type)
            impact = determine_impact(issue_type)

            error = {
                **log,
                "issue_type": issue_type,
                "severity": severity,
                "impact": impact
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