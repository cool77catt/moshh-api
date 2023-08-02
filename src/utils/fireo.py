
def fireo_model_to_response(model):
    d = model.to_dict()
    d.pop('key')    # Remove the "key" parameter (don't expose to the user)
    return d
