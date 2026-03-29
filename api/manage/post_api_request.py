import httpx


def post_api_request(cmd: str, url: str, body: str):
    print(f'cmd={cmd}, url={url}, body={body}')

    r = httpx.post(url, content=body, follow_redirects=True)

    print(f'status_code={r.status_code}')
    print(f'reason={r.reason_phrase}')
    print(f'text={r.text}')
