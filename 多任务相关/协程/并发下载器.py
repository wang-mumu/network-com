import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_name,img_site):
    req = urllib.request.urlopen(img_site)
    img_content = req.read()
    with open(img_name,"wb") as f:
        f.write(img_content)

def main():
    gevent.joinall([
        gevent.spawn(downloader,'1.jpg','https://rpic.douyucdn.cn/live-cover/roomCover/2018/10/28/0a539aaf2e6a086155cad8af9a40b80e_big.png'),
        gevent.spawn(downloader,'2.jpg','https://rpic.douyucdn.cn/live-cover/roomCover/2020/02/18/268ae2d8d6898bc04dd84460503f6352_big.jpg'),
        gevent.spawn(downloader,'3.jpg','https://rpic.douyucdn.cn/live-cover/roomCover/2020/03/31/bbb22987611ae433f2eed35f154383b8_big.jpg')
    ])
if __name__ == '__main__':
    main()
