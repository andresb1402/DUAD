import csv
from datetime import datetime
import FreeSimpleGUI as sg

from data import *
from models import FinanceManager, Transaction

DB_FILE = "transactions.json"
manager = FinanceManager()

categories_list = [
    "General",
    "Rims",
    "Photography",
    "Savings",
    "Food",
    "Supermarket",
    "Weekly House Expenses",
    "Gas",
    "Services",
    "CC Payment",
    "CC Partial Payment",
    "Others",
]

payment_methods = [
    "Cash",
    "Credit Card",
    "Transfer",
    "SINPE",
]

# Add categories
for cat in categories_list:
    manager.add_category(cat)

# Load existing JSON data
raw_data = json_file_reader(DB_FILE)
if isinstance(raw_data, list):
    for item in raw_data:
        try:
            t = Transaction(
                trans_type=item.get("trans_type"),
                category=item.get("category"),
                title=item.get("title"),
                amount=item.get("amount"),
                payment_method=item.get("payment_method"),
                date=item.get("date"),
            )
            manager.add_transaction(t)
        except Exception as e:
            print(f"Error loading transaction: {e}")


def get_table_data(transactions=None):
    if transactions is None:
        transactions = manager.get_transactions()
    return [
        [
            t.date,
            t.trans_type,
            t.category,
            t.title,
            f"₡{t.amount:,.2f}",
            t.payment_method,
        ]
        for t in transactions
    ]


