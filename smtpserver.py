from aiosmtpd.controller import Controller

class CustomHandler:
    async def handle_DATA(self, server, session, envelope):
        print(f"Message from {envelope.mail_from}")
        print(f"Message to {envelope.rcpt_tos}")
        print(f"Message data:\n{envelope.content.decode('utf8', errors='replace')}")
        return '250 OK'

if __name__ == "__main__":
    handler = CustomHandler()
    controller = Controller(handler, hostname="localhost", port=25)
    print("Fake SMTP server running on localhost:25")
    controller.start()
    input("Press Enter to stop the server.\n")
    controller.stop()
