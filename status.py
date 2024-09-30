from flask import Flask, render_template, request, redirect, url_for
from mastodon import Mastodon, MastodonRatelimitError

app = Flask(__name__)

# Base code structure created by all of us in the team.
# Initialize Mastodon client
mastodon = Mastodon(
    access_token="D1wDyWxOM0J6db4TdiV5lEYttfB3uFio3Th1rwrYY9I",
    api_base_url="https://mastodon.social",
)

# Global variable to store the ID of the created post
created_post_id = None


@app.route("/")
def index():
    """Render the homepage."""
    return render_template(
        "index.html", post=None, retrieved_post=None, all_posts=None, error_message=None
    )


# Code written by Manjunath
@app.route("/create_post", methods=["POST"])
def create_post():
    """Create a new post on Mastodon."""
    global created_post_id
    content = request.form.get("status")
    # Refactorded and added try block by Harshavardhan
    try:
        post = mastodon.status_post(content)
        created_post_id = post.id
        return redirect(url_for("index"))
    # Refactorded and added except block by Apurva
    except MastodonRatelimitError:
        error_message = "Rate limit exceeded. Please try again later."
        return render_template(
            "index.html",
            post=None,
            retrieved_post=None,
            all_posts=None,
            error_message=error_message,
        )
    # Refactorded and added except block by Manjunath
    except Exception as e:
        error_message = f"An error occurred: {e}"
        return render_template(
            "index.html",
            post=None,
            retrieved_post=None,
            all_posts=None,
            error_message=error_message,
        )


# Code written by Harshavardhan
@app.route("/retrieve_all_posts", methods=["GET"])
def retrieve_all_posts():
    """Retrieve posts from your home timeline."""
    try:
        # Retrieve posts from the home timeline
        posts = mastodon.timeline_home()
        return render_template(
            "index.html",
            post=None,
            retrieved_post=None,
            all_posts=posts,
            error_message=None,
        )
    except MastodonRatelimitError:
        error_message = "Rate limit exceeded. Please try again later."
        return render_template(
            "index.html",
            post=None,
            retrieved_post=None,
            all_posts=None,
            error_message=error_message,
        )
    except Exception as e:
        error_message = f"An error occurred while retrieving posts: {e}"
        return render_template(
            "index.html",
            post=None,
            retrieved_post=None,
            all_posts=None,
            error_message=error_message,
        )


# Code written by Apurva
@app.route("/retrieve_post_by_id", methods=["POST"])
def retrieve_post_by_id():
    """Retrieve a post by its ID using the Mastodon API."""
    post_id = request.form.get("post_id")
    try:
        post = mastodon.status(post_id)
        return render_template(
            "index.html",
            post=None,
            retrieved_post=post,
            all_posts=None,
            error_message=None,
        )
    except MastodonRatelimitError:
        error_message = "Rate limit exceeded. Please try again later."
        return render_template(
            "index.html",
            post=None,
            retrieved_post=None,
            all_posts=None,
            error_message=error_message,
        )
    except Exception:
        error_message = f"Post with ID {post_id} not found."
        return render_template(
            "index.html",
            post=None,
            retrieved_post=None,
            all_posts=None,
            error_message=error_message,
        )


# Code written by Manjunath
@app.route("/delete_post", methods=["POST"])
def delete_post():
    """Delete the previously created post."""
    global created_post_id
    if not created_post_id:
        error_message = "No post has been created to delete."
        return render_template(
            "index.html",
            post=None,
            retrieved_post=None,
            all_posts=None,
            error_message=error_message,
        )
    try:
        mastodon.status_delete(created_post_id)
        created_post_id = None
        return redirect(url_for("index"))
    except MastodonRatelimitError:
        error_message = "Rate limit exceeded. Please try again later."
        return render_template(
            "index.html",
            post=None,
            retrieved_post=None,
            all_posts=None,
            error_message=error_message,
        )
    except Exception as e:
        error_message = f"An error occurred: {e}"
        return render_template(
            "index.html",
            post=None,
            retrieved_post=None,
            all_posts=None,
            error_message=error_message,
        )


if __name__ == "__main__":
    app.run(debug=True)
