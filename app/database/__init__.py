from .user import User

def get(entity_class, attribute_name, attribute_value):
	"""
	Retrieve an instantiated entity from the database
	:param entity_class: Class of the entity e.g. db.EntityClass
	:param attribute_name: The attribute name on which to query
	:param attribute_value: The attribute value to look for
	:return:
	"""
	res = []

	# search for the entity
	for x in entity_class._table:
		value = x.get(attribute_name)

		if value == attribute_value:
			res.append(x)

	# no results
	if not res:
		return None

	x_dict = res[0]

	return entity_class(x_dict)
