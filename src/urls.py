from apps.auth.urls import auth

def load_urls(app):
    app.register_blueprint(auth, url_prefix='/auth/')