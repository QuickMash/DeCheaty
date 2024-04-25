import urllib
config = open(r'src/configs/settings.conf', 'r')
url = config.readline(2)
def upgrade():
    urlretrive(url, 'DeCheaty')