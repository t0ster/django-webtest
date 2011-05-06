from django.test import TestCase
from django.conf import settings
from nose.util import resolve_name


DJANGO_WEBTEST_BASE_TESTCASE = getattr(
    settings, 'DJANGO_WEBTEST_BASE_TESTCASE', 'django.test.TestCase'
)
DJANGO_WEBTEST_BASE_TESTCASE = resolve_name(DJANGO_WEBTEST_BASE_TESTCASE)
