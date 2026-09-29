from django import template

register = template.Library()


@register.filter()
def badge(status: str):
    status_badges: dict[str, str] = {"todo": "⬜", "pending": "⏳", "done": "✅"}
    return status_badges[status.lower()]
