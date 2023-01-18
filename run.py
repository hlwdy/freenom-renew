import argparse

from freenom import FreeNom

# args
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', type=str)
parser.add_argument('-p', '--password', type=str)
parser.add_argument('-pr', '--proxy', type=str)
args = parser.parse_args()

username = args.username
password = args.password
proxy_ = args.proxy

instance = FreeNom(username, password, proxy_)
instance.renew()
