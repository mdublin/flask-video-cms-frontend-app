

def input_prep(user_tag):
    '''
    This provides some amount of tolerance for user input of multiple tags with formatting for URL encoding, etc. We have very explicit instructions on form for the user, although this could be improved...
    For example, if user submits: 
        sports,basketball,nba, SMGV 
    You wind up with:
        [u'sports', u'basketball', u'nba', u'%20SMGV']
        which then becomes, via the video_feed_parser script:
            &any=tag:sports&any=tag:basketball&any=tag:nba&any=tag:%20SMGV 
        So then the Brightcove CMS is being search for the tag " SMGV" instead of just "SMGV"

    '''

    print("THIS IS user_tag in input_prep")
    print(user_tag)

    #hopefully user submitted tags properly
    #contains cleaned up tags
    tags_package = []
    
    if ',' in user_tag:
        tags = user_tag.split(',')
        print("THIS IS tags in if")
        print(tags)
        for tag in tags:
            if ' ' in tag:
                tag = tag.replace(" ", "%20")
                tags_package.append(tag)
                print(tags_package)
            else:
                tags_package.append(tag)
                print(tags_package)

        return tags_package

    elif " " in user_tag:
        #format single tag with spaces for URL
        tag = user_tag.replace(" ", "%20")
        return tag

    else:
        tag = user_tag
        return tag







