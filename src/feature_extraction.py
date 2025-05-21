def extract_features(url):
    features = {}
    features['length'] = len(url)
    features['https'] = 1 if 'https' in url else 0
    features['count_dots'] = url.count('.')
    features['count_at'] = url.count('@')
    features['count_hyphen'] = url.count('-')
    features['count_question'] = url.count('?')
    features['count_equal'] = url.count('=')
    features['count_percent'] = url.count('%')
    features['count_digits'] = sum(c.isdigit() for c in url)
    return features
