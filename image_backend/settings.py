import os

from split_settings.tools import optional, include

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'D')
print(ENVIRONMENT)

ENVIRONMENTS = {
    'D': 'env_settings/development.py',
    'S': 'env_settings/staging.py',
    'P': 'env_settings/production.py',
}


include(
    'components/main.py',
    'components/rest_framework.py',
    ENVIRONMENTS[ENVIRONMENT],
    optional('env_settings/local_settings.py'),
)

