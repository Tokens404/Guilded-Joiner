import requests, threading, random

proxies = []
for line in open('proxies.txt'):
    proxies.append(line.replace('\n', ''))

class ServerJoiner(threading.Thread):
    def __init__(self, invite, hmac_session):
        threading.Thread.__init__(self)
        self.guild_invite = invite
        self.hmac_session = hmac_session
    
    def run(self):
        headers = {"cookie" : f"hmac_signed_session={self.hmac_session}"}
        proxyServer = f"http://{random.choice(proxies)}"
        resp = requests.put(f"https://www.guilded.gg/api/invites/{self.guild_invite}", headers=headers, proxies={"http": proxyServer, "https": proxyServer})
        
        if "id" in resp.json(): 
            print(f"Joined Server: {self.hmac_session[:30]}")
        elif "code" in resp.json(): 
            print(f"Error Joining Server: {self.hmac_session[:30]}")


if __name__ == "__main__":
    invite = input("Enter guild invite code: ")

    with open("accounts.txt", "r") as _cookies:
        cookies =  []
        cookies += [_cookie.strip() for _cookie in _cookies.readlines()]

    for cookie in cookies:
        x = cookie.split(':')[2]
        ServerJoiner(invite=invite, hmac_session=x).start()
