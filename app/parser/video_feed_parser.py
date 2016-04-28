#! /usr/bin/python
# -*- coding: utf-8 -*-

print "Content-type: application/json\n\n"
import requests
import feedparser
import json

#receiving user_tag text submitted by user via TagSearchForm on http://127.0.0.1:5000/protected

def load(user_tag):
    
    video_feed = 'http://api.brightcove.com/services/library?command=search_videos&any=tag:{}&output=mrss&media_delivery=http&sort_by=CREATION_DATE:DESC&token=8-XmRYT4C6VKYvvCGoJhcaGFX-t7ZO-ML3eXD95oalq6obm5ho7eJg..'.format(user_tag)
    
    d = feedparser.parse(video_feed)

    response_array = []

    # -- For each item in the feed
    for index, post in enumerate(d.entries):
        if index >= 1:
            break
        # Here we set up a dictionary in order to extract selected data from the
        # original brightcove "post" result
        item = {}
        
        item['name'] = post.title,
        item['description'] = post.description,
        item['url'] = u"%s" % post.link,
        # item['tags'] = post.media_keywords.split(",")
        item['videoID'] = post.bc_titleid,

        max_bitrate = 0
        vid_url = None
        videos = post.media_content

        # -- For each video in the item dict
        for video in videos:
            # -- If the video has a value for its bitrate
            if 'bitrate' in video:
                # -- Extract the value of this video's bitrate
                bitrate_str = video['bitrate']
        # -- and convert it to an integer (by default it is a string in the XML)
                curr_bitrate = int(bitrate_str)
            # -- If the bitrate of this video is greater than
            # -- the highest bitrate we've seen, mark this video as the one with
            # -- the highest birate.
                if curr_bitrate > max_bitrate:
                    max_bitrate = curr_bitrate
                vid_url = video['url']
        # -- This line simply prints out the maximum bitrate and current video URL for each iteration
        # print "{} url {}".format(max_bitrate, vid_url)
        # print "highest bitrate {} url {}".format(max_bitrate, vid_url)

        item['url'] = vid_url
        videoID = item['videoID']
        # new line
        videoName = item['name']
        response_array.append(item)

        videoID = str(videoID)
        videoUrl = vid_url
        # videoName = str(videoName) #we have to convert videoName to a plain
        # old string instead of leaving it as unicode because the dudupe
        # function in our db script is "seeing" the video titles in our db
        for i in videoName:
            videoNameConverted = i  # Extracting the video title out of the tuple its in, so we can get string utf-8 encoded. So everwhere below this, we're replacing videoName with videoNameConverted
        # foo = type(i)
        # print "this is type check of tuple extract on line 70: %s" % foo
        videoDescription = item['description']


        print(response_array)
        print(type(response_array))

        asset_dict = response_array[0]
        extract_from_tup = asset_dict['videoID']
        
        return extract_from_tup[0]


        '''if videoExists(videoID):
            print "This video has already been uploaded to Facebook."
            print videoID
            print videoNameConverted

        if not videoExists(videoID):
            print "Haven't seen", videoNameConverted and videoID, "before, adding it to Facebook!"
            access = '<Facebook permanent access token>'

            fburl = 'https://graph-video.facebook.com/v2.3/<page id>/videos?access_token=' + \
                str(access)
            # In the payload we're using title instead of name, so that the
            # actual video title is posted to the timeline (name wasn't
            # working, so the description was posted instead)
            payload = {
                'name': '%s' % (videoNameConverted),
                'description': '%s' % (videoDescription),
                'file_url': '%s' % (videoUrl)}
            flag = requests.post(fburl, data=payload).text
            print flag
            fb_res = json.loads(flag)
            print fb_res
            if not "error" in fb_res:
                addVideo(videoID, videoNameConverted)
            else:
                print "An error occured uploading to facebook for ", videoNameConverted'''
