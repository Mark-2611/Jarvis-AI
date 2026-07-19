from services.system import open_application


class SystemTool:

    def execute(self, action, data):

        if action == "open_app":
            return open_application(data["target"])

        return None