def open_transactions_window():
    editing_transaction = None

    layout_transactions = [
        [sg.Text("Finance Tracker", font=("Helvetica", 16, "bold"))],
        # Transaction form
        [
            sg.Text("Type:"),
            sg.Radio("Income", "TYPE", key="-INCOME-", default=True),
            sg.Radio("Expense", "TYPE", key="-EXPENSE-"),
            sg.Radio("CC Payment", "TYPE", key="-CC-PAYMENT-"),
            sg.Radio("CC Partial Payment", "TYPE", key="-CC-PARTIAL-"),
        ],
        [
            sg.Text("Category:"),
            sg.Combo(
                categories_list,
                default_value=categories_list[0],
                key="-CATEGORY-",
                readonly=True,
            ),
        ],
        [sg.Text("Title:"), sg.InputText(key="-TITLE-")],
        [sg.Text("Amount (₡):"), sg.InputText(key="-AMOUNT-")],
        [
            sg.Text("Payment Method:"),
            sg.Combo(
                payment_methods,
                default_value=payment_methods[0],
                key="-PAYMENT-",
                readonly=True,
            ),
        ],
        [
            sg.Text("Date (DD/MM/YYYY):"),
            sg.InputText(key="-DATE-", size=(15, 1)),
            sg.CalendarButton(
                "Choose date",
                target="-DATE-",
                format="%d/%m/%Y",
                close_when_date_chosen=True,
            ),
        ],
        # Actions buttons
        [
            sg.Button("Save Transaction", key="-SAVE-"),
            sg.Button("Clear Form", key="-CLEAR-"),
            sg.Button("Back"),
        ],
        [sg.HorizontalSeparator()],
        # Search & Filter bar
        [
            sg.Text("Search:"),
            sg.InputText(key="-SEARCH-", enable_events=True, size=(25, 1)),
        ],
        [
            sg.Text("From:"),
            sg.InputText(key="-DATE-FROM-", size=(10, 1)),
            sg.CalendarButton(
                "From",
                target="-DATE-FROM-",
                format="%d/%m/%Y",
                close_when_date_chosen=True,
            ),
            sg.Text("To:"),
            sg.InputText(key="-DATE-TO-", size=(10, 1)),
            sg.CalendarButton(
                "To",
                target="-DATE-TO-",
                format="%d/%m/%Y",
                close_when_date_chosen=True,
            ),
            sg.Button("Filter Range", key="-FILTER-DATES-"),
            sg.Button("Clear Filters", key="-CLEAR-DATES-"),
        ],
        [
            sg.Table(
                values=get_table_data(),
                headings=[
                    "Date",
                    "Type",
                    "Category",
                    "Title",
                    "Amount",
                    "Payment Method",
                ],
                auto_size_columns=False,
                col_widths=[12, 12, 18, 22, 14, 12],
                display_row_numbers=False,
                justification="left",
                key="-TABLE-",
                num_rows=8,
                enable_events=True,
                select_mode=sg.TABLE_SELECT_MODE_BROWSE,
            )
        ],
        # Selected transaction buttons
        [
            sg.Button("Edit Selected", key="-EDIT-"),
            sg.Button("Delete Selected", key="-DELETE-"),
        ],
    ]

    trans_window = sg.Window(
        "Transactions Manager", layout_transactions, modal=True
    )

    def refresh_table(search_query="", date_from_str="", date_to_str=""):
        filtered = manager.get_transactions()

        # 1. Text Search Filter
        if search_query:
            q = search_query.lower()
            filtered = [
                t
                for t in filtered
                if q in t.title.lower()
                or q in t.category.lower()
                or q in t.trans_type.lower()
                or q in f"{t.amount:.2f}"
                or q in str(t.amount)
            ]

        # 2. Date Range Filter
        if date_from_str and date_to_str:
            try:
                d_start = datetime.strptime(date_from_str, "%d/%m/%Y")
                d_end = datetime.strptime(date_to_str, "%d/%m/%Y")

                if d_start > d_end:
                    sg.popup_error(
                        "End date must be greater than or equal to Start date."
                    )
                    return filtered

                temp_filtered = []
                for t in filtered:
                    try:
                        t_date = datetime.strptime(t.date, "%d/%m/%Y")
                        if d_start <= t_date <= d_end:
                            temp_filtered.append(t)
                    except ValueError:
                        continue

                filtered = temp_filtered

            except ValueError:
                sg.popup_error(
                    "Invalid date format. Please use DD/MM/YYYY."
                )
                return filtered

        trans_window["-TABLE-"].update(values=get_table_data(filtered))
        return filtered

    current_visible_transactions = manager.get_transactions()

    while True:
        event, values = trans_window.read()

        if event in (sg.WINDOW_CLOSED, "Back"):
            break

        # Real-time search
        if event == "-SEARCH-":
            current_visible_transactions = refresh_table(
                search_query=values["-SEARCH-"].strip(),
                date_from_str=values["-DATE-FROM-"].strip(),
                date_to_str=values["-DATE-TO-"].strip(),
            )

        if event == "-FILTER-DATES-":
            from_val = values["-DATE-FROM-"].strip()
            to_val = values["-DATE-TO-"].strip()

            if not from_val or not to_val:
                sg.popup_error("Please enter both Start Date and End Date.")
            else:
                current_visible_transactions = refresh_table(
                    search_query=values["-SEARCH-"].strip(),
                    date_from_str=from_val,
                    date_to_str=to_val,
                )

        if event == "-CLEAR-DATES-":
            trans_window["-DATE-FROM-"].update("")
            trans_window["-DATE-TO-"].update("")
            trans_window["-SEARCH-"].update("")
            current_visible_transactions = refresh_table(
                search_query="", date_from_str="", date_to_str=""
            )

        # Clear form
        if event == "-CLEAR-":
            editing_transaction = None
            trans_window["-TITLE-"].update("")
            trans_window["-AMOUNT-"].update("")
            trans_window["-DATE-"].update("")
            trans_window["-INCOME-"].update(True)
            trans_window["-CATEGORY-"].update(categories_list[0])
            trans_window["-PAYMENT-"].update(payment_methods[0])
            trans_window["-SAVE-"].update("Save Transaction")

        # Edit button
        if event == "-EDIT-":
            selected_rows = values["-TABLE-"]
            if not selected_rows:
                sg.popup_error(
                    "Please select a transaction from the table first."
                )
                continue

            row_idx = selected_rows[0]
            editing_transaction = current_visible_transactions[row_idx]

            # Load values into form
            trans_window["-TITLE-"].update(editing_transaction.title)
            trans_window["-AMOUNT-"].update(str(editing_transaction.amount))
            trans_window["-DATE-"].update(editing_transaction.date)
            trans_window["-CATEGORY-"].update(editing_transaction.category)
            trans_window["-PAYMENT-"].update(
                editing_transaction.payment_method
            )

            if editing_transaction.trans_type == "Income":
                trans_window["-INCOME-"].update(True)
            elif editing_transaction.trans_type == "Expense":
                trans_window["-EXPENSE-"].update(True)
            elif editing_transaction.trans_type == "CC Payment":
                trans_window["-CC-PAYMENT-"].update(True)
            else:
                trans_window["-CC-PARTIAL-"].update(True)

            trans_window["-SAVE-"].update("Update Transaction")

        # Delete selected
        if event == "-DELETE-":
            selected_rows = values["-TABLE-"]
            if not selected_rows:
                sg.popup_error("Please select a transaction to delete.")
                continue

            row_idx = selected_rows[0]
            target_trans = current_visible_transactions[row_idx]

            confirm = sg.popup_yes_no(
                f"Are you sure you want to delete '{target_trans.title}'?",
                title="Confirm Delete",
            )
            if confirm == "Yes":
                manager.get_transactions().remove(target_trans)
                save_to_file(
                    DB_FILE, [t.to_dict() for t in manager.get_transactions()]
                )

                if editing_transaction == target_trans:
                    editing_transaction = None
                    trans_window["-SAVE-"].update("Save Transaction")

                current_visible_transactions = refresh_table(
                    search_query=values["-SEARCH-"].strip(),
                    date_from_str=values["-DATE-FROM-"].strip(),
                    date_to_str=values["-DATE-TO-"].strip(),
                )
                sg.popup("Deleted", "Transaction removed successfully.")

        # Save/Update
        if event == "-SAVE-":
            if values["-INCOME-"]:
                trans_type = "Income"
            elif values["-EXPENSE-"]:
                trans_type = "Expense"
            elif values["-CC-PAYMENT-"]:
                trans_type = "CC Payment"
            else:
                trans_type = "CC Partial Payment"

            title = values["-TITLE-"].strip()
            category = values["-CATEGORY-"]
            amount_str = values["-AMOUNT-"].strip()
            payment_method = values["-PAYMENT-"]
            date_str = values["-DATE-"].strip()

            if not title or not amount_str or not date_str:
                sg.popup_error(
                    "Please fill in all required fields (Title, Amount, Date)."
                )
                continue

            try:
                amount = float(amount_str)
            except ValueError:
                sg.popup_error("Amount must be a valid number.")
                continue

            try:
                if editing_transaction is None:
                    new_trans = Transaction(
                        trans_type, category, title, amount, payment_method, date_str
                    )
                    manager.add_transaction(new_trans)
                else:
                    editing_transaction.set_date(date_str)
                    editing_transaction.trans_type = trans_type
                    editing_transaction.category = category
                    editing_transaction.title = title
                    editing_transaction.amount = amount
                    editing_transaction.payment_method = payment_method

                    editing_transaction = None
                    trans_window["-SAVE-"].update("Save Transaction")

            except ValueError as err:
                # Error if future date
                sg.popup_error(str(err))
                continue

            # Save to JSON
            data_to_save = [t.to_dict() for t in manager.get_transactions()]
            save_to_file(DB_FILE, data_to_save)

            # Refresh table with active filters
            current_visible_transactions = refresh_table(
                search_query=values["-SEARCH-"].strip(),
                date_from_str=values["-DATE-FROM-"].strip(),
                date_to_str=values["-DATE-TO-"].strip(),
            )

            # Clear inputs
            trans_window["-TITLE-"].update("")
            trans_window["-AMOUNT-"].update("")
            trans_window["-DATE-"].update("")

            sg.popup("Success", "Transaction saved successfully!")

    trans_window.close()


