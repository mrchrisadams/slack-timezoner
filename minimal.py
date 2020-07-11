import sys

from django.conf import settings
from django.conf.urls import url
from django.core.management import execute_from_command_line
from django.http import HttpResponse, JsonResponse
import json
from group_by_timezones import TimeZoneCounter

from dotenv import load_dotenv
load_dotenv()

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
)


def index(request):
    tzc = TimeZoneCounter()
    res = tzc.summary()


    return (JsonResponse(res))

urlpatterns = [
    url(r'^$', index),
]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)