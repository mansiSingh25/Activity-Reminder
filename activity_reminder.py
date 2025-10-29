from plyer import notification
from datetime import datetime, timezone, timedelta
from time import sleep

# Track if a reminder has been sent for each hour of the day
is_notification_sent = [0] * 24


def send_reminder(msg):
    """Send a desktop notification."""
    notification.notify(
        title="⏰ Urgent Reminder",
        message=msg,
        timeout=5  
    )
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Reminder sent: {msg}")


def schedule(date):
    """Check time and send appropriate reminders."""
    hour = date.hour

    # Lunch + Water Reminder
    if hour == 13 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("🍱 It's time for lunch and water!")

    # Snack Reminder
    elif hour == 16 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("🍪 It's time for snacks and water!")

    # Log-off Reminder
    elif hour == 18 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("💻 Time to log off from work!")

    # Study Reminder
    elif hour == 20 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("📚 Time to study!")

    # Water Reminders (Office hours)
    elif 9 <= hour < 18 and hour not in [13, 16] and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("💧 Drink some water!")


if __name__ == "__main__":
    print("🔔 Activity Reminder started... Press Ctrl+C to stop.\n")

    prev_date = datetime.now(timezone.utc).astimezone() - timedelta(days=1)

    while True:
        date = datetime.now(timezone.utc).astimezone()

        # Reset daily reminder flags
        if date.day != prev_date.day:
            is_notification_sent = [0] * 24
            prev_date = date

        schedule(date)
        sleep(60)  # Check every 1 minute
