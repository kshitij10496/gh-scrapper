import sys
import subprocess


def notify(message):
    """ Notifies the logged in user with an update message using the notifer application based on the Operating System.

    For MacOS : terminal-notifier
        Linux : notify-send

    """
    title = "GitHub Notification"
    platform = sys.platform
    if platform == 'darwin':
        # test if terminal-notifier is present on the system or not
        status = subprocess.run(["which", "terminal-notifier"]).returncode
        if status == 0:
            notifier = "terminal-notifier"

        else:
            print("Kindly install terminal-notifier for MacOS.")
            return -1

    elif platform == 'linux':
        notifier = "notify-send"

    # look into other cases
    else:
        print("Your system is not supported yet.")
        return -1

    subprocess.run([notifier, "-title", "GitHub Notification", "-message",
                    message, "-timeout", 10])
    return 1
