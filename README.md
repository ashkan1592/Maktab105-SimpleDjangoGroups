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



