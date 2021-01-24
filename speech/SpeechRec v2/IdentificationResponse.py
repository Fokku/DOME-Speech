class IdentificationResponse:
    """This class encapsulates the identification response."""

    _PROFILE_ID = 'profileId'
    _SCORE = 'score'
    _PROFILES_RANKING = 'profilesRanking'

    def __init__(self, response):
        """Constructor of the IdentificationResponse class.

        Arguments:
        response -- the dictionary of the deserialized python response
        """
        self._identified_profile_id = response['identifiedProfile'].get(self._PROFILE_ID, None)
        self._confidence = response['identifiedProfile'].get(self._SCORE, None)
        self._profiles_ranking = response.get(self._PROFILES_RANKING, None)
        print(response)
    def get_identified_profile_id(self):
        """Returns the identified profile ID"""
        return self._identified_profile_id

    def get_confidence(self):
        """Returns the identification confidence"""
        return self._confidence

    def get_profiles_ranking(self):
        return self._profiles_ranking