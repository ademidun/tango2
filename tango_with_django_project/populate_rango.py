import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

# Why are the import statements mixed with os.environ and django.setup()
# We do this because we want to import the Django settings for the
# models we want to use, otherwise an exception will be raised.

def populate():
    python_cat = add_cat('Python',
        views=128,
        likes=64,)

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/",
             views=14)

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
             views=4)

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
             views=10)

    django_cat = add_cat("Django",
        views=64,
        likes=32,)

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
             views=33)

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
             views=37)

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",
             views=77)

    frame_cat = add_cat("Other Frameworks",
        views=32,
        likes=16,)

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
             views=74)

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",
             views=74)

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "Cat: {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name,views=0,likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    # [0] is necessary because method returns a tuble of the instance
    #  and a boolean creatd if the method already existed (get) or had to be created
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()