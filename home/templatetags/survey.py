from django import template

from home.utils import create_star as utils_create_star

register = template.Library()


@register.filter(name="addclass")
def addclass(field, class_attr):
    return field.as_widget(attrs={"class": class_attr})


@register.filter(name="get_id_field")
def get_id_field(field):
    parse = field.auto_id.split("_")
    return parse[-1]


@register.simple_tag
def create_star(number, id_element, num_stars):
    return utils_create_star(
        active_star=int(number), num_stars=num_stars, id_element=id_element
    )
