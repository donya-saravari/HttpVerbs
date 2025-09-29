import requests
def get_request(url):
    response = requests.get(url)
    print("GET Request:")
    print("Status Code: ", response.status_code)
    print("Response Body: ", response.json())
    print()
def post_request(url, data):
    response = requests.post(url, json=data)
    print("POST Request:")
    print("Status Code: ", response.status_code)
    print("Response Body: ", response.json())
    print()
def put_request(url, data):
    response = requests.put(url, json=data)
    print("PUT Request:")
    print("Status Code: ", response.status_code)
    print("Response Body: ", response.json())
    print()
def delete_request(url):
    response = requests.delete(url)
    print("DELETE Request:")
    print("Status Code: ", response.status_code)
    print("Response Body: ", response.json())
    print()
def read_all_posts(url):
    response = requests.get(url)
    print("All Posts:")
    print("Status Code: ", response.status_code)
    posts = response.json()
    for post in posts:
        print(f"Post ID: {post['id']}, Title: {post['title']}")
        print()
def main():
    base_url = "https://jsonplaceholder.typicode.com"
    get_request(f"{base_url}/posts/2")
    post_data = {
        "id": 1,
        "title": "new post title",
        "body": "the body of the post",
        "userId": 1,
    }
    post_request(f"{base_url}/posts", post_data)
    put_data = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1,
    }
    put_request(f"{base_url}/posts/1", put_data)
    delete_request(f"{base_url}/posts/1")
if __name__ == "__main__":
    main()