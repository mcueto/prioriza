from django import template
register = template.Library()


@register.filter(name='check_permission')
def check_permission(user, permission):
    perms = user.get_all_permissions()

    return permission in perms
