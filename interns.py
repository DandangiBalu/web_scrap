import requests
from bs4 import BeautifulSoup
import instaloader

loader = instaloader.Instaloader()
profile = instaloader.Profile.from_username(loader.context, 'chennaiipl')

url = 'https://www.instagram.com/chennaiipl/'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

# Scrape biography
biography_element = soup.find('meta', property='og:description')
biography = biography_element['content'] if biography_element else "Biography not found"


# Scrape user ID
user_id_element = soup.select_one('script[type="application/ld+json"]')
if user_id_element:
    user_id = user_id_element.get('data-id', 'User ID not found')
else:
    user_id = 'User ID not found'

# Scrape follower count
follower_element = soup.find('span', {'class': 'g47SY'})
follower_count = follower_element.text if follower_element else "Follower count not found"

# Scrape following count
following_count = ""
following_element = soup.find_all('span')
for span in following_element:
    if "Following" in span.text:
        following_count = span.text.split()[0]
        break
if not following_count:
    following_count = "Following count not found"

# Scrape post count
post_count_element = soup.find('span', {'class': 'g47SY'})
if post_count_element:
    post_count = post_count_element['title']
else:
    post_count = "Post count not found"

# Scrape profile picture URL
profile_picture_element = soup.find('img', {'class': 'be6sR'})
profile_picture_url = profile_picture_element['src'] if profile_picture_element else "Profile picture not found"

# Get the required information
biography = profile.biography
user_id=profile.userid
follower_count = profile.followers
following_count = profile.followees
post_count = profile.mediacount
profile_picture_url = profile.profile_pic_url

# Print the scraped data
print('Biography:', biography)
print('User ID:', user_id)
print('Follower count:', follower_count)
print('Following count:', following_count)
print('Post count:', post_count)
print('Profile picture URL:', profile_picture_url)


















# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

# responce=requests.get("https://www.instagram.com/chennaiipl/")
# soup=BeautifulSoup(responce.content,'lxml')

# biography=soup.find_all('div',class_='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1')
# bio_graphy=[]
# for i in biography:
#     d=i.get_text()
#     bio_graphy.append(d)
# print(bio_graphy)






# import requests
# from bs4 import BeautifulSoup

# url = 'https://twitter.com/DHONiOffiCiaL'
# response = requests.get(url)
# html_content = response.content

# soup = BeautifulSoup(html_content, 'html.parser')

# biography = soup.find('div', {'class': 'ProfileHeaderCard-bio u-dir'}).text.strip()
# followers_count = int(soup.find('li', {'class': 'ProfileNav-item--followers'}).find('a').find('span', {'class': 'ProfileNav-value'}).get('data-count'))
# following_count = int(soup.find('li', {'class': 'ProfileNav-item--following'}).find('a').find('span', {'class': 'ProfileNav-value'}).get('data-count'))
# likes_count = int(soup.find('li', {'class': 'ProfileNav-item--favorites'}).find('a').find('span', {'class': 'ProfileNav-value'}).get('data-count'))
# user_id = int(soup.find('div', {'class': 'ProfileNav'}).find('a').get('data-user-id'))

# data = {
#     'biography': biography,
#     'followers_count': followers_count,
#     'following_count': following_count,
#     'likes_count': likes_count,
#     'user_id': user_id
# }

# print(data)
