from .models import *

def get_user_height(current_user):
    if current_user.is_authenticated:
        if current_user.info:
            height = current_user.info[0].height
            return height
    return None


def get_user_weight(current_user):
    if current_user.is_authenticated:
        if current_user.info:
            weight = current_user.info[0].weight
            return weight
    return None


def get_user_age(current_user):
    if current_user.is_authenticated:
        if current_user.info:
            age = current_user.info[0].age
            return age
    return None


def get_user_gender(current_user):
    if current_user.is_authenticated:
        if current_user.info:
            gender = current_user.info[0].gender
            return gender
    return None


def get_user_activity_level(current_user):
    if current_user.is_authenticated:
        if current_user.info:
            activity_level = current_user.info[0].activity_level
            return activity_level
    return None