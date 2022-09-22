from flask import abort, send_file, render_template, redirect, url_for
import os

from webapp import app
from webapp.utils import find_latest, get_all_images


BASE_DIR = os.getcwd()


@app.route("/", defaults={"req_path": ""})
@app.route("/<path:req_path>")
@app.route("/collections/<path:req_path>")
def collections(req_path):
    # Joining the base and the requested path
    root_path = os.path.join(BASE_DIR, "collections")
    latest = find_latest(root_path)
    abs_path = os.path.join(root_path, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = sorted(
        os.listdir(abs_path),
        key=lambda _: int(_.split("/")[-1].replace(".png", "")),
        reverse=True,
    )

    return render_template("index.html", latest=latest, files=files)


@app.route("/analyze/<string:area>")
def analyze(area):
    if not area:
        return redirect(url_for("collections"))
    root_path = os.path.join(BASE_DIR, "collections")
    images = sorted(get_all_images(area), reverse=True)
    return render_template("analyze.html", images=images)
