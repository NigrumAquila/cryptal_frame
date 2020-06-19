
dictionaryGetValueKey = lambda dictionary: [value + ' - ' +key for key, value in dictionary.items()]

dictionaryGetValueKeySeparated = lambda dictionary: '; '.join(dictionaryGetValueKey(dictionary))

dictionaryKeyParser = lambda dictionary, desired: [key for key, value in dictionary.items() if value == desired][0]

dictionaryWithoutKeys = lambda dictionary, keys: {key: value for key, value in dictionary.items() if key not in keys}