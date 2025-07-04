import geocoder


def get_current_ip_location():
    g = geocoder.ip('me')

    return g


coordinates = get_current_ip_location()