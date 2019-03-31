import sys, os
from subprocess import Popen, PIPE, STDOUT

def svtplaydl(VIDEO,DLPATH):

    # OS parameters - Creates course path and sets current course directory
    coursepath = os.path.join(DLPATH,VIDEO)
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
    videourlc = sp + qu + siteurl + VIDEO + qu
    
    # Command string
    cmd = cmdtool + verbc + filenamec + videourlc
    
    # Command execution and logging
    bufflen = 512
    logile = VIDEO + ".log"
    logpath = os.path.join(coursepath,logile)
    with Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT, bufsize=bufflen) as process, \
        open(logpath, 'ab',bufflen) as file:
        for line in process.stdout:
            sys.stdout.buffer.write(line)
            file.flush()
            file.write(line)
            file.flush()

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
    DLPATH = os.path.join(scriptpath,dldirname)
    if not os.path.exists(DLPATH):
        os.mkdir(DLPATH)
    
    # Looping through the videolist determined by videolist()
    videoList = videolist(scriptpath)
    for VIDEO in videoList:
        svtplaydl(VIDEO,DLPATH)
