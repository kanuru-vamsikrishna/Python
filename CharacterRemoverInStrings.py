"""
Background
We've got a very long string, containing a bunch of User IDs. This string is a listing, which seperates each user ID with a comma and a whitespace ("' "). Sometimes there are more than only one whitespace. Keep this in mind! Futhermore, some user Ids are written only in lowercase, others are mixed lowercase and uppercase characters. Each user ID starts with the same 3 letter "uid", e.g. "uid345edj". But that's not all! Some stupid student edited the string and added some hashtags (#). User IDs containing hashtags are invalid, so these hashtags should be removed!

Task
Remove all hashtags
Remove the leading "uid" from each user ID
Return an array of strings --> split the string
Each user ID should be written in only lowercase characters
Remove leading and trailing whitespaces
"""

import re

def get_users_ids(st):
    i = 0
    initArray = st.split(',') or st.split(' ')
    finalArray = []
    while i < len(initArray):
        if '#' in initArray[i] or 'uid' in initArray[i]:
            string =  initArray[i].replace('#', '').strip()
            actualString = string[3:] if string.startswith('uid') else string.strip()
            finalArray.append(actualString.lower().strip())
        else:
            finalArray.append(initArray[i].lower().strip())
        i += 1
    return finalArray

result = get_users_ids("uid345edj")
print("Result:", result)