
def generic_model_mutation_process(model, data, id=None, commit=True):
    """Esta funcion lo que nos permite es actualizar
    o crear un nuevo dato en la db"""
    if id:
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)
    if commit:
        item.save()
    return item
