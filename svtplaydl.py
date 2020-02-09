import sys, os, re, requests, io
from subprocess import Popen, PIPE, STDOUT

SVT_URL = "https://www.svtplay.se"

def parse_series(VIDEO):
    svt_url = SVT_URL
    series = VIDEO

    r = requests.get(svt_url + '/' + series)
    html = str(r.content)
    rough_episode = re.compile(r'\"\$Episode\:.*?{"svtplay":".*?"Urls"}')
    specific_episode = re.compile(r'(?<={"svtplay":").*?(?=")')

    invoke_links = []
    for episode in rough_episode.findall(html):
        this_episode = specific_episode.findall(episode)
        if this_episode:
            invoke_links.append(svt_url + this_episode[0])
    
    return invoke_links

def _cli_request(command, logpath):
    """Invokes an OS command line request
    
    Arguments:
        command {str} -- Full command string
        logpath {str} -- Path to stdout/stderror log file
    
    """
    os.chdir(os.path.dirname(logpath))
    print("Logging stdout/stderror to:\n" + logpath + "\n")

    with Popen(command, shell=True, stdout=PIPE, stderr=STDOUT) as process, \
        open(file=logpath, mode='wt') as logfile:
            for line in io.TextIOWrapper(process.stdout, newline=''):
                sys.stdout.write(line)
                logfile.write(line)
                logfile.flush()


def svtplaydl(request,video,dlpath):
    # OS parameters - Creates course path and sets current course directory
    coursepath = os.path.join(dlpath,video)
    if not os.path.exists(coursepath):
        os.mkdir(coursepath)
    os.chdir(coursepath)

    # Quote and space char
    # # # # # # # # # # # #
    qu = '"';  sp = " "   # 
    # Download parameters
    siteurl = "https://www.svtplay.se/"
    
    # CMD Tool parameters - useful settings for the download process (youtube-dl)
    cmdtool = "youtube-dl"
    verbc = sp + "--verbose"
    template = qu + "%(playlist_index)s-%(title)s-%(resolution)s.%(ext)s" + qu
    filenamec = sp + "-o" + sp + template
    videourlc = sp + qu + request + qu
    
    # Command string
    command = cmdtool + verbc + filenamec + videourlc
    print(command)
    
    # Command execution and logging
    logpath = os.path.join(coursepath, video + ".log")
    _cli_request(command, logpath)

def videolist(scriptpath):

    # Videolist textfile prelocated in the same directory as this script
    filelist = "videolist.txt"
    
    # Loops the list's lines and stores it as a python list
    filepath = os.path.join(scriptpath,filelist)
    lines = "notNull"
    courseList = []
    with open(filepath, 'r+') as file:
        while lines != "":
            lines = file.readline()
            if lines != "":
                course = lines.split("\n")[0]
                courseList.append(course)
    return courseList

if __name__ == "__main__":

    # Script's absolute directory path
    sysfile = sys.argv[0]
    scriptabspath = os.path.abspath(sysfile)
    scriptpath = os.path.dirname(scriptabspath)
    
    # Download directory path
    dldirname = "Videos"
    dlpath = os.path.join(scriptpath,dldirname)
    if not os.path.exists(dlpath):
        os.mkdir(dlpath)
    
    # Looping through the videolist determined by videolist()
    videoList = videolist(scriptpath)
    for video in videoList:
        invoke_links = parse_series(video)
        for request in invoke_links:
            svtplaydl(request,video,dlpath)
