
import os
import pprint
import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from invoke import task

from src.data_manager import DataManager



## Running App
@task(default=True)
def run_app(context):
    python_path = os.pathsep.join(["src"])
    command = f"PYTHONPATH={python_path} streamlit run src/view_main.py"
    context.run(command, echo=True)



## Tests
# @task
# def run_tests(context):
#     """
#     :summary: This task runs the small unittests

#     """
#     python_path = os.pathsep.join(["tests", "src"])
#     command = f"PYTHONPATH={python_path} python3 -m unittest test_main -v --failfast -b"
#     context.run(command, echo=True)

@task
def run_tests(context, var):
    print(var)



## Setup
@task
def setup_db(context):
    try:
        DataManager().create_table()
        default_products = [
            ('hard hat', '13.99', '10.00'),
            ('drill kit', '92.00','30.00'),
            ('gloves', '19.00','5.00')
        ]
        DataManager().add_products(default_products)
    except Exception as e:
        print(f"DB CREATE ERROR: {e}")

@task
def get_prods(context):
    try:
        prods = DataManager().get_products()
        print(prods)
    except Exception as e:
        print(f"DB QUERY ERROR: {e}")

@task
def add_item(context):
    try:
        new_prods = [
            ('wrench', '33.99', '13.00')
        ]
        DataManager().add_products(new_prods)
    except Exception as e:
        print(f"DB UPDATE ERROR: {e}")

@task
def update_item(context):
    try:
        new_prods = [
            ('wrench', '33.99', '13.00')
        ]
        DataManager().add_products(new_prods)
    except Exception as e:
        print(f"DB UPDATE ERROR: {e}")

@task
def delete_item(context):
    try:
        new_prods = [
            ('wrench', '33.99', '13.00')
        ]
        DataManager().add_products(new_prods)
    except Exception as e:
        print(f"DB UPDATE ERROR: {e}")

## Documents
@task
def run_docs(context):
    """
    :summary: This allows the user to start the MKDocs server and use the app's documentation.

    """
    python_path = os.pathsep.join(["docs", "src"])
    command = f"PYTHONPATH={python_path} mkdocs serve"
    context.run(command, echo=True)



