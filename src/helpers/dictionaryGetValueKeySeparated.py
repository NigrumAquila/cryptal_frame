
dictionaryGetValueKey = lambda dictionary: [value + ' - ' +key for key, value in dictionary.items()]

dictionaryGetValueKeySeparated = lambda dictionary: '; '.join(dictionaryGetValueKey(dictionary))