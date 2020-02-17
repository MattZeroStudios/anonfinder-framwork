import twitter


class Twitter:

    def twitter_get_profile(self, profile, api):

        return api.GetUser(screen_name=profile)
