def get_value(data, key, default, lookup=None, mapper=None):
    return_value = data[key]
    # Instead of checking for empty string specifically, check if the value is falsy
    # This covers cases like None, empty string, 0, etc.
    if not return_value:  
        return_value = default
    if lookup:
        return_value = lookup[return_value]
    if mapper:
        return_value = mapper(return_value)
    return return_value

def ftp_file_prefix(namespace):
    # Suggestion: Add handling for empty namespace or namespace without dots.
    # For example: if not namespace or '.' not in namespace: return 'ftp' 
    # This would prevent an IndexError if namespace is empty or doesn't contain a dot.
    return ".".join(namespace.split(".")[:-1]) + '.ftp' 

def string_to_bool(string):
    
    # Consider using string.casefold() instead of string.lower()
    # for more robust case-insensitive comparison
    if string.lower() == 'true':
        return True
    if string.lower() == 'false':
        return False
    
    # Consider using a more specific error message
    # e.g., "Invalid input. Expected 'true' or 'false' (case-insensitive)."
    raise ValueError(f'String {string} is neither true nor false')

    #  Consider adding type hinting for better code readability
    # and maintainability, e.g.:
    # def string_to_bool(string: str) -> bool:
    # For better performance, you could use a single if-else structure
    # instead of two separate if statements
    
def config_from_dict(dict):
    # Consider renaming 'dict' to a more descriptive name like 'config_dict'
    # to avoid shadowing the built-in 'dict' type
    namespace = dict['Namespace']
    return (dict['Airflow DAG'],
            {"earliest_available_delta_days": 0,
             "lif_encoding": 'json',
             "earliest_available_time":
                 get_value(dict, 'Available Start Time', '07:00'),
             "latest_available_time":
                 get_value(dict, 'Available End Time', '08:00'),
             "require_schema_match":
                 get_value(dict, 'Requires Schema Match', 'True',
                           mapper=string_to_bool),
             "schedule_interval":
                 get_value(dict, 'Schedule', '1 7 * * *'),
             "delta_days":
                 get_value(dict, 'Delta Days', 'DAY_BEFORE',
                           lookup=DeltaDays),
             "ftp_file_wildcard":
                 # Consider adding a default value for 'File Naming Pattern'
                 get_value(dict, 'File Naming Pattern', None),
             "ftp_file_prefix":
                 get_value(dict, 'FTP File Prefix',
                           ftp_file_prefix(namespace)),
             "namespace": namespace
             }
    )
    # Consider adding type hints to improve code readability and maintainability
    # The 'get_value' function is not defined in this snippet. Ensure it's imported or defined elsewhere
    # The 'string_to_bool' and 'DeltaDays' are not defined. Make sure they are imported or defined
    # The 'ftp_file_prefix' function is used but not defined. Ensure it's imported or defined
    # Consider adding error handling for missing keys in the input dictionary
    # The indentation of the return statement could be improved for better readability
    # Consider using a constant for default values like '07:00' and '08:00'