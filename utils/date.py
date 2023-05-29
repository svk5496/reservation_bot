from datetime import datetime, timedelta


def get_future_date(days):
    # Get today's date
    today = datetime.now().date()

    # Calculate the future date
    future_date = today + timedelta(days=days)

    # Format the date as "YYYY-MM-DD"
    formatted_date = future_date.strftime("%Y-%m-%d")

    return formatted_date
