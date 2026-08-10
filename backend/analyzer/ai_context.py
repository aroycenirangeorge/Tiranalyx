def build_ai_context(analysis):

    context = {
        "total_logs": analysis["total_logs"],
        "error_count": analysis["statistics"]["error_count"],
        "warning_count": analysis["statistics"]["warning_count"],
        "issues": []
    }

    for issue in analysis["issues"]:
        context["issues"].append({
            "type": issue["issue_type"],
            "timestamp": issue["timestamp"],
            "message": issue["message"]
        })

    return context