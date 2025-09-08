# Simple DB setup Template

***

#### Setting up your environment
The below steps will help walk you through what needs to be done to get your environment set up in order to run the application
1. Create your Python Virtual Environment
2. Start your Virtual Environment
3. Upgrade pip
4. Install Requirements
5. Open `tasks.py` file
6. Run the command `invoke setup-db` to setup your database, the products table and add default products

#### Running the application
Once your environment has been set up, you can now run the below commands to navigate throughout the application using the command line.  In most cases, running the application will be what the user will need to use.
- To run the application: `invoke run-app`
- To run the unit tests: `invoke run-tests`
- To open the documentation: `invoke run-docs`

***

#### Other CLI Invoke commands
These can be used to test the backend and check what is currently in the database table.
- Get a list of products: `invoke get-prods`
- To add a product: `invoke add-prod`
  - A sample product is setup within the automation since it currently does not take user input