#!/usr/bin/env python3

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints their titles.
    Prints the HTTP status code and the titles of each post.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.
    Creates a CSV file named 'posts.csv' with columns 'id', 'title', and 'body'.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
        print("Posts saved to posts.csv")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
