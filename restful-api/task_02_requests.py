#!/usr/bin/env python3

import requests
import csv


def fetch_and_print_posts():
    """Function that fetches all post from JSONPlaceholder"""
    # printing response codes
    responses = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(responses.status_code))

    # If the request was sucessfull
    if responses.status_code == 200:
        posts = responses.json()
        # print the titles of all the posts
        for i in posts:
            print(i.get("title"))


def fetch_and_save_posts():
    """
    Function that fetches all post from JSONPlaceholder
    and saves it
    """
    responses = requests.get('https://jsonplaceholder.typicode.com/posts')

    if responses.status_code == 200:
        posts = responses.json()

    # creating list of dictionaries
    posts_dict = []
    for i in posts:
        posts_dict.append = (
            {"id": i.get("id"),
             "title": i.get("title"),
             "body": i.get("body")}
        )

    # save to cvs file
    with open('posts.csv', mode='w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(posts_dict)
