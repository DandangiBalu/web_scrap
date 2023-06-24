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
