import io
import sys
import urllib.request as request

BUFF_SIZE = 1024

def download_lenght(response, output, lenght):
    times = lenght // BUFF_SIZE
    if lenght % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Download %d" %(((time * BUFF_SIZE) / lenght) * 100))

def download(response, output):
    total_download = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_download += len(data)
        if not data:
            break
        output.write(data)
        print("Downloaded {bytes}".format(bytes = total_download))

def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("saida.zip", mode = "w")

    content_lenght = response.getheader('Content-Length')
    if content_lenght:
        lenght = int(content_lenght)
        download_lenght(response, out_file, lenght)
    else:
        download(response, out_file)
    
    response.close()
    out_file.close()
    print("Finished")

if __name__ == "__main__":
    main()