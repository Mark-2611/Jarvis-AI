from services.file_manager import (
    create_folder,
    create_file,
    open_folder,
    rename_item,
    delete_item,
    open_recycle_bin
)

class FileTool:

    def execute(self, action, data):

        if action == "create_folder":
            return create_folder(data["target"])
        elif action == "create_file":
            return create_file(data["target"])
        elif action == "open_folder":
            return open_folder(data["target"])
        elif action == "rename":
            return rename_item(
        data["old_name"],
        data["new_name"]
                                )
        elif action == "delete_folder":
            return delete_item(
            data["target"],
            "folder"
    )
        elif action == "delete_file":
            return delete_item(
            data["target"],
            "file"
    )
        elif action == "open_recycle_bin":
            return open_recycle_bin()
        return None