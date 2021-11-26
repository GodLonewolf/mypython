import bitly_api
user = "o_amodqqf77"
api = "fadcdf709a043bc49d23f5fe438b55cb08ad7852"
bitly = bitly_api.Connection(user, api)
while True:
    shortlink = bitly.shorten(input("Paste link: "))
    print("Shortened:  ")