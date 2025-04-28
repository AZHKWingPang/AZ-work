from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import urllib.parse

def connect_to_redshift():
    """
    Connect to an Amazon Redshift database using SQLAlchemy and psycopg2.
    Replace the placeholder credentials with actual values.
    """
    # Placeholder credentials - replace with your actual Redshift details
    host = "az-edh-redshift-prod.ckupxdabfvk3.eu-west-1.redshift.amazonaws.com"
    port = "5439"  # Default Redshift port
    database = "im_rpt"
    user = "Prod readonly User"
    password = "HKazm@247"

    # URL encode the username and password to handle special characters
    encoded_user = urllib.parse.quote_plus(user)
    encoded_password = urllib.parse.quote_plus(password)

    # Construct the connection string
    connection_string = f"postgresql+psycopg2://{encoded_user}:{encoded_password}@{host}:{port}/{database}"

    try:
        # Create the SQLAlchemy engine
        engine = create_engine(connection_string)
        # Test the connection
        with engine.connect() as connection:
            print("Connection to Amazon Redshift was successful!")
        return engine
    except SQLAlchemyError as e:
        print(f"Error connecting to Amazon Redshift: {e}")
        return None
        