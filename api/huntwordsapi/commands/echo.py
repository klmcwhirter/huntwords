
from ..handler_models import Request, Response


class HuntwordsEchoCommand(object):
    """Command class that processes echo message"""

    def run(self, request: Request):
        """Command that processes echo message"""

        resp = {'oper': request.oper, 'body': request.body}

        return Response(200, resp, {})
