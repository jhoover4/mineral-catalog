from django import template

register = template.Library()


@register.simple_tag(name='url_add_replace')
def url_add_replace(request, field, value):
    url_string = request.GET.copy()

    url_string.__setitem__(field, value)

    return u"?%s" % (url_string.urlencode())
