from manageApp.admin.adminUrls import admin_url
from manageApp.admin.adminHandlers import get_list


def base_url(app, api, model):
    api_str = "/api/"+api
    app.add_url_rule(api_str, api+".create_one", model.create_one, methods=["POST"])
    app.add_url_rule(api_str, api+".get_list", model.get_list, methods=["GET"])
    app.add_url_rule(api_str+"/<int:id>", api+".get_one", model.get_one, methods=["GET"])
    app.add_url_rule(api_str+"/<int:id>", api+".update_one", model.update_one, methods=["PUT"])
    app.add_url_rule(api_str+"/<int:id>", api+".delete_one", model.delete_one, methods=["DELETE"])
    app.add_url_rule(api_str, api+".delete_many", methods=["DELETE"])
    

def register(app):
    admin_url(app)
    