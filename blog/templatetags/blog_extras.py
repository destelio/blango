
from django import template
from django.template.defaultfilters import stringfilter

#register = template.Library()
#from django.contrib.auth import get_user_model
#from django.contrib.auth import get_user_model

from django.contrib.auth import get_user_model

from django.utils import translation
from django.utils.html import format_html
#from django.utils.translation import string_concat
#from django.utils.translation import ugettext_lazy as _

register = template.Library()

user_model = get_user_model()

@register.filter
def author_details(author, current_user):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)
