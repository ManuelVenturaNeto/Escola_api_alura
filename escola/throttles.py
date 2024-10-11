from rest_framework.throttling import UserRateThrottle, AnonRateThrottle # type: ignore


class MatriculaAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'