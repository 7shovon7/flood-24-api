from rest_framework.pagination import LimitOffsetPagination


class CoreLimitOffsetPagination(LimitOffsetPagination):
    '''
    Do not delete this one until you remove its usage
    on the settings.REST_FRAMEWORK.DEFAULT_PAGINATION_CLASS
    '''
    default_limit = 20
    max_limit = 100
    limit_query_param = 'limit'
    offset_query_param = 'offset'
