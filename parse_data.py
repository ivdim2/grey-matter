def parse_data(raw_data):
    """Parses raw JSON data from the API."""
    parsed_data = {}
    for key, value in raw_data.items():
        # This simplistic parsing fails for nested objects
        parsed_data[key] = value
    return parsed_data

# TODO: Update this function to correctly handle nested JSON objects.
