import os, random, colorama, sys
import time
import random
from colorama import Fore, Back, Style
from colorama import init
from time import sleep
import requests
colorama.init(autoreset=True)
init()
MB_OK = 0x0
ICON_INFO = 0x40
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW
def clear():
    os.system("cls" if os.name == "nt" else "echo -e \\\\033c")
    os.system("mode con: cols=105 lines=30")
    os.system(
        'title ' + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t                                                      InstaTag @MassMentionBot ^| Press [ENTER] to Continue')
purple = '\x1b[38;5;56m'
gray = '\x1b[38;5;56m'
def logo():
    try:
        text = """                                   
                                ▪        .▄▄▄ ·▄▄▄▄▄▄ ▄▄▄· ▄▄▄▄▄▄ ▄▄▄·  ▄▄  
                                ██  •█▌▐█▐█  ▀.• ██  ▐█ ▀█ • ██  ▐█ ▀█ ▐█ ▀ ▪
                               @▐█· ▐█▐▐▌ ▀▀▀█▄  ██▪  █▀▀█   ██▪ ▄█▀▀█ ▄█ ▀█▄
                                ▐█▌  █▐█▌▐█▄▪▐█  ██· ▐█ ▪▐▌  ██· ▐█ ▪▐▌▐█▄▪▐█
                                ▀▀▀▀ ▀ █▪ ▀▀▀▀        ▀   ▀       ▀  ▀ ·▀▀▀▀  \n                    
        """
        bad_colors = ['LIGHTPURPLE_EX', 'CYAN']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in text]
        print(''.join(colored_chars))
        print(Fore.WHITE + "\t\t\t\t   Made by  24HOST#1010 - Moat#0666\n")
    except KeyboardInterrupt:
        sys.exit()
clear()
logo()
input("\t\t\t\t   [\x1b[38;5;199m+\x1b[0m] Press [\x1b[38;5;199mENTER\x1b[0m] to Continue   ")
global acc, username, password, post2122, commentdd
try:
    acc = open('burner.txt').read()
    pass
except FileNotFoundError:
    input("\t\t\t\t   [\x1b[38;5;199m!\x1b[0m] File [\x1b[38;5;199mBurner.txt\x1b[0m] is not found - Create one   ")
    quit()
username = acc.split(':')[0]
password = acc.split(':')[1]
r1 = requests.Session()
login_headers = {
    'accept': '/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '275',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=X0padwAEAAEPS5xI4RZu1YV6z7zS; rur=ASH; csrftoken=xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6; urlgen="{"185.88.26.35": 201031}:1kC1CG:D41DVXmf-j-T5nYho3c7g7K3MQU"',
    'origin': 'https://www.instagram.com/',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'x-csrftoken': 'xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',
    'x-instagram-ajax': '0c15f4d7d44a',
    'x-requested-with': 'XMLHttpRequest'}
login_data = {
    'username': f'{username}',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
    'queryParams': '{}',
    'optIntoOneTap': 'false'}
re = requests.post('https://www.instagram.com/accounts/login/ajax/', headers=login_headers, data=login_data, timeout=15)
if '"authenticated":true' in re.text:
    print(
        Fore.WHITE + '\t\t\t\t   [' + Fore.GREEN + '$' + Fore.WHITE + ']' + Fore.WHITE + ' Logged in: ' + Fore.YELLOW + f' {re.text} ')
    pass
