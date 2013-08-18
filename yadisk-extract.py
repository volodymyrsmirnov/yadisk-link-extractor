#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json
import random
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", nargs="+", help="Yandex.Disk public url")

class YandexDiskException(Exception):
	pass

def get_direct_url(url):
	pass_request = requests.get("https://pass.yandex.ru/", params={
		"retpath": requests.get(url).url,
		"origsah": "FFFFFFFF",
		"ncrnd": random.randint(4000, 5000)
	}, allow_redirects=False)

	cookiejar = dict(pass_request.cookies)

	if not pass_request.status_code == 302 or not "yandexuid" in cookiejar:
		raise YandexDiskException("Something went wrong during pass.yandex.ru request")

	session_request_url = pass_request.headers["location"]

	session_request = requests.get(session_request_url, cookies=cookiejar, allow_redirects=False)
	cookiejar = dict(session_request.cookies)

	if not session_request.status_code == 302 or not "yandexuid" in cookiejar or not "Session_id" in cookiejar:
		raise YandexDiskException("Something went wrong during sessions request")

	page_request = requests.get(session_request.headers["location"], cookies=cookiejar)

	if not page_request.status_code == requests.codes.ok:
		raise YandexDiskException("Wrong response code while getting the page", page_request.status_code)

	ckey_match = re.search(r'"ckey":"([^"]+)"', page_request.text, re.I|re.U|re.M)

	if not ckey_match:
		raise YandexDiskException("Could not extract correct ckey from page")

	ckey = ckey_match.group(1)

	filehash_match = re.search(r'data-params="hash=([^"]+)"', page_request.text, re.I|re.U|re.M)

	if not filehash_match:
		raise YandexDiskException("Could not extract correct file hash from page")

	file_hash = filehash_match.group(1).replace("%3D", "=")
	
	get_link_request = requests.post("https://disk.yandex.ua/handlers.jsx", data={
		"_ckey": ckey,
		"_name": "getLinkFileDownload",
		"hash": file_hash
	}, cookies=cookiejar)

	if not get_link_request.status_code == requests.codes.ok:
		raise YandexDiskException("Could not get getLinkFileDownload command json answer")

	json_answer = get_link_request.json()

	if not "data" in json_answer or not "url" in json_answer["data"]:
		raise YandexDiskException("Something went wrong while getting URL from JSON reply, try again later or on another file")

	return json_answer["data"]["url"]

if __name__ == "__main__":
	args = parser.parse_args()

	for url in set(args.url): 
		print url, ">", get_direct_url(url)
