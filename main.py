from sonicbit import SonicBit
import logging
from time import sleep
logging.basicConfig(level=logging.info,format="%(asctime)s - %(level)s - %(message)s")
EMAIL = "trezepottalu-6066@yopmail.com"
PASSWORD = "Something@123"
def login():
    try:
        return SonicBit(email=EMAIL,password=PASSWORD)
    except Exception as e:
        logging.error(f"Failed to Login:{str(e)}")

def torrent2link(magnet_link,smart_mode=True):
    SB=login()
    logging.info(f"Logged in as {EMAIL} Successfully")
    torrents=SB.list_torrents().torrents
    if len(torrents)>0:
        print("Torrent Existing")
        SB.delete_torrent("".join(list(torrents.keys())))
        SB.clear_storage()
        print("Deleting Existing Torrent Succesfully")
    if smart_mode:
        logging.info("Smart mode is enabled")
        SB.clear_storage()
        logging.info("Storage Cleared Succesfully")
    SB.add_torrent(magnet_link)
    logging.info(f"Torrent Added Successfully:{magnet_link}")
    sleep(20)
    while 1:
        try:
           dl_url=SB.list_files().items[0].download_url
           break
        except:
            print("Wait....\n Your File is Uploading..")
    logging.info("Download url is fetched")
    return dl_url
if __name__=="__main__":
    print(torrent2link(str(input("Paste the Magnet link Here:"))))
