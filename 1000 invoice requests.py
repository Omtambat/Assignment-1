import queue
import threading
import time
from datetime import datetime

invoice_queue = queue.Queue()


def generate_invoices():
    """Generate 1000 invoice requests."""
    for invoice_id in range(1, 1001):
        invoice_queue.put(invoice_id)

    print("1000 invoice requests added to queue.")


def process_invoice():
    while True:
        try:
            invoice_id = invoice_queue.get(timeout=2)
        except queue.Empty:
            break

        try:
            print(f"Processing Invoice {invoice_id}")

            # 1. Validate invoice data
            # 2. Calculate amount/tax
            # 3. Generate invoice
            # 4. Save to database
            # 5. Send notification

            time.sleep(0.01)

            print(f"Invoice {invoice_id} completed.")

        except Exception as error:
            print(f"Invoice {invoice_id} failed: {error}")

        finally:
            invoice_queue.task_done()


def main():
    # Triggered once every day at the fixed time
    generate_invoices()

    workers = []

    # Multiple workers process invoices concurrently
    for i in range(10):
        worker = threading.Thread(target=process_invoice)
        worker.start()
        workers.append(worker)

    invoice_queue.join()

    for worker in workers:
        worker.join()

    print("All invoice requests processed.")


if __name__ == "__main__":
    main()