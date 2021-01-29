from . import adminHandlers


def admin_url(app):
    from manageApp.routes import base_url
    base_url(app, "admin", adminHandlers)