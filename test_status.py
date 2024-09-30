import unittest
from unittest.mock import patch, MagicMock
from status import app


# Base code is written by all of us in the team.
class TestMastodonService(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    # Code written by Manjunath
    @patch("status.mastodon.status_post")
    def test_create_post(self, mock_status_post):
        # Mock the response from mastodon.status_post
        mock_post = MagicMock()
        mock_post.id = 66934
        mock_status_post.return_value = mock_post

        response = self.app.post(
            "/create_post", data={"status": "Test post"}, follow_redirects=False
        )

        # Check for redirect to '/'
        self.assertEqual(response.status_code, 302)

    # Code written by Apurva
    @patch("status.mastodon.status")
    def test_retrieve_post_by_id(self, mock_status):
        # Mock the response from mastodon.status
        mock_post = MagicMock()
        mock_post.id = 66934
        mock_post.content = "Test post content"
        mock_post.account.display_name = "Test User"
        mock_post.account.username = "testuser"
        mock_post.account.acct = "testuser"
        mock_status.return_value = mock_post

        response = self.app.post("/retrieve_post_by_id", data={"post_id": "66934"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test post content", response.data)

    # Code written by Harshavardhan
    @patch("status.mastodon.timeline_home")
    def test_retrieve_all_posts(self, mock_timeline_home):
        # Mock the response from mastodon.timeline_home
        mock_post = MagicMock()
        mock_post.id = 66934
        mock_post.content = "Timeline post content"
        mock_post.account.display_name = "Timeline User"
        mock_post.account.username = "timelineuser"
        mock_post.account.acct = "timelineuser"
        mock_timeline_home.return_value = [mock_post]

        response = self.app.get("/retrieve_all_posts")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Timeline post content", response.data)

    # Code written by Manjunath
    @patch("status.mastodon.status_delete")
    def test_delete_post(self, mock_status_delete):
        # Assume created_post_id is set
        with app.app_context():
            app.created_post_id = 66934

        response = self.app.post("/delete_post", follow_redirects=False)

        # Check for redirect to '/'
        self.assertEqual(response.status_code, 302)

    # Code written by Apurva
    @patch("status.mastodon.status_post")
    def test_create_post_rate_limit_error(self, mock_status_post):
        # Simulate a rate limit error
        mock_status_post.side_effect = Exception("Rate limit exceeded.")

        response = self.app.post("/create_post", data={"status": "Test post"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"An error occurred", response.data)

    # Code written by Harshavardhan
    @patch("status.mastodon.status")
    def test_retrieve_post_by_id_not_found(self, mock_status):
        # Simulate a post not found error
        mock_status.side_effect = Exception("Post not found.")

        response = self.app.post("/retrieve_post_by_id", data={"post_id": "99999"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Post with ID 99999 not found.", response.data)


if __name__ == "__main__":
    unittest.main()
