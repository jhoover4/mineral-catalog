# Mineral Catalog

This is the sixth and eighth project in the Treehouse Python tech degree.

Hosted on [Heroku](https://mineral-catalog-filter.herokuapp.com). To view locally clone the repo, download the 
requirements with ```pip install requirements.txt``` and run ```python manage.py runserver```.

## Description

As part of your job, you’ve been asked to build a website that displays information about various minerals. The home 
page of the site contains a list of all of the minerals in a database. Clicking on a mineral’s name opens a page that 
displays information about the mineral.

## User Stories

- As a user, I should be able to to filter minerals by first letter in mineral name, grouping, and category.
- As a user, I should be able to user the search bar to perform a full-text search of the app.
- As a user, I should be able to view a random mineral page by clicking a button.
- As a user, I should be able to seed a database with the minerals.json file.

## Completed Development Tasks

- Write a model to store the mineral data. Write a script that constructs a mineral model instance for each mineral in 
minerals.json and saves them to a SQLite database.
- Create a layout template for the app.
- Create a template and view to show the names of all the minerals.
- Create a mineral details template and view.
- Write unit tests to test that models, classes, and other functions are working correctly.
- Add css throughout the app to make changes match provided files.
- Queries to the database should be optimized and take no longer than 10ms to complete.
- Complete above user stories.