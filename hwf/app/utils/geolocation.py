import geocoder

def get_current_ip_location():
    g = geocoder.ip('me')
    
    return g
    # if g.latlng:
    #     return g.latlng
    # else:
    #     return None


coordinates = get_current_ip_location()