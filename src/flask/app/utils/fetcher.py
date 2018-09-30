import os

import requests

class Fetcher():
    def get_file_from_url(self, image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"):
        # URL of the image to be downloaded is defined as image_url
        r = requests.get(image_url)  # create HTTP response object

        # send a HTTP request to the server and save
        # the HTTP response in a response object called r
        save_path = "C:\\temp\\fetcher_file.png"
        if not os.path.exists(save_path):
            os.makedirs(os.path.dirname(save_path))
        with open(save_path, 'wb') as f:
            # Saving received content as a png file in
            # binary format

            # write the contents of the response (r.content)
            # to a new file in binary mode.
            f.write(r.content)

        # return open(save_path, 'wb')
        return save_path