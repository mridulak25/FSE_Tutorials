from decimal import Decimal

from loguru import logger

from transactions import Transaction, Category, calculate_financial_summary
from database import get_session
from sqlalchemy import select




def main():
    logger.add("logs/app.log", rotation="1 MB")
    # Initialize database and create tables
    # Get a session
    session = get_session()

    try:
        # Ensure transaction table exists by querying it
        session.query(Transaction).first()

        # Query all transactions from the database
        all_transactions = session.query(Transaction).all()

        # Calculate and display summary
        summary = calculate_financial_summary(all_transactions)
        print("Financial Summary:")
        for key, value in summary.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    except Exception as e:
        logger.error(
            f"You may need to seed the database first, run 'python seed.py' and try again.\n\n"
        )
        raise e

    finally:
        session.close()
        # TODO: Once you have added the Entertainment category and sample  expenses, uncomment the lines below to display them!
        # display_transactions_by_category("Job")
        # display_transactions_by_category("Entertainment")


# TODO: Add the entertainment category, if it does not already exist
# NOTE: This means checking if a category with that name exists first
def add_entertainment_category():
    session = get_session()
    try:
        #Check if the Entertainment category already exists
        entertainment_category = session.query(Category).filter_by(name="Entertainment").first()
        if entertainment_category:
            return  # Category already exists, no need to add
        if not entertainment_category:
            # Create the Entertainment category if it doesn't exist
            entertainment_category = Category(name="Entertainment")
            session.add(entertainment_category)
            session.commit()
            logger.info("Entertainment category added.")
        else:
            logger.info("Entertainment category already exists.")

    finally:
        session.close()


# TODO: Add sample entertainment expenses
# NOTE: Fetch the Entertainment category first, then add two sample expenses linked to that category
def add_entertainment_expenses():
    session = get_session()
    try:
        # Fetch the Entertainment category
        entertainment_category = session.query(Category).filter_by(name="Entertainment").first()
        if not entertainment_category:
            logger.error("Entertainment category does not exist. Please add it first.")
            return

        # Add sample expenses linked to the Entertainment category
        expense1 = Transaction(
            date="2024-03-01",
            description="Concert Tickets",
            amount=Decimal(-300.00),
            category_ref=entertainment_category,
        )
        expense2 = Transaction(
            date="2024-03-15",
            description="Movie Night",
            amount=Decimal(-600.00),
            category_ref=entertainment_category,
        )
        session.add_all([expense1, expense2])
        session.commit()
        logger.info("Sample entertainment expenses added.")
    finally:
        session.close()


# TODO: Display all transactions for a given category name
def display_transactions_by_category(category_name: str):
    session = get_session()
    try:
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            logger.error(f"Category '{category_name}' does not exist.")
            return

        transactions = session.query(Transaction).filter_by(category_id=category.id).all()
        print(f"Transactions in category '{category_name}':")
        for transaction in transactions:
            print(f"{transaction.date} - {transaction.description}: {transaction.amount}")
    except Exception as e:
        logger.error(
            f"Error displaying transactions for category '{category_name}': {e}"
        )
    finally:
        session.close()


if __name__ == "__main__":
    main()
