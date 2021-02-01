from settings import USER_AGENTS
import random


class RotateUserAgentMiddleware(object):
    def process_request(self, request, spider):
        # 用于随机选择user-agent
        ua = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', ua)


