from geopy.geocoders import Nominatim

def add_geocodes(df):
    address = ''
    if 'Address' in df.columns:
        address='Address'
    if 'address' in df.columns:
        address = 'address'
    geo_df = df
    geolocator = Nominatim(user_agent="Udemy python student geolocator app")
    geo_df['location']= geo_df[address].apply(geolocator.geocode)
    geo_df['Lat'] = geo_df['location'].map(lambda location: None if location is None else location.latitude)
    geo_df['Lon'] = geo_df['location'].map(
        lambda location: None if location is None else location.longitude)
    geo_df.drop('location',1)
    print(geo_df)
    # save file

    return geo_df