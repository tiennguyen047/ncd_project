from http.server import SimpleHTTPRequestHandler

class NCD_http_request_handler(SimpleHTTPRequestHandler):

    def version_string(self):
        """override version_string to ensure all responses does not include
        Returns:
            _type_: _description_
        """
        return "NCD Service"
