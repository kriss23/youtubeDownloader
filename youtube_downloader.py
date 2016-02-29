#!/bin/python

import urllib
import argparse
import time
import subprocess

def label_image(youtube_ID, image_title, uuid):
    print "downloading video from YouTube: http://www.youtube.com/watch?v=" + youtube_ID
    # generate unitque filename for tmp file
    output_filename = image_title.lower().replace(" ", "_") + "_" + uuid + ".mp4"

    # render output image
    subprocess.call(["/usr/bin/youtube-dl", "-f", "18",
                     "http://www.youtube.com/watch?v=" + youtube_ID,
                     "-o", "/var/www/html/trailers_de/360/" + output_filename])
    print "Done. Video rendered can be found on: http://trailers.mixd.tv/trailers_de/360/" + output_filename,

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--youtube_ID', help='URL to dowload image from')
    parser.add_argument('--title', help='Title to name the video')
    parser.add_argument('--uuid', help='UUID to name the video')
    # parser.add_argument('--restore', action='store_true', default=False, help='Restore from last Backup')
    args = parser.parse_args()
    label_image(args.youtube_ID, args.title, args.uuid)
