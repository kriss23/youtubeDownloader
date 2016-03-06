#!/bin/python

import urllib
import argparse
import time
import os.path
import subprocess


VIDEO_PATH_720 = "/var/www/html/trailers_de/720/"
VIDEO_PATH_360 = "/var/www/html/trailers_de/360/"

def label_image(youtube_ID, image_title, uuid):
    print "downloading video from YouTube: http://www.youtube.com/watch?v=" + youtube_ID
    # generate unitque filename for tmp file
    output_filename = image_title.lower().replace(" ", "_") + "_" + uuid + ".mp4"

    output_path_720 = VIDEO_PATH_720 + output_filename
    output_path_360 = VIDEO_PATH_360 + output_filename

    # render output image
    subprocess.call(["/usr/bin/youtube-dl", "-f", "22", # 18 for 320p and 22 for 720p
                     "http://www.youtube.com/watch?v=" + youtube_ID,
                     "-o", output_path_720])
    subprocess.call(["/usr/bin/youtube-dl", "-f", "18", # 18 for 360p and 22 for 720p
                     "http://www.youtube.com/watch?v=" + youtube_ID,
                     "-o", output_path_360])

    if os.path.isfile(output_path_720):
        print "Done. Video rendered can be found on: http://trailers.mixd.tv/trailers_de/720/" + output_filename,
    elif os.path.isfile(output_path_360):
        # fallback to 360p resolution
        print "Done. Video rendered can be found on: http://trailers.mixd.tv/trailers_de/360/" + output_filename,
    else:
        print "Error: file could not be found in 720p or 360p resolution."

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--youtube_ID', help='URL to dowload image from')
    parser.add_argument('--title', help='Title to name the video')
    parser.add_argument('--uuid', help='UUID to name the video')
    # parser.add_argument('--restore', action='store_true', default=False, help='Restore from last Backup')
    args = parser.parse_args()
    label_image(args.youtube_ID, args.title, args.uuid)
