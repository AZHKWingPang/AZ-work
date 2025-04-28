# AZ-work

# Redshift Connection Utility

A Python utility for securely connecting to Amazon Redshift database.

## Features
- Secure database connection handling
- Environment-based configuration
- Error handling and logging

## Setup
1. Create a `.env` file with your Redshift credentials
2. Install required dependencies:
```bash
pip install sqlalchemy psycopg2-binary python-dotenv
```

## Security
- Credentials are stored in environment variables
- Sensitive files are excluded via .gitignore
- Using secure connection practices

## Usage
```python
from connect_redshift import connect_to_redshift

engine = connect_to_redshift()
if engine:
    # Use the connection
    pass
```

## Note
This is an internal tool. Do not share credentials or sensitive information.

## License
This project is licensed under the MIT License with additional restrictions - see the [LICENSE](LICENSE) file for details.
Internal AstraZeneca use only. Contains sensitive database connection information.
