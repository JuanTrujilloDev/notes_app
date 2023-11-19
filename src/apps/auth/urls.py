from apps.auth.views import login

from apps.auth.app import auth

# urls
auth.add_url_rule('login/', view_func=login, methods=["POST"])