if '"authenticated":false' in re.text:
    os.system("cls" if os.name == "nt" else "echo -e \\\\033c")
    logo()
    os.system(
        'title ' + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t                                                     InstaTag @MassMentionBot ^| Login [FAILED] ')
    input(
        f"\t\t   [\x1b[38;5;199m+\x1b[0m] Failed to Login Press [\x1b[38;5;199mENTER\x1b[0m] to Exit, Account: {username}:{password} ")
    sleep(5)
    quit()
sessid = re.cookies['sessionid']
csrftoken = re.cookies['csrftoken']
celeb = open('celebrity.txt').read()
urlll = f'https://www.instagram.com/{celeb}/?__a=1'
head = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
log = {'__a': '1'}
cookies = {'sessionid':sessid,
           'csrftoken':csrftoken}
r = requests.get(urlll, headers=head, data=log, cookies=cookies)
id_of_acc = r.json()["graphql"]["user"]["id"]
username_of_acc = r.json()["graphql"]["user"]["username"]
num_to_scrape = int(input(f'\t\t\t\t   {Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}${Fore.WHITE}]How Many Account to Scrape From "{celeb}"{Fore.LIGHTMAGENTA_EX}: '))
num_to_men = int(input(f'\t\t\t\t   {Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}${Fore.WHITE}]how Many Mentions? less than 20: '))
if num_to_men > 20:
    print('Put In A Number Thats Less Than 20!')
    quit()
doneee = 0
for i in range(100000):
    try:
        os.system(f'title MassMentionBot - Done: {doneee}')
        scrape_followers_url = f'https://i.instagram.com/api/v1/friendships/{id_of_acc}/followers/?count={num_to_scrape}&max_id=QVFBdGhyRTNOQ3g4RDdsYjBmZktVRzhDVVQ0Nlc0YzRyQTZldGZzYW9YMndvZDhxUXdzd3hnWU5PeDdoOEV6NEJ1cENTSUhyMVBUODJlaktFanZ3S2ZROQ%3D%3D&search_surface=follow_list_page'
        scrape_followers_headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': f'mid=YUiYQwALAAHkb0XfO-TA3uowJHuV; ig_did=4A4AE4DD-3820-4251-9952-D92D2B8FBBC4; ig_nrcb=1; datr=aO1IYUyaftjTUnfw-2svFngJ; fbm_124024574287414=base_domain=.instagram.com; shbid="8361\05450645069751\0541669631738:01f7551a849e82213f6241f43068d25d2e480f9771d1f73190b7b7a801d8ca3f933e9448"; shbts="1638095738\05450645069751\0541669631738:01f7f0beb235fa647f81703f6e014c68fd7954c0c859945c37e945322b2a5958c89fdf6b"; csrftoken={csrftoken}; ds_user_id=49698190565; sessionid={sessid}; fbsr_124024574287414=NjbAoZwN-o_vfeKwy7uMVcPqIKsnY_YpmLBgqevn598.eyJ1c2VyX2lkIjoiMTAwMDcyNjI5MjY4MDQ4IiwiY29kZSI6IkFRRG9jcTNIN2hXQXY2NUt1WUhhVzMybElod2RFQkw2Ylh2SjdOMHo5bWowNUpucEgzS0R1NHVTZGFuWDRndG5GM3AxOV9NZFhnNEpBcTBib3ZNNUlCYUlYOVBxLThDTk1DUFJQWnVwVFFzczhnUFJzdXozckdmRElkSnBJRF93U2JENHJPNGczOVdIM3ZrODZfeXJsaTF2a0JGVkJkOGdJWkRCdlZxenBBUFpIcllGVk1QMXNuNUIzNnh5REx5c0lfeEtSSld5akJSb2RveUJ6T0F1QnZ4LVVkQTJUS2FOcERLaGQ4MXA5MmJaMXhSVmlXenMwWmZEWWc0aWplLU9QSHNvalVWR28yZ0RjdWJBQV9kSVB6LTZ6VmtPRGZJTy1UWWNpYzdZYnYxNjgwZDhVeDNBbUNFRVI5TmNkRHZSOGNKb0lELWYzMkJUSU5LdXpyWDJMbmtnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9lcnhjRlpCb3BsQ2xOZm1uRzJIOXN1Q2tQY2huSkI0ZDZOVUwyZ2RrQVduNDFuT1RKWXQxNnVJdmdTR3MzSjFVS1pBZmVzWWVwZDU2Z0J2ZXBOYThyTU9DaVRlQnB4R285NFFzR21sYnVaQ2RnN0Q5OHBXM1FKNXF2R1VwSnEwdlZUUmJRSTBzWVFWaGpmY1M0c3g4R0VTZ1RyUnNrWkFla0lxd2Z0NVlHSVlQYVhGTDBaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjM4MjQyNjI1fQ; rur="ODN\05449698190565\0541669778634:01f74a7513d910c312cdc7a5fe4b33037cb92ea5d91c0d049228cadb07396275f088bb2e"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'x-asbd-id': '198387',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0djJ7gdubjX7BaOAWASynl6V2AWpWz5rix3zkT7kwjv6vO'}
        scrape_followers_data = {
            'count': f'{num_to_scrape}',
            'max_id': 'QVFBdGhyRTNOQ3g4RDdsYjBmZktVRzhDVVQ0Nlc0YzRyQTZldGZzYW9YMndvZDhxUXdzd3hnWU5PeDdoOEV6NEJ1cENTSUhyMVBUODJlaktFanZ3S2ZROQ==',
            'search_surface': 'follow_list_page'}
        resp = r1.get(scrape_followers_url, headers=scrape_followers_headers, data=scrape_followers_data)
        post2122 = resp.json()['users'][i]['username']
        f = open('scrapedfollowers.txt','a').write(post2122+'\n')
        doneee += 1
    except IndexError:
        print('Done Scraping . . .')
        def idk():
            global commentdd
            commentdd = 0
            comment = open('post.txt').read()
            comment_url = comment + '?__a=1'
            comment_head = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': f'mid=YUiYQwALAAHkb0XfO-TA3uowJHuV; ig_did=4A4AE4DD-3820-4251-9952-D92D2B8FBBC4; ig_nrcb=1; datr=aO1IYUyaftjTUnfw-2svFngJ; fbm_124024574287414=base_domain=.instagram.com; shbid="8361\05450645069751\0541669631738:01f7551a849e82213f6241f43068d25d2e480f9771d1f73190b7b7a801d8ca3f933e9448"; shbts="1638095738\05450645069751\0541669631738:01f7f0beb235fa647f81703f6e014c68fd7954c0c859945c37e945322b2a5958c89fdf6b"; fbsr_124024574287414=jZo4RXj89-oGk6dwkgCMdtam7jR-0Gj03MOuDSiwF0o.eyJ1c2VyX2lkIjoiMTAwMDcyNjI5MjY4MDQ4IiwiY29kZSI6IkFRRGVFTWNscTAzaHpvcjJCZ0t4d3dLbjJudHhLaDVvQXB4eTg5OWxnS3E4YUNmRkxDbDdZMmRpeXZqUlE4aW1qZkdWcnNmdE14Y2t1amgyU25RSTRLOHo0OWhHTHlFQ2VrWGc5NVNiSzRLWVJPTVREWjNYR0swc0RTdGJfYnR6T0tJYy1XOWNPZkpVQ1A4RXgwZFFnMHBLTW9GbTh3M3FEV1dhbjlrc2d3YWIzakZqX1BNQlMxanJWS0RYU0lNQWpUSWFBaGIyaXJ5QzNlV01XVWZROVJ5ZjZoM3NublFvZVpRVUdrZUJENXM2eUVHWXc2d0Y4bWlYSzFtZGNwOUdXTXd1TzlzR0ZubmpENXhTYVY3NXBKR1RsWngtTUtkZEQ3VXIyM0xXM3FOeHpiUXBBNFEzdzl1X00wTEJKaDVudW90cDJoMDlkd3FWT09sQ0NfUkVka2IyIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU5HWFI0VWR1WkFJSVpDc2hMbHpGcFpBNkpnbmNUMTVvM01BVnJyOURNSVpCOHJFRjNVQW1kekJxWTBWc3VSb3daQUZDZjlaQ1haQkhJY1pBWWFXZ2xaQkxhZmQ1Y3FrNlBzTUc5aklzbzRvWkNVWHlpZUpVdmtwZUVhdnFiNWg0QThQd01kbDdGM3E2R2YyMjNXcUkwYjhiR2wyaGNERmlJc1MwRVhJNkxrVXJnNThlRElaQUlaQXBxWVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2MzgyMjA4NDF9; csrftoken={csrftoken}; ds_user_id=45566283988; sessionid={sessid}; fbsr_124024574287414=jZo4RXj89-oGk6dwkgCMdtam7jR-0Gj03MOuDSiwF0o.eyJ1c2VyX2lkIjoiMTAwMDcyNjI5MjY4MDQ4IiwiY29kZSI6IkFRRGVFTWNscTAzaHpvcjJCZ0t4d3dLbjJudHhLaDVvQXB4eTg5OWxnS3E4YUNmRkxDbDdZMmRpeXZqUlE4aW1qZkdWcnNmdE14Y2t1amgyU25RSTRLOHo0OWhHTHlFQ2VrWGc5NVNiSzRLWVJPTVREWjNYR0swc0RTdGJfYnR6T0tJYy1XOWNPZkpVQ1A4RXgwZFFnMHBLTW9GbTh3M3FEV1dhbjlrc2d3YWIzakZqX1BNQlMxanJWS0RYU0lNQWpUSWFBaGIyaXJ5QzNlV01XVWZROVJ5ZjZoM3NublFvZVpRVUdrZUJENXM2eUVHWXc2d0Y4bWlYSzFtZGNwOUdXTXd1TzlzR0ZubmpENXhTYVY3NXBKR1RsWngtTUtkZEQ3VXIyM0xXM3FOeHpiUXBBNFEzdzl1X00wTEJKaDVudW90cDJoMDlkd3FWT09sQ0NfUkVka2IyIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU5HWFI0VWR1WkFJSVpDc2hMbHpGcFpBNkpnbmNUMTVvM01BVnJyOURNSVpCOHJFRjNVQW1kekJxWTBWc3VSb3daQUZDZjlaQ1haQkhJY1pBWWFXZ2xaQkxhZmQ1Y3FrNlBzTUc5aklzbzRvWkNVWHlpZUpVdmtwZUVhdnFiNWg0QThQd01kbDdGM3E2R2YyMjNXcUkwYjhiR2wyaGNERmlJc1MwRVhJNkxrVXJnNThlRElaQUlaQXBxWVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2MzgyMjA4NDF9; rur="CLN\05445566283988\0541669757201:01f7b8cd374d1fcdcd95282d04d56a04c5f39e6135c4bcc5dfbe7e40292b47175009e7d5"',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
            comment_data = {'__a': '1'}
            re = requests.get(comment_url, headers=comment_head, data=comment_data)
            opened_file = open('scrapedfollowers.txt')
            lines = opened_file.readlines()
            random_line = str("@".join(random.choice(lines) for z in range(num_to_men)))
            final = ('@' + random_line)
            id_of_post = re.json()['graphql']['shortcode_media']['id']
            post_com_url = f'https://www.instagram.com/web/comments/{id_of_post}/add/'
            post_com_head = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '48',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'mid=YUiYQwALAAHkb0XfO-TA3uowJHuV; ig_did=4A4AE4DD-3820-4251-9952-D92D2B8FBBC4; ig_nrcb=1; datr=aO1IYUyaftjTUnfw-2svFngJ; fbm_124024574287414=base_domain=.instagram.com; shbid="8361\05450645069751\0541669631738:01f7551a849e82213f6241f43068d25d2e480f9771d1f73190b7b7a801d8ca3f933e9448"; shbts="1638095738\05450645069751\0541669631738:01f7f0beb235fa647f81703f6e014c68fd7954c0c859945c37e945322b2a5958c89fdf6b"; csrftoken={csrftoken}; ds_user_id=45566283988; sessionid={sessid}; fbsr_124024574287414=jZo4RXj89-oGk6dwkgCMdtam7jR-0Gj03MOuDSiwF0o.eyJ1c2VyX2lkIjoiMTAwMDcyNjI5MjY4MDQ4IiwiY29kZSI6IkFRRGVFTWNscTAzaHpvcjJCZ0t4d3dLbjJudHhLaDVvQXB4eTg5OWxnS3E4YUNmRkxDbDdZMmRpeXZqUlE4aW1qZkdWcnNmdE14Y2t1amgyU25RSTRLOHo0OWhHTHlFQ2VrWGc5NVNiSzRLWVJPTVREWjNYR0swc0RTdGJfYnR6T0tJYy1XOWNPZkpVQ1A4RXgwZFFnMHBLTW9GbTh3M3FEV1dhbjlrc2d3YWIzakZqX1BNQlMxanJWS0RYU0lNQWpUSWFBaGIyaXJ5QzNlV01XVWZROVJ5ZjZoM3NublFvZVpRVUdrZUJENXM2eUVHWXc2d0Y4bWlYSzFtZGNwOUdXTXd1TzlzR0ZubmpENXhTYVY3NXBKR1RsWngtTUtkZEQ3VXIyM0xXM3FOeHpiUXBBNFEzdzl1X00wTEJKaDVudW90cDJoMDlkd3FWT09sQ0NfUkVka2IyIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU5HWFI0VWR1WkFJSVpDc2hMbHpGcFpBNkpnbmNUMTVvM01BVnJyOURNSVpCOHJFRjNVQW1kekJxWTBWc3VSb3daQUZDZjlaQ1haQkhJY1pBWWFXZ2xaQkxhZmQ1Y3FrNlBzTUc5aklzbzRvWkNVWHlpZUpVdmtwZUVhdnFiNWg0QThQd01kbDdGM3E2R2YyMjNXcUkwYjhiR2wyaGNERmlJc1MwRVhJNkxrVXJnNThlRElaQUlaQXBxWVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2MzgyMjA4NDF9; fbsr_124024574287414=vbrxGjiU-WT-lNVxVHpXMB-lCEyp3L33ah0nFJKFul4.eyJ1c2VyX2lkIjoiMTAwMDcyNjI5MjY4MDQ4IiwiY29kZSI6IkFRQ0FhVmNaM1V6Q1gtcjVCQ0EzeWhzVkI1V0FRVmhHSnp2RTJnMy1oRkhrVFRJbzF2VzI4ZVVndUlTSlktU3BDc3padTBTQ3dySjZuSlJoZF9qb1NoUHVucXNrZ0puRk5jMHhodHdYZGFrU3owZlV2Vi1WMkhxQ3R3TlhnSmlFMUJucEpzbEs2WkZVZE9lQk9aTDJ1SXdNNlFteFJLeW81ckJCTmd0VUFRMmsyZlVjcUhCSFdvOTBVYmNQX0M4QWFBZ19Lc0Q2YmdRc2w5dGpLdjItTDN5clN3RjRnbldNbXprOWk1UmxFdlBqWmNXZko2eGM2MjRTZnNtakZ1Y3FvNV80WEp0MW5hOEVKSkQ5bTRSN3dXZWNTcnpwUy12WUw0LXpGTU1jT0drTlE1Q0NWLVp2ZWVfcXNuWlg1SjFHdDJadWExSEdtcGl1UEZkclh6WXNXaFk3Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUJKNEhRMnIxTk50OE1zNW04aUdUQTVDZ2ZYTXdjWkNEVVpCWkI3b0VhdEJtaU1LSGZYQ2xNWkFaQURaQmNMVUZ1dFB5MGFEYU9TSlQ2UHJrc01waEEyR1J1RmNCdEowTllibnNIblk3U2VBUDNhV2dudHpQanZGMlhIamMwVXB2Z1NmMFNLMmNnN3pWSE1yT2FINGN3c3lRbjdMWThPeXh3QTRPVWl0UFREWEROQjUzOUZ2VVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2MzgyMjIyMzZ9; rur="CLN\05445566283988\0541669758262:01f7b73fbad6356ba4d90aff0aaaf7649eecc0ae6a55c60102f9f07df422259aac1dc4df"',
                'origin': 'https://www.instagram.com',
                'referer': f'https://www.instagram.com/{username_of_acc}/',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
                'x-asbd-id': '198387',
                'x-csrftoken': csrftoken,
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR2aiW9QCcPln1fcpICA4iHoZCnCw4ucqfr8aMJaAhxZITwo',
                'x-instagram-ajax': '038693313a95',
                'x-requested-with': 'XMLHttpRequest'}
            post_data = {
                'comment_text': final,
                'replied_to_comment_id': ''}
            final = r1.post(post_com_url, headers=post_com_head, data=post_data)
            if '"status":"ok"' in final.text:
                print('Done Commented!')
            if final.status_code == 429:
                print('Wait . . .')
        while True:
            idk()
            time.sleep(2)
            idk()
            time.sleep(2)
            idk()
            time.sleep(300)