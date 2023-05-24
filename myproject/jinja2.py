from django_jinja.builtins import DEFAULT_EXTENSIONS
from jinja2 import Environment

# Add any additional extensions you want to use
# by appending them to the `extensions` list
extensions = DEFAULT_EXTENSIONS

# Customize the Jinja2 environment as needed
env = Environment(extensions=extensions)

def environment(**options):
    return env
