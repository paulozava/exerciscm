def transform(legacy_data):
    return {value.lower(): old_key
            for old_key, values_list in legacy_data.items()
            for value in values_list}