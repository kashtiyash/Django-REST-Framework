from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5  # To set number of records per page, default = 5
    page_query_param = 'mypage'  # To set query param to any word, default = page
    page_size_query_param = 'records'  # To allow client set per page records as per their requirements
    max_page_size = 7  # To limit the per page records
    last_page_strings = 'end'  # To set last_page_strings to any word, default = last


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5  # To set the number of records per page
    limit_query_param = 'mylimit'  # To set the limit_query_param to any word, default = limit
    offset_query_param = 'myoffset'  # To set the offset_query_param to any word, default = offset
    max_limit = 6  # To limit the number of records per page


class MyCursorPagination(CursorPagination):
    page_size = 5  # Number of records per page
    ordering = 'name'  # Order by any field,If created field is already in the model then it will automatically order by
    cursor_query_param = 'cu'  # To set cursor_query_param any word, by default = cursor
