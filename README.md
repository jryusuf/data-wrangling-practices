# SQL and Data Wrangling Portfolio

This repository showcases my SQL and data wrangling skills through various problems and katas.

## Purpose

The main goal of this repository is to demonstrate my ability to:

*   Write efficient and effective SQL queries.
*   Work with different datasets and database scenarios.
*   Document my approach and solutions clearly.

## Repository Structure

```
/
├── customer_purcases/       # Customer purchase analysis files
├── requirements.txt        # Python dependencies for the project
├── README.md               # Repository overview and usage instructions
└── venv/                   # Python virtual environment directory (ignored by Git)
```


## Examples

The repository includes SQL queries and Python scripts for data analysis. For example, the `customer_purcases/query.sql` file contains SQL queries to analyze customer purchase data.

**Note**: Running SQL queries requires a local PostgreSQL setup.

To explore SQL examples, you can refer to the `customer_purcases/query.sql` file. This file contains SQL queries designed for PostgreSQL.

## How to Use

### PostgreSQL Setup

To run the SQL queries, you need to have PostgreSQL installed and set up locally. You can then use a tool like `psql` (PostgreSQL command-line interface) to execute the queries.

### Running SQL Queries with psql

1.  **Navigate** to the directory containing the SQL files, e.g., `customer_purcases/`.
2.  **Connect** to your PostgreSQL database using `psql`. You might need to adjust the connection command based on your local setup:

    ```bash
    psql -d your_database_name -U your_username
    ```

    Replace `your_database_name` with the name of your PostgreSQL database and `your_username` with your PostgreSQL username.

3.  **Execute** the SQL queries using `psql`. For example, to run the queries in `query.sql`, you can use:

    ```bash
    psql -d your_database_name -U your_username -f query.sql
    ```

### Python Scripts

Before running the Python scripts, it is recommended to create a virtual environment to manage dependencies.

#### Create a virtual environment

Navigate to the project directory in your terminal and run:

```bash
python -m venv venv
```

#### Activate the virtual environment

*   **On Linux/macOS**:

    ```bash
    source venv/bin/activate
    ```

*   **On Windows**:

    ```bash
    venv\\Scripts\\activate
    ```

#### Install dependencies

Ensure you have the required Python libraries installed as listed in `requirements.txt`. You can install them using pip:

```bash
pip install -r requirements.txt
```

#### Run Python scripts

To run the Python scripts, navigate to the `customer_purcases/` directory in your terminal and execute the scripts using Python. For example, to run `main.py`, use the command:

```bash
python customer_purcases/main.py
```
