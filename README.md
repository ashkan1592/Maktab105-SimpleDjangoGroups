# Music Website Mini Project

This Django-based mini project aims to create a simple music website where users can add, view, and delete music entries. The project includes features such as adding new music, displaying all music, and generating reports on music statistics.

## Requirements
- Python 3.x
- Django

## Installation

1. Clone the repository:

`git clone https://github.com/yourusername/music-website.git`

2. Navigate to the project directory:

`cd music-website`

3. Install the required dependencies:

`pip install -r requirements.txt`


## Usage

1. Run the Django development server:

`python manage.py runserver`

2. Access the website in your browser at `http://localhost:8000/`.

## Features

### Add Music
- Access `/add` to add new music entries.
- Fill in the form with the required fields: name, category, URL, and cover.

### View All Music
- Access the homepage `/` to view all music entries.
- Each line displays the name of the music.

### Delete Music
- Access `/delete/<id_or_name>` to delete a music entry by its ID or name.
- If the deletion is successful, a response of 200 is provided; otherwise, 404 is returned.
- Deleted music entries are still present in the database but might not be displayed on the main page.

### Music Info
- Access `/info` to view reports on music statistics.
- Reports include the number of songs, number of songs in each category, number of categories, etc.

## Implementation Details

- All views are implemented as class-based views to maintain consistency and improve code organization.
- The project follows the Model-View-Template (MVT) architecture provided by Django.
- Frontend styling and advanced features like authentication and authorization are not included in this basic implementation.

## Contributing

Contributions are welcome! If you have suggestions or encounter issues, please open an issue or submit a pull request.


# How to Fork a Repository on GitHub

Forking a repository on GitHub allows you to create a personal copy of someone else's project. This copy is entirely separate from the original repository and can be modified without affecting the original. Here's a step-by-step guide on how to fork a repository:

## Step 1: Log in to GitHub

First, ensure you're logged in to your GitHub account. If you don't have one, you'll need to sign up for a free account at [GitHub](https://github.com/).

## Step 2: Find the Repository

Navigate to the repository you want to fork. You can search for repositories using the GitHub search bar, or you can visit the repository directly if you have the URL.

## Step 3: Fork the Repository

Once you're on the repository page, you'll find a "Fork" button in the top-right corner of the page. Click on this button. GitHub will then create a copy of the repository under your account.

## Step 4: Clone Your Fork

After forking the repository, you'll have your own copy of it under your GitHub account. To work on this repository locally on your computer, you'll need to clone it.

Open a terminal or command prompt and use the `git clone` command followed by the URL of your forked repository. For example:

```sh
git clone https://github.com/your-username/repository-name.git
```

## Step 5: Make Changes
Now that you have your own copy of the repository on your computer, you can make changes to it as needed. You can add, edit, or delete files according to your requirements.

## Step 6: Push Changes
Once you've made the desired changes to your local repository, you'll need to commit those changes and push them to your fork on GitHub.

Use the following commands:

```git add .
git commit -m "Your commit message here"
git push origin master
```

## Step 7: Create a Pull Request
If you want to contribute your changes back to the original repository, you can create a pull request.

Navigate to your fork on GitHub, click on the "Pull Requests" tab, and then click on the "New pull request" button. Follow the prompts to create a pull request with your changes. The owner of the original repository can then review your changes and decide whether to merge them.
