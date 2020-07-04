def get_error_message(error):
    return getattr(error, "message", str(error))


def get_error_messages(error):
    return getattr(error, "messages", [get_error_message(error)])
