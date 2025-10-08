import requests
class WebLogClient:
    def __init__(self):
      self.base_url = "https://jsonplaceholder.typicode.com"

    def get_post(self, post_id: int):
        route = f"/posts/{post_id}"
        url = self.base_url + route
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def create_post(self, post_id: int, title: str, body: str, user_id: int):
        route = f"/posts"
        url = self.base_url + route
        data = {
            "id": post_id,
            "title": title,
            "body": body,
            "userId": user_id,
        }
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def edit_post(self, post_id: int, user_id: int, title = None, body = None):
        route = f"/posts/{post_id}"
        url = self.base_url + route
        data = {
            "id": post_id,
        }
        if title is not None:
            data["title"] = title
        if body is not None:
            data["body"] = body
        data["userId"] = user_id
        response = requests.put(url, json=data)
        response.raise_for_status()
        return response.json()

    def delete_post(self, post_id: int):
        route = f"/posts/{post_id}"
        url = self.base_url + route
        response = requests.delete(url)
        response.raise_for_status()
        return response.json()

    def read_all_posts(self):
        route = "/posts"
        url = self.base_url + route
        response = requests.get(url)
        response.raise_for_status()
        print("All Posts:")
        posts = response.json()
        for post in posts:
            print(f"Post ID: {post['id']}, Title: {post['title']}")
            print()
def main():
    weblog = WebLogClient()
    post_id = 10
    my_post = weblog.get_post(post_id=post_id)
    print(f"Read post: {post_id}")
    print(my_post)
    create_post_id = 2
    create_post_title = "new post title"
    create_post_body = "new post body"
    create_post_user_id = 1
    create_post = weblog.create_post(create_post_id, create_post_title, create_post_body, create_post_user_id)
    print(f"create post number: {create_post_id}")
    print(create_post)
    edit_post_id = 1
    edit_post_title = "updated title"
    edit_post_body = "updated body"
    edit_post_user_id = 1
    edit_post = weblog.edit_post(edit_post_id,edit_post_user_id,edit_post_title , edit_post_body )
    print(f"edit post number: {edit_post_id}")
    print(edit_post)
    delete_post_id = 3
    delete_post = weblog.delete_post(delete_post_id)
    print(f"delete post number: {delete_post_id}")
    print(delete_post)
if __name__ == "__main__":
    main()