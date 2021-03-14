import requests

per_page = 150
repo = "alenaPy/devops_lab"


def get_pulls(state):
    params1 = {'state': state, 'per_page': per_page}
    params2 = {'per_page': per_page}
    params3 = {'state': 'all', 'per_page': per_page}
    url_pulls = f'https://api.github.com/repos/{repo}/pulls'
    url_label = f'https://api.github.com/search/issues?q=\
            is:pr%20label:"{state}"%20repo:{repo}'
    if state in ('open', 'closed'):
        response = requests.get(url_pulls, params=params1)
        print(response.url)
        pull = response.json()
    elif state in ('needs work', 'accepted'):
        response = requests.get(url_label, params=params2)
        pull = response.json()['items']
        print(response.url)
    else:
        response = requests.get(url_pulls, params=params3)
        print(response.url)
        pull = response.json()

    out = []
    for item in pull:
        out.append({'num': item['number'], 'title': item['title'],
            'link': item['html_url']})

    return out
