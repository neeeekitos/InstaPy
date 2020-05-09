import math
import random
from time import sleep
from selenium import webdriver

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
# driver = webdriver.Chrome(chrome_options=chrome_options)

from instapy import InstaPy, smart_run
from instapy.like_util import get_links_for_tag, check_link
from instapy.unfollow_util import follow_user
from selenium.common.exceptions import NoSuchElementException
from instapy_chromedriver import binary_path

photo_comments = ['Nice shot! @{}',
                 'I love your profile! @{}',
             'Your feed is an inspiration :thumbsup:',
             'Just incredible :open_mouth:',
             'What camera did you use @{}?',
             'Love your posts @{}',
             'Looks awesome @{}',
             'Getting inspired by you @{}',
             ':raised_hands: Yes!',
             'I can feel your passion @{} :muscle:']

#nogui = true when running on linux instead of headless browser
session = InstaPy(username="eco_latitude", password="PERICOrokuGIN700", headless_browser=False, bypass_security_challenge_using='sms')
with smart_run(session):
   session.set_comments(photo_comments, media='Photo')
   session.join_pods(topic = 'food')


#### SETTINGS ###
session.set_quota_supervisor(enabled=True,
                             sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                             sleepyhead=True, stochastic_flow=True, notify_me=True,
                             peak_likes_hourly=random.randint(40, 60),
                             peak_likes_daily=random.randint(300, 340),
                             peak_comments_hourly=random.randint(12,14),
                             peak_comments_daily=random.randint(70,80),
                             peak_follows_hourly=random.randint(10,27),
                             peak_follows_daily=random.randint(70,80),
                             peak_unfollows_hourly=35,
                             peak_unfollows_daily=402,
                             peak_server_calls_hourly=None,
                             peak_server_calls_daily=4700)

#watch stories
session.set_do_story(enabled=True, percentage=random.randint(20,40), simulate=True)

#all necessary settings here

session.set_simulation(enabled=True, percentage=66)
#skip private accounts
session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=True)
#comment if minimum 4 comments
session.set_delimit_commenting(enabled=True, min_comments=3,comments_mandatory_words=['choco', 'chocolat',
                                                                                      'bonappetit', 'chocolatier',
                                                                                      'artisanat', 'bio',
                                                                                      'gourmand', 'gourmandise',
                                                                                      'tablettes', 'gourmands',
                                                                                      'cuisine', 'recette',
                                                                                      'création', 'beauté',
                                                                                      'photographe', 'nature',
                                                                                      'légende', 'magique',
                                                                                      'photographie', 'paysage',
                                                                                      'plantes', 'photography',
                                                                                      'ballade', 'photographe',
                                                                                      'bon week-end', 'ballades',
                                                                                      'voyage', 'rêve',
                                                                                      'rêver', 'beau',
                                                                                      'amazonie', 'equateur',
                                                                                      'délicieux', 'artisanal',
                                                                                      'éco', 'magnifique',
                                                                                      'formidable', 'dessert',
                                                                                      'cuisine', 'organique',
                                                                                      'apero', 'belle',
                                                                                      'joli', 'repas',
                                                                                      'idéal', 'féve',
                                                                                      'régal', 'bel'])
#set delimit liking
session.set_delimit_liking(enabled=True, max_likes=1005, min_likes=20)

#only needed for interact_by... actions
session.set_do_like(enabled=True, percentage=60)

#######################
#comments
session.set_do_comment(enabled=True, percentage=25)
session.set_comments([u'Magnifique 😍', 'Super!', 'Wouaah magnifique!','Merci de partager de belles photos comme celle-là avec nous! 😍',
                      'Wouaah, j’adore!', 'Mmm magnifique!'])
session.set_comments(['Nice shot! @{}', 'Belle photo !@{}', 'Woow c\'est beau! @{}'], media='Photo')
#######################

#follows
session.set_do_follow(enabled=True, percentage=10, times=1)

