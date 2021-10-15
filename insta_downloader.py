import requests as req
import re
import wget


def get_response(url):
    r = req.get(url)
    while r.status_code != 200:
        for i in range(1,10):
            i=i+1
            r = req.get(url)
        break
    return r.text

def sorting(matches):
    return list({match.replace("\\u0026","&") for match in matches})

#def download(final_urls):
#    wget.download(final_urls)
 #   print(f"Image/video Successfully Downloaded")

url = input("Enter IG [video/image/post] link: \n")
response = get_response(url)
#print(f'{req.get(url).status_code}')
video = re.findall('"video_url":"([^"]+)"', response)
image = re.findall('"display_url":"([^"]+)"', response)

vid_urls = sorting(video)
img_urls = sorting(image)
#print(vid_urls)
#print(img_urls)
if vid_urls:
    print('Video-Src:\n{0}'.format('\n'.join(vid_urls)))
    final = format('\n'.join(vid_urls))
    wget.download(final)

elif img_urls:
    print('Image-Src:\n{0}'.format('\n'.join(img_urls)))
    final = format('\n'.join(img_urls))
    wget.download(final)
else:
    print(f"Error: check the url. \n {url}")


#final = input("Enter the src: \n")
#final = img_urls.


