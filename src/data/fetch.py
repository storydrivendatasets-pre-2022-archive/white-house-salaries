#!/usr/bin/env python3

from pathlib import Path
import re
import requests
YURLS = [
    (2009, 'https://opendata.socrata.com/api/views/pc5g-zfsx/rows.csv?accessType=DOWNLOAD'),
    (2010, 'https://opendata.socrata.com/api/views/vedg-c5sb/rows.csv?accessType=DOWNLOAD'),
    (2011, 'https://opendata.socrata.com/api/views/73t8-rw4g/rows.csv?accessType=DOWNLOAD'),
    (2012, 'https://opendata.socrata.com/api/views/jv7a-cjdv/rows.csv?accessType=DOWNLOAD'),
    (2013, 'https://opendata.socrata.com/api/views/44xn-rs2p/rows.csv?accessType=DOWNLOAD'),
    (2014, 'https://open.obamawhitehouse.archives.gov/sites/default/files/2014_Report_to_Congress_on_White_House_Staff.csv'),
    (2015, 'https://open.obamawhitehouse.archives.gov/sites/default/files/2015_Report_to_Congress_on_White_House_Staff.csv'),
    (2016, 'https://open.obamawhitehouse.archives.gov/sites/default/files/2016_Report_to_Congress_on_White_House_Staff.csv'),
    (2017, 'https://www.whitehouse.gov/sites/whitehouse.gov/files/docs/disclosures/07012017-report-final.pdf'),
    (2018, 'https://www.whitehouse.gov/wp-content/uploads/2018/06/07012018-report-final.pdf'),
]
DEST_DIR = Path('data', 'raw')

for year, url in YURLS:
    print("Downloading:", year, url)
    resp = requests.get(url)
    if resp.status_code != 200:
        raise requests.HTTPError("Status code was %s" % resp.status_code)
    else:
        destname = DEST_DIR.joinpath('{yr}.{ext}'.format(yr=year, ext=re.search(r'(?<=\.)\w{3}(?=$|\?)', url).group()))
        print("Saving:", destname)
        destname.write_bytes(resp.content)


