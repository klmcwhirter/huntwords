
from ..models.command import CommandRequest, CommandResponse


class HuntwordsEchoCommand(object):
    """Command class that processes echo message"""

    def run(self, request: CommandRequest):
        """Command that processes echo message"""

        resp = {'oper': request.oper, 'body': request.body}

        return CommandResponse(200, resp, {})