#######################
#smart hashtags
session.set_smart_location_hashtags(['16366456/monaco','c774666/montpellier-france', 'c770236/lyon-france', 'FR/france',
                                     'c777934/paris-france', 'c753315/grenoble-france',
                                     'c775739/nantes-france', 'c795852/versailles-france',
                                     'c733103/annecy-france', 'c768995/lille-france',
                                     'c792225/strasbourg-france', 'c775712/nancy-france',
                                     'c740869/cannes-france', 'c793635/tours-france'], radius=20,
                                    limit=10)
session.set_smart_hashtags(['chocolat', 'bio', 'yummy', 'instafood', 'delicious', 'healthyfood', 'tasty','miam', 'cuisine', 'food', 'foodporn'], limit=random.randint(5,8), sort='top', log_tags=True)
#######################

#interactions settings
session.set_relationship_bounds(enabled=True,
                                potency_ratio=None,
                                delimit_by_numbers=True,
                                max_followers=8500,
                                max_following=4490,
                                min_followers=100,
                                min_following=56,
                                min_posts=10,
                                max_posts=1000)

#sleep after every action
session.set_action_delays(enabled=True,
                          like=38,
                          comment=400,
                          follow=45,
                          unfollow=42, story=7, randomize=True, random_range_from=70, random_range_to=140)


#### ACTIONS ###
for cycle in range(7):

    session.like_by_tags(amount=random.randint(10,50), use_smart_location_hashtags=True, randomize = True)

    session.like_by_locations(['224442573'], amount=100)
    session.follow_by_tags(amount=random.randint(10,30), use_smart_location_hashtags=True, randomize = True)

    # Interact with the people that a given user is followed by
    # set_do_comment, set_do_follow and set_do_like are applicable
    session.set_user_interact(amount=random.randint(2,10), randomize=True, percentage=50, media='Photo')
    session.set_do_follow(enabled=True, percentage=20)
    session.set_do_like(enabled=False, percentage=40)
    session.set_comments([u'Magnifique 😍', 'Super!', 'Wouaah magnifique!'])
    session.set_do_comment(enabled=True, percentage=10)
    session.interact_user_followers(['lepetitcarredechocolat','ccilouuups','marie_roudiere', 'foodieinspi','lavieenplusjolie_'] , amount=random.randint(2,15), randomize=True)



    session.follow_by_tags(amount=random.randint(10,30), use_smart_location_hashtags=True, randomize = True)

    session.like_by_tags(amount=random.randint(10,50), use_smart_location_hashtags=True, randomize = True)

    # Interact with the people that a given user is followed by
    # set_do_comment, set_do_follow and set_do_like are applicable
    session.set_user_interact(amount=random.randint(2,10), randomize=True, percentage=50, media='Photo')
    session.set_do_follow(enabled=True, percentage=20)
    session.set_do_like(enabled=False, percentage=40)
    session.set_comments([u'Mmmmmh ça a l’air délicieux 😋', 'Super 😋', 'Miammm! Connaissez vous le chocolat équatorien?'])
    session.set_do_comment(enabled=True, percentage=10)
    session.interact_user_followers(['mum.and.patisserie','marie.sweet.pastry','stefanolaghi66','gnawchocolatefrance','empanadas_club','mamanvogue'],
                                    amount=random.randint(2, 15), randomize=True)

    session.like_by_tags(amount=random.randint(10,50), use_smart_location_hashtags=True, randomize = True)

    # Interact with the people that a given user is followed by
    # set_do_comment, set_do_follow and set_do_like are applicable
    session.set_user_interact(amount=random.randint(2,10), randomize=True, percentage=50, media='Photo')
    session.set_do_follow(enabled=True, percentage=20)
    session.set_do_like(enabled=False, percentage=40)
    session.set_comments([u'Merci de partager de belles photos comme celle-là avec nous! 😍', 'Wouaah, j’adore!', 'Mmm magnifique!'])
    session.set_do_comment(enabled=True, percentage=10)
    session.interact_user_followers(['cookies_et_mignardises','cizzystudio','emilie_mazere','praline_et_caramel','croustilicious.gaellemarot'],
                                    amount=random.randint(2, 15), randomize=True)

    session.follow_by_tags(amount=random.randint(10,30), use_smart_location_hashtags=True, randomize = True)



session.end()
