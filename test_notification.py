from winotify import Notification, audio

toast = Notification(
    app_id="com.mansi.activityreminder",
    title="Activity Reminder",
    msg="Your notification system is ready!",
    icon=r"C:\Windows\System32\Shell32.dll"
)
toast.set_audio(audio.Default, loop=False)
toast.show()
