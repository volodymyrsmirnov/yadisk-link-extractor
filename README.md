# Yandex.Disk downloadable direct links extractor

Get direct links from sharing links for files stored in Yandex.Disk.

### Dependencies

yadisk-link-extractor depends on Python-Requests, install it using "pip install requests".

### Usage example

1. Get file link using Yandex.Disk desktop client of web interface, it should like like http://yadi.sk/d/evfDgRTt82mlW or https://disk.yandex.ua/public/?hash=bGPuIbyz6hzRbcKurY7Ny69nk60XVtSEdm46TELfGK4%3D
2. Execute `python yadisk-extract.py http://yadi.sk/d/TS3MQcvo834K8`. You can provide multuple URLs, just separate them by spaces.
3. It will do all the magic and output something like `http://yadi.sk/d/evfDgRTt82mlW > https://downloader.disk.yandex.ru/disk/1eb2cafe972c7c2d112f8a5864f0713b/521127a7/DtvhwprQ18lRuYX-XvCiwx1uceMrS6qhwbhc20ZiD1hnROt5GBRsam9tPU6j0oR-cqbghOPWk1wWsB9_6mAcbw%3D%3D?uid=0&filename=just_a_test.txt&disposition=attachment&hash=bGPuIbyz6hzRbcKurY7Ny69nk60XVtSEdm46TELfGK4%3D&limit=0&content_type=text%2Fplain`, where part befor ">" sign is a source link, and long pasta-style URL after ">" sign is a direct link.
4. Use wget ot any other command line tool for getting the file, i.e. `wget "https://downloader.disk.yandex.ru/disk/1eb2cafe972c7c2d112f8a5864f0713b/521127a7/DtvhwprQ18lRuYX-XvCiwx1uceMrS6qhwbhc20ZiD1hnROt5GBRsam9tPU6j0oR-cqbghOPWk1wWsB9_6mAcbw%3D%3D?uid=0&filename=just_a_test.txt&disposition=attachment&hash=bGPuIbyz6hzRbcKurY7Ny69nk60XVtSEdm46TELfGK4%3D&limit=0&content_type=text%2Fplain" -O test_text_file.txt`

### Disclaimer
This code could be used for educational purposes only.

You shall not copy any part of the provided program to the testing or production environments,
otherwise you may violate Yandex.Disk EULA, usage terms and the Exodus 20:15 "Thou shalt not steal".

The author is not responsible for any violation of this simple and clear rules.