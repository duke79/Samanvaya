import os

import requests
from PIL import Image


class Fetcher():
    def get_file_from_url(self, image_url="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"):
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

    def get_captcha(self, selenium_driver, element, path="C:\\temp\\captcha.png"):
        """
        Ref: https://stackoverflow.com/a/36636459/973425
        :param selenium_driver:
        :param element:
        :param path:
        :return:
        """
        # now that we have the preliminary stuff out of the way time to get that image :D
        location = element.location
        size = element.size
        # saves screenshot of entire page
        screenshot_path = "C:\\temp\\get_captcha.png"
        selenium_driver.save_screenshot(screenshot_path)

        # uses PIL library to open image in memory
        image = Image.open(screenshot_path)

        # left = location['x']
        # top = location['y'] + 140
        # right = location['x'] + size['width']
        # bottom = location['y'] + size['height'] + 140

        left = location['x'] + size['height'] + 150
        top = location['y'] - size['height'] - 200
        right = location['x'] + size['width'] + 240
        bottom = location['y'] + size['width'] - 90

        image = image.crop((left, top, right, bottom))  # defines crop points
        image.save(path, 'png')  # saves new cropped image
        return path
