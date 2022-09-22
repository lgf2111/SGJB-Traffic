from flask import abort, send_file, render_template
import os

from webapp import app
from webapp.utils import find_latest


@app.route("/", defaults={"req_path": ""})
@app.route("/<path:req_path>")
@app.route("/collections/<path:req_path>")
def dir_listing(req_path):
    BASE_DIR = os.getcwd()

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
    files = os.listdir(abs_path)

    return render_template("index.html", latest=latest, files=files)
