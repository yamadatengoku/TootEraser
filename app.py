#https://mstdn.jp/web/statuses/19814124
from mastodon import Mastodon
import os.path
import time

#設定ここから
instance = 'https://mstdn.jp'
login_id = ''
login_passwd = ''
account_id = ''
#設定ここまで
mastodon = ''
retry = 0

def main():
	global mastodon
	mastodon = Mastodon(
	    client_id="yourapp_clientcred.txt",
	    access_token="your_usercred.txt",
	    api_base_url = "https://mstdn.jp")
	while True:
	    remover()
	    time.sleep(20)

def remover():
	global account_id,mastodon
	a = mastodon.account_statuses(account_id)

	if len(a) > 0:
		for i,item in enumerate(a):
			print(item['id'])
			mastodon.status_delete(item['id'])
	else:
		print("トゥートが無いか一時的に削除できません。時間を置いて試してね。")
		quit()
def checkCertFiles():
	global instance,login_id,login_passwd,retry
	retry += 1
	if retry > 5:
		print("Too many retry.Check Setting.")
		quit()
	if not os.path.exists('yourapp_clientcred.txt'):
		print('creating files...(1/2)')
		Mastodon.create_app("TootEraser",
		                    api_base_url = instance,
		                    to_file = "yourapp_clientcred.txt"
		)
		time.sleep(10)
		checkCertFiles()

	if not os.path.exists('your_usercred.txt'):
		print('creating files...(2/2)')
		mastodon = Mastodon(
		    client_id="yourapp_clientcred.txt",
		    api_base_url = instance)

		mastodon.log_in(
		    login_id,
		    login_passwd,
		    to_file = "your_usercred.txt")
		time.sleep(10)
		checkCertFiles()
	else:
		main()

checkCertFiles()
