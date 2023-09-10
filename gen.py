import os
import os.path as osp
from pathlib import Path

ROOT = '/'

SUBFOLDER_TO_PERMALINK = {
    ROOT: 'https://kaylielam03.wixsite.com/myportfolio',
    'vda': 'https://vda-kaylielam.notion.site/vda-kaylielam/Visual-Design-Apprenticeship-Journal-b3e84cd456114f1aa913d58f4e1d7c17',
    'bb': 'https://arth.website/',
}

for subfolder, link in SUBFOLDER_TO_PERMALINK.items():
    f = None
    if subfolder == ROOT:
        f = open('index.html', 'w')
    else:
        subfolder_path = Path(subfolder)
        subfolder_path.mkdir(parents=True, exist_ok=True)
        f = open(str(subfolder_path / 'index.html'), 'w')

    f.write(
f"""<html>
    <head>
        <title>Kaylie Lam</title>
        <meta http-equiv="refresh" content="0;url={link}" />
    </head>
    <body>
        <p>You are being redirected to <a href="{link}">{link}</a></p>
        <p>If the redirect does not work, please click the link above to continue.</p>
    </body>
</html>
"""
    )
