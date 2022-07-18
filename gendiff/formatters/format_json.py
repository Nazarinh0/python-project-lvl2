import json


def render(diff):
    """Render JSON."""
    return json.dumps(diff, indent=2)