def open_metrics_window():
    current_metrics_data = []
    current_metrics_type = "Summary"

    layout_metrics = [
        [sg.Text("Metrics Viewer", font=("Helvetica", 16, "bold"))],
        # Date Filter Row
        [
            sg.Text("From:"),
            sg.InputText(key="-M-DATE-FROM-", size=(12, 1)),
            sg.CalendarButton(
                "From",
                target="-M-DATE-FROM-",
                format="%d/%m/%Y",
                close_when_date_chosen=True,
            ),
            sg.Text("To:"),
            sg.InputText(key="-M-DATE-TO-", size=(12, 1)),
            sg.CalendarButton(
                "To",
                target="-M-DATE-TO-",
                format="%d/%m/%Y",
                close_when_date_chosen=True,
            ),
        ],
        [sg.HorizontalSeparator()],
        # Metric Selector Buttons
        [
            sg.Button("Summary", key="-BTN-SUMMARY-"),
            sg.Button("Expenses by Category", key="-BTN-EXP-CAT-"),
            sg.Button("Incomes by Category", key="-BTN-INC-CAT-"),
        ],
        # Dynamic Table
        [
            sg.Table(
                values=[],
                headings=["Category", "Amount"],
                auto_size_columns=True,
                justification="left",
                key="-METRICS-TABLE-",
                num_rows=10,
                expand_x=True,
            )
        ],
        [
            sg.Button("Export to CSV", key="-EXPORT_CSV-"),
            sg.Button("Back"),
        ],
    ]

    metrics_window = sg.Window("Metrics Viewer", layout_metrics, modal=True)

    def export_table_to_csv(default_filename, headers, rows):
        if not rows:
            sg.popup_warning("No data to export.", title="Empty Table")
            return

        file_path = sg.popup_get_file(
            "Save report as...",
            save_as=True,
            default_extension=".csv",
            file_types=(("CSV File", "*.csv"), ("All files", "*.*")),
            default_path=f"{default_filename}.csv",
        )

        if file_path:
            try:
                with open(
                    file_path, mode="w", newline="", encoding="utf-8"
                ) as file:
                    writer = csv.writer(file)
                    if headers:
                        writer.writerow(headers)
                    writer.writerows(rows)

                sg.popup(
                    "File exported successfully",
                    f"Saved in:\n{file_path}",
                    title="Success!",
                )
            except Exception as e:
                sg.popup_error(
                    f"There was an error saving the file:\n{e}", title="Error"
                )

    while True:
        event, values = metrics_window.read()

        if event in (sg.WINDOW_CLOSED, "Back"):
            break

        d_from = values["-M-DATE-FROM-"].strip()
        d_to = values["-M-DATE-TO-"].strip()

        if event == "-BTN-SUMMARY-":
            current_metrics_type = "Summary"
            current_metrics_data = manager.get_summary_metrics(d_from, d_to)
            metrics_window["-METRICS-TABLE-"].update(
                values=current_metrics_data
            )

        if event == "-BTN-EXP-CAT-":
            current_metrics_type = "Expenses_by_Category"
            current_metrics_data = manager.get_expenses_by_category(
                d_from, d_to
            )
            metrics_window["-METRICS-TABLE-"].update(
                values=current_metrics_data
            )

        if event == "-BTN-INC-CAT-":
            current_metrics_type = "Incomes_by_Category"
            current_metrics_data = manager.get_income_by_category(
                d_from, d_to
            )
            metrics_window["-METRICS-TABLE-"].update(
                values=current_metrics_data
            )

        if event == "-EXPORT_CSV-":
            headers = ["Category", "Amount"]
            filename = f"{current_metrics_type.lower()}_report"
            export_table_to_csv(filename, headers, current_metrics_data)

    metrics_window.close()


# Layout and main menu loop
layout_menu = [
    [sg.Text("Finance System", font=("Helvetica", 16, "bold"))],
    [sg.Button("Transactions"), sg.Button("Metrics")],
    [sg.Button("Exit")],
]

main_window = sg.Window("Main Menu", layout_menu)

while True:
    event, values = main_window.read()

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    if event == "Transactions":
        open_transactions_window()

    if event == "Metrics":
        open_metrics_window()

main_window.close()