# Player Combination Generator

This project selects optimal player combinations for defensive and offensive positions, maximizing the overall team performance.

## Features
- Uses MySQL to store and query data.
- Generates combinations considering defensive, offensive, and overall values.
- Sorts combinations to highlight the best options.

## Requirements
- Python 3.8+
- MySQL 8.0+
- Python libraries:
  - `mysql-connector-python`

## Installation
1. Clone this repository.
2. Set up the database:
   ```bash
   mysql -u root -p < database/schema.sql
   mysql -u root -p < database/seed.sql
