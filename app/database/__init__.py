# -*- coding: utf-8 -*-

from .user import User
from .pronto_soccorso import ProntoSoccorso
from .pratica_assistenza import PraticaAssistenza


def get(entity_class, attribute_name, attribute_value):
    """
    Retrieve an instantiated entity from the database
    :param entity_class: Class of the entity e.g. db.EntityClass
    :param attribute_name: The attribute name on which to query
    :param attribute_value: The attribute value to look for
    :return:
    """
    l = get_list(entity_class, attribute_name, attribute_value)

    if len(l) > 0:
        return l[0]

    return None


def get_list(entity_class, attribute_name=None, attribute_value=None):
    """
    Retrieve a list of instantiated entities from the database
    :param entity_class: Class of the entity e.g. db.EntityClass
    :param attribute_name: The attribute name on which to query
    :param attribute_value: The attribute value to look for
    :return:
    """
    res = []

    for x in entity_class._table:

        if attribute_name is None and attribute_value is None:
            res.append(entity_class(x))
        else:
            value = x.get(attribute_name)

            if value == attribute_value:
                res.append(entity_class(x))

    return res
