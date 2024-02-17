# Music Application

## Overview
The Music Application is a web-based platform designed to help users manage and interact with music-related data. It provides functionalities for adding, viewing, and deleting music entries, as well as displaying counts of albums, categories, and music entries.

## Installation
1. **Clone the repository:** Begin by cloning the repository to your local machine using Git.
```
git clone git@github.com:pedramkarimii/Maktab105-SimpleDjangoGroups.git
```

2. **Install dependencies:** Navigate to the project directory and install the required dependencies using pip.
```
cd music-application
pip install -r requirements.txt
```

3. **Configure database settings:** Open the `settings.py` file and configure the database settings according to your environment (e.g., SQLite, MySQL, PostgreSQL).

4. **Run migrations:** Apply database migrations to create the necessary tables in the database.
```
python manage.py makemigrations
python manage.py migrate
```

5. **Start the development server:** Run the Django development server to launch the application.
```
python manage.py runserver
```

## Features
- **Add Music:** Users can add new music entries by providing details such as URL, cover image, and album.
- **View Information:** The application allows users to view information about existing music entries, including title, artist, album, release date, and modification date.
- **Delete Music:** Users have the option to delete music entries by name or ID.
- **Count Statistics:** The application displays counts of albums, categories, and music entries to provide insights into the database content.

## Usage
1. **Access the application:** Open a web browser and navigate to the URL where the application is hosted.
2. **Add Music:** Use the 'Add Music' feature to add new music entries to the database.
3. **View Information:** Explore existing music entries and their details in the 'Info' section of the application.
4. **Delete Music:** Delete unwanted music entries using the 'Delete' feature. You can delete entries by name or ID.
5. **Count Statistics:** Check the 'Count' section to view statistics such as the total number of albums, categories, and music entries in the database.

## Troubleshooting
- **Database Errors:** If you encounter database-related errors, double-check the database settings in the `settings.py` file to ensure they are correct.
- **Server Errors:** In case of server errors, check the server logs for detailed error messages and stack traces to diagnose the issue.
- **Documentation:** Refer to the Django documentation for guidance on troubleshooting common issues or seeking assistance online through forums and communities.
