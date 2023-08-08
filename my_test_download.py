from anylearn.config import init_sdk, print_config
from anylearn.interfaces.resource import Resource, ResourceDownloader, AsyncResourceDownloader, SyncResourceDownloader

from threading import Thread


init_sdk('http://192.168.10.22:30128', 'xlearn', '123456')

file_id = "FILEb1b48c7811eb92069a7180c2256e"
save_path = "/data/wtt/"
# file_id = "FILE49f6f9c511eba043763c62e0eb8e"
# save_path = "D:\\anyctl-test\\download\\export_best_model"

downloader = AsyncResourceDownloader()
t_download = Thread(target=Resource.download_file,
                    kwargs={
                        'resource_id': file_id,
                        'save_path': save_path,
                        'downloader': downloader,
                        'polling': 2,
                    })
print("====== Downloading...")
t_download.start()
t_download.join()
print("====== Done")

# downloader = SyncResourceDownloader()
# res = Resource.download_file(resource_id=file_id,
#                              save_path=save_path,
#                              downloader=downloader,
#                              polling=1)
# print(f"====== Resource download {res}")
