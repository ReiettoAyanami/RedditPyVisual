from urllib import request
from urllib.request import urlopen
import requests
import io
import re


class Loader:

    def __init__(self):
        pass

    def convert(self,url):
        image_to_string = urlopen(url).read()
        image_to_file = io.BytesIO(image_to_string)
        return image_to_file


    def convert_list(self,url_list):
        imglst = []
        for url in url_list:
            image_to_string = urlopen(url).read()
            image_to_file = io.BytesIO(image_to_string)
            imglst.append(image_to_file)
        return imglst

