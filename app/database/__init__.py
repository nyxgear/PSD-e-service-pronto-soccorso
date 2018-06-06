# -*- coding: utf-8 -*-

from .user import User
from .pronto_soccorso import ProntoSoccorso
from .pratica_assistenza import PraticaAssistenza
from .richiesta_soccorso import RichiestaSoccorso


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

            if str(value) == str(attribute_value):
                res.append(entity_class(x))

    return res


def save(entity):
    """
    Save the entity to the database
    :param entity:
    :return:
    """

    e_id = entity.e_d.get('id')
    if e_id:
        print('::DB:: Updating {}<{}>'.format(entity.__class__.__name__, e_id))
        # the entity already has an id
        # search for the entity in the table and update it
        for d in entity._table:
            if d['id'] == e_id:
                d.update(entity.to_dict())
    else:
        # it's a new entity, let's create a new id
        last_entity = entity._table[-1]
        new_id = last_entity.get('id') + 1
        print('::DB:: Inserting {}<{}>'.format(entity.__class__.__name__, new_id))
        entity.e_d['id'] = new_id
        entity._table.append(entity.e_d)
