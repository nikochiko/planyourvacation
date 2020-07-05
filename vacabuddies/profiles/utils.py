def get_error_message(error):
    return getattr(error, "message", str(error))

def get_error_messages(error):
    return getattr(error, "messages", [get_error_message(error)])


def make_user_dict(user):
    retval = {}
    retval.update(
        name=user.last_name,
        email=user.email,
        username=user.username,
        bio=getattr(user, 'bio', ''),
        likes=len(user.likes_in.all())
    )
    return retval


def make_trip_dict(trip):
    retval = {}
    retval.update(
        title = trip.title,
        description=trip.description,
        creator=make_user_dict(trip.creator),
        date=str(trip.dates),
    )
    return retval
