import json, os
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
DIST = "."

def build_post(slug: str, post: dict, site: dict, year: int):
    html = env.get_template("post.html").render({
        "post": post,
        "site": site,
        "now": {"year": year}
    })

    out_dir = os.path.join(DIST, slug)
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--posts", required=True)
    parser.add_argument("--site", required=True)
    parser.add_argument("--year", type=int, required=True)
    args = parser.parse_args()

    posts = json.loads(args.posts)
    site = json.loads(args.site)

    print("Total posts:", len(posts))

    for post in posts:
        slug = post["slug"]
        print(f"Building post: {slug}")
        build_post(slug, post, site, args.year)
