from django.core.management.utils import get_random_secret_key # type: ignore

print(get_random_secret_key())