from django import template
register = template.Library()

@register.filter
def index(List, idx):
	return List[int(idx-1)]

