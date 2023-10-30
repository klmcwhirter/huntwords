import requests


def command(cmd: str, url: str, body: str):
    print(f'cmd={cmd}, url={url}, body={body}')

    r = requests.post(url, body)

    print(f'status_code={r.status_code}')
    print(f'reason={r.reason}')
    print(f'text={r.text}')
