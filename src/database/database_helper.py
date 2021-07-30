def config_helper(config) -> dict:
    return {
        "id": str(config['_id']),
        "field_name": config['field_name'],
        "field_value": config['field_value'],
    }

def admin_helper(admin) -> dict:
    return {
        "id": str(admin['_id']),
        "fullname": admin['fullname'],
        "email": admin['email'],
    }


def post_helper(post) -> dict:
    return {
        "id": str(post['_id']),
        "content": post['content'],
        "imageLink": post['imageLink'],
        "approved": str(post['approved']),
    }
