import argparse, json, os
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
DIST = "."

def build_site(template_name: str, slug: str, context: dict):
    html = env.get_template(template_name).render(context)

    out_dir = os.path.join(DIST, slug)
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
        
parser = argparse.ArgumentParser()
parser.add_argument("--posts", required=True)
parser.add_argument("--site", required=True)
parser.add_argument("--year", type=int, required=True)

args = parser.parse_args()
posts = json.loads(args.posts)
site = json.loads(args.site)

posts = posts[::-1]  # reverse to have newest first

print("Number of posts:", len(posts))
print("Year:", args.year)
print("Site title:", site["title"])

build_site("index.html", "", {
    "posts": posts,
    "site": site,
    "now": {"year": args.year}
})
