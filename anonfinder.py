from smedia.twitter import Twitter


class __KeyManager:
    def __init__(self, *__key_file):

        self.key_file = __key_file

        self.__twitter_keys = []


class AnonFinder(Twitter):
    pass
