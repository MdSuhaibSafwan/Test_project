from django import template

register = template.Library()  


def count_user_posts(user):
    qs = user.content_set.all()
    return qs.count()


def add(x, y):
    return x + y


register.filter(name="count_user_posts", filter_func=count_user_posts)  # registering a filter function
