# SWAGGER UTILS
class Tag:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Server:
    def __init__(self, url, description):
        self.url = url
        self.description = description

class Contact:
    def __init__(self, name, url, email):
        self.name = name
        self.url = url
        self.email = email

class License:
    def __init__(self, name, url):
        self.name = name
        self.url = url

# PRE DEFINES RESPONSES
responses = {
    403: {"description": "Insufficient privileges for this action"}
}

response_post = { 
    201: {"description": "Resource Successfully created "},
    **responses
}

response_update = { 
    204: {"description": "Resource Successfully updated"},
    **responses,
    404: {"description": "Resource not Found"}
}

response_delete = {
    204: {"description": "Resource Successfully deleted"},
    **responses
}

response_get = { 
    200: {"description": "Successfully retrieved information of the user"},
    **responses,
    404: {"description": "Resource Not Found"}
}