# Automated download from SVTPlay with `svtplaydl.py`

You can download whole courses from a number of tutorial sites with the CLI tool `youtube-dl`, however, in this Git I have provided an Python script, `svtplaydl.py`,  for automated download of a **whole sequence of SVTPlay series** at once using `youtube-dl` as a subprocess. Below I give an example of how to use the `svtplaydl.py` script to get videos from an arbitrary large list of series at their site.

## Installation of youtube-dl

##### For **macOS/UNIX**

With [`brew`](https://brew.sh/)  for macOS:

```bash
brew install youtube-dl
```

With [`npm`](https://www.npmjs.com/):

```bash
npm install youtube-dl
```

Or you can `curl`/`wget` the thing:

```bash
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```
```bash
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```


##### For Windows

Download with npm as above or just download the `exe`-file from the link below and [put the `exe` in your _PATH_](https://gist.github.com/jesperorb/836cb398e4bb8dc149902d68d3711295).

Or download with `npm` like above.

[Source: youtube-dl download](https://rg3.github.io/youtube-dl/download.html)

## Usage

### Download from **SVTPlay** with `pluradl.py`
After installation of youtube-dl (thus is avaiable to the environment) make sure that `courselist.txt` is in the same directory as `svtplaydl.py` with the video ID's of your choice **listed row by row**. 

Run the command below in your terminal to download all the videos from all the series in `videolist.txt`. The videos will be automatically placed in course specific folders and named by playlist order number. Supply `videolist.txt` with your desired series  and do the following ...

```bash
python svtplaydl.py
```

... with `videolist.txt` available at the same path ...

courselist.txt
```notepad
svenska-nyheter
den-forsta-manniskan
.
.
.
```
