from deployment.Record import Record


def main():
    print("Synchronizing data on the cloud...")
    Record().get_record()
    print("Sync succeeded!")
