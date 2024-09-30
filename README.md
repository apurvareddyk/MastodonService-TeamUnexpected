# MastodonService-TeamUnexpected
CPME272 HW #2 - Mastodon Service

# Mastodon Service - Group Project

## Overview

This project is a simple web-based service that integrates with the Mastodon API, allowing users to create, retrieve, and delete posts programmatically. It was developed as a group project with equal contributions from three team members: Manjunatha Inti, Apurva Karne, and Harshavardhan Gadila.

The project is built using Python for the backend logic and HTML for the frontend UI. Unit tests are provided to verify the functionality of the core features.

## Features

1. **Create a Post:** Users can create a new Mastodon post by entering their status.
2. **Retrieve a Post:** Users can retrieve a post by its ID.
3. **View Timeline:** Users can view all the posts from their Mastodon timeline.
4. **Delete a Post:** Users can delete their post by specifying the post ID.

## Project Structure

- `status.py` - Backend logic for interacting with Mastodon API
- `test_status.py` - Unit tests for the backend functionality
- `index.html` - Frontend interface for user interaction
- `README.md` - Project documentation (this file)

## Requirements

To run this project, you'll need the following:

- Python 3.x
- Flask (for web server handling)
- Mastodon.py (a Python wrapper for the Mastodon API)

Install the required Python packages using pip.

## How to Run

1. Clone this repository and navigate to the project directory.

2. Run the Flask server and open your web browser to interact with the service.

## Running Unit Tests

Run the unit tests to validate that the key functions (create, retrieve, and delete) are working as expected.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributors

- **Manjunatha Inti** - [GitHub](https://github.com/manjunatha-inti)
- **Apurva Karne** - [GitHub](https://github.com/apurva-karne)
- **Harshavardhan Gadila** - [GitHub](https://github.com/hvr2026)
