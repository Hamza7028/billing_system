import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class TajHotel:

    def __init__(self, root):

        self.root = root
        self.root.title("Taj Hotel - Management System")
        self.root.geometry("1280x720")
        self.root.minsize(1100, 650)

        self.colors = {
            "main_bg": "#F4F1EA",
            "header_bg": "#1F2937",
            "left_bg": "#D97706",
            "middle_bg": "#374151",
            "right_bg": "#E5E7EB",
            "bottom_bg": "#111827",
            "button_bg": "#F59E0B",
            "button_fg": "#111827",
            "white": "#FFFFFF",
            "text": "#111827",
            "green": "#16A34A",
            "red": "#DC2626",
            "blue": "#2563EB",
            "purple": "#7C3AED"
        }

        self.root.configure(
            bg=self.colors["main_bg"]
        )

        # -----------------------------
        # Food Prices
        # -----------------------------

        self.prices = {
            "Drink": 700,
            "Burger King": 250,
            "Cherry": 99,
            "Nacho Fries": 300,
            "Pizza": 1200,
            "Biscuits": 120,
            "Roll": 220,
            "Tea": 350
        }

        self.entries = {}

        # -----------------------------
        # Output Variables
        # -----------------------------

        self.output_vars = {
            "Order Number": tk.StringVar(),
            "Cost": tk.StringVar(value="0.00"),
            "Tax": tk.StringVar(value="0.00"),
            "Sub Total": tk.StringVar(value="0.00"),
            "Total": tk.StringVar(value="0.00")
        }

        # -----------------------------
        # Order System
        # -----------------------------

        self.order_number = 1001

        self.order_history = []

        self.history_index = -1

        self.order_completed = False

        # -----------------------------
        # Create GUI
        # -----------------------------

        self.setup_styles()

        self.create_menu()

        self.create_header()

        self.create_order_section()

        self.create_calculator()

        self.create_bottom_buttons()

        self.update_clock()

        self.output_vars["Order Number"].set(
            str(self.order_number)
        )

    # =========================================================
    # STYLING
    # =========================================================

    def setup_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Treeview",
            font=("Arial", 11),
            rowheight=30
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 11, "bold")
        )

    # =========================================================
    # MENU BAR
    # =========================================================

    def create_menu(self):

        menu_bar = tk.Menu(self.root)

        # -----------------------------
        # File Menu
        # -----------------------------

        file_menu = tk.Menu(
            menu_bar,
            tearoff=0
        )

        file_menu.add_command(
            label="New Order",
            command=self.new_order
        )

        file_menu.add_command(
            label="Previous Order",
            command=self.previous_order
        )

        file_menu.add_command(
            label="Order History",
            command=self.show_order_history
        )

        file_menu.add_command(
            label="Price List",
            command=self.show_price_list
        )

        file_menu.add_separator()

        file_menu.add_command(
            label="Exit",
            command=self.quit_app
        )

        menu_bar.add_cascade(
            label="File",
            menu=file_menu
        )

        # -----------------------------
        # Order Menu
        # -----------------------------

        order_menu = tk.Menu(
            menu_bar,
            tearoff=0
        )

        order_menu.add_command(
            label="Calculate Price",
            command=self.calculate_price
        )

        order_menu.add_command(
            label="Calculate Total",
            command=self.calculate_total
        )

        order_menu.add_separator()

        order_menu.add_command(
            label="Next Order",
            command=self.new_order
        )

        order_menu.add_command(
            label="Previous Order",
            command=self.previous_order
        )

        order_menu.add_separator()

        order_menu.add_command(
            label="Reset Order",
            command=self.reset_order
        )

        menu_bar.add_cascade(
            label="Order",
            menu=order_menu
        )

        # -----------------------------
        # Calculator Menu
        # -----------------------------

        calculator_menu = tk.Menu(
            menu_bar,
            tearoff=0
        )

        calculator_menu.add_command(
            label="Clear Calculator",
            command=self.clear_calculator
        )

        calculator_menu.add_command(
            label="Focus Calculator",
            command=self.focus_calculator
        )

        menu_bar.add_cascade(
            label="Calculator",
            menu=calculator_menu
        )

        # -----------------------------
        # Help Menu
        # -----------------------------

        help_menu = tk.Menu(
            menu_bar,
            tearoff=0
        )

        help_menu.add_command(
            label="About",
            command=self.show_about
        )

        menu_bar.add_cascade(
            label="Help",
            menu=help_menu
        )

        self.root.config(
            menu=menu_bar
        )

    # =========================================================
    # HEADER
    # =========================================================

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg=self.colors["header_bg"],
            height=100
        )

        header.pack(
            fill="x",
            padx=15,
            pady=(10, 5)
        )

        header.pack_propagate(False)

        # -----------------------------
        # Hotel Title
        # -----------------------------

        title = tk.Label(
            header,
            text="TAJ HOTEL",
            font=("Arial", 28, "bold"),
            fg="#F59E0B",
            bg=self.colors["header_bg"]
        )

        title.pack(
            pady=(8, 0)
        )

        subtitle = tk.Label(
            header,
            text="Management & Billing System",
            font=("Arial", 13, "bold"),
            fg="#FFFFFF",
            bg=self.colors["header_bg"]
        )

        subtitle.pack()

        # -----------------------------
        # Digital Clock
        # -----------------------------

        self.clock_label = tk.Label(
            header,
            text="00:00:00",
            font=("Consolas", 22, "bold"),
            fg="#F59E0B",
            bg="#000000",
            relief="sunken",
            bd=4,
            padx=8,
            pady=3
        )

        self.clock_label.place(
            relx=0.90,
            rely=0.5,
            anchor="center"
        )

    # =========================================================
    # DIGITAL CLOCK
    # =========================================================

    def update_clock(self):

        current_time = datetime.now().strftime(
            "%H:%M:%S"
        )

        self.clock_label.config(
            text=current_time
        )

        self.root.after(
            1000,
            self.update_clock
        )

    # =========================================================
    # ORDER SECTION
    # =========================================================

    def create_order_section(self):

        main = tk.Frame(
            self.root,
            bg=self.colors["main_bg"]
        )

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=8
        )

        # =====================================================
        # LEFT FOOD ITEM FRAME
        # =====================================================

        item_frame = tk.LabelFrame(
            main,
            text=" FOOD ITEMS ",
            font=("Arial", 12, "bold"),
            fg="#FFFFFF",
            bg=self.colors["left_bg"],
            bd=5,
            relief="ridge",
            width=350
        )

        item_frame.pack(
            side="left",
            fill="y",
            padx=(0, 10)
        )

        item_frame.pack_propagate(False)

        for row, item in enumerate(self.prices):

            label = tk.Label(
                item_frame,
                text=item,
                font=("Arial", 11, "bold"),
                fg="#FFFFFF",
                bg=self.colors["left_bg"],
                anchor="w"
            )

            label.grid(
                row=row,
                column=0,
                padx=10,
                pady=8,
                sticky="w"
            )

            entry = tk.Entry(
                item_frame,
                font=("Arial", 12),
                width=10,
                justify="center",
                relief="sunken",
                bd=2
            )

            entry.grid(
                row=row,
                column=1,
                padx=10,
                pady=8
            )

            self.entries[item] = entry

        # =====================================================
        # MIDDLE BILL DETAILS FRAME
        # =====================================================

        calc_frame = tk.LabelFrame(
            main,
            text=" BILL DETAILS ",
            font=("Arial", 12, "bold"),
            fg="#FFFFFF",
            bg=self.colors["middle_bg"],
            bd=5,
            relief="ridge",
            width=360
        )

        calc_frame.pack(
            side="left",
            fill="y",
            padx=(0, 10)
        )

        calc_frame.pack_propagate(False)

        output_names = [
            "Order Number",
            "Cost",
            "Tax",
            "Sub Total",
            "Total"
        ]

        for row, name in enumerate(output_names):

            label = tk.Label(
                calc_frame,
                text=name,
                font=("Arial", 11, "bold"),
                fg="#FFFFFF",
                bg=self.colors["middle_bg"],
                anchor="w"
            )

            label.grid(
                row=row,
                column=0,
                padx=12,
                pady=12,
                sticky="w"
            )

            value_label = tk.Label(
                calc_frame,
                textvariable=self.output_vars[name],
                font=("Arial", 12, "bold"),
                fg="#111827",
                bg="#FFFFFF",
                width=14,
                anchor="e",
                relief="sunken",
                bd=2
            )

            value_label.grid(
                row=row,
                column=1,
                padx=12,
                pady=12
            )

        # =====================================================
        # RIGHT ORDER SUMMARY
        # =====================================================

        right_frame = tk.Frame(
            main,
            bg=self.colors["right_bg"]
        )

        right_frame.pack(
            side="left",
            fill="both",
            expand=True
        )

        notes_title = tk.Label(
            right_frame,
            text="ORDER SUMMARY",
            font=("Arial", 14, "bold"),
            fg="#FFFFFF",
            bg=self.colors["blue"]
        )

        notes_title.pack(
            fill="x"
        )

        self.notes = tk.Text(
            right_frame,
            font=("Arial", 11),
            bg="#FFFFFF",
            fg="#111827",
            relief="sunken",
            bd=4
        )

        self.notes.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
        )

        self.notes.insert(
            "1.0",
            "Enter food quantities and calculate the order."
        )

    # =========================================================
    # CALCULATOR
    # =========================================================

    def create_calculator(self):

        calculator_frame = tk.Frame(
            self.root,
            bg="#D1D5DB",
            bd=3,
            relief="ridge"
        )

        calculator_frame.place(
            relx=0.75,
            rely=0.43,
            relwidth=0.20,
            relheight=0.36
        )

        self.calculator_display = tk.Entry(
            calculator_frame,
            font=("Consolas", 16, "bold"),
            justify="right",
            bd=4,
            relief="sunken"
        )

        self.calculator_display.pack(
            fill="x",
            padx=7,
            pady=7
        )

        buttons = [
            ("1", 0, 0),
            ("2", 0, 1),
            ("3", 0, 2),
            ("+", 0, 3),
            ("4", 1, 0),
            ("5", 1, 1),
            ("6", 1, 2),
            ("-", 1, 3),
            ("7", 2, 0),
            ("8", 2, 1),
            ("9", 2, 2),
            ("*", 2, 3),
            ("C", 3, 0),
            ("0", 3, 1),
            ("=", 3, 2),
            ("/", 3, 3)
        ]

        button_grid = tk.Frame(
            calculator_frame,
            bg="#D1D5DB"
        )

        button_grid.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=2
        )

        for text, row, col in buttons:

            button = tk.Button(
                button_grid,
                text=text,
                font=("Arial", 12, "bold"),
                command=lambda value=text:
                self.calculator_click(value),
                relief="raised",
                bd=3
            )

            button.grid(
                row=row,
                column=col,
                sticky="nsew",
                padx=2,
                pady=2
            )

        for i in range(4):

            button_grid.grid_columnconfigure(
                i,
                weight=1
            )

            button_grid.grid_rowconfigure(
                i,
                weight=1
            )

        clear_button = tk.Button(
            calculator_frame,
            text="Clear",
            font=("Arial", 10, "bold"),
            bg="#DC2626",
            fg="#FFFFFF",
            command=self.clear_calculator,
            relief="raised",
            bd=3
        )

        clear_button.pack(
            pady=5
        )

    # =========================================================
    # CALCULATOR FUNCTION
    # =========================================================

    def calculator_click(self, value):

        if value == "C":

            self.clear_calculator()

        elif value == "=":

            expression = (
                self.calculator_display
                .get()
                .strip()
            )

            if not expression:

                return

            try:

                allowed = set(
                    "0123456789+-*/.() "
                )

                if any(
                    char not in allowed
                    for char in expression
                ):

                    raise ValueError

                result = eval(
                    expression,
                    {"__builtins__": None},
                    {}
                )

                if (
                    isinstance(result, float)
                    and result.is_integer()
                ):

                    result = int(result)

                self.calculator_display.delete(
                    0,
                    tk.END
                )

                self.calculator_display.insert(
                    0,
                    str(result)
                )

            except Exception:

                messagebox.showerror(
                    "Calculator Error",
                    "Invalid mathematical expression."
                )

        else:

            self.calculator_display.insert(
                tk.END,
                value
            )

    # =========================================================
    # CLEAR CALCULATOR
    # =========================================================

    def clear_calculator(self):

        self.calculator_display.delete(
            0,
            tk.END
        )

    # =========================================================
    # FOCUS CALCULATOR
    # =========================================================

    def focus_calculator(self):

        self.calculator_display.focus_set()

    # =========================================================
    # GET QUANTITIES
    # =========================================================

    def get_quantities(self):

        quantities = {}

        for item, entry in self.entries.items():

            text = entry.get().strip()

            if text == "":

                quantities[item] = 0

                continue

            try:

                quantity = int(text)

                if quantity < 0:

                    raise ValueError

                quantities[item] = quantity

            except ValueError:

                messagebox.showerror(
                    "Invalid Quantity",
                    f"Please enter a valid whole number for {item}."
                )

                entry.focus_set()

                return None

        return quantities

    # =========================================================
    # CALCULATE COST
    # =========================================================

    def calculate_cost(self):

        quantities = self.get_quantities()

        if quantities is None:

            return None

        cost = sum(
            self.prices[item] * quantities[item]
            for item in self.prices
        )

        return cost, quantities

    # =========================================================
    # CALCULATE PRICE
    # =========================================================

    def calculate_price(self):

        result = self.calculate_cost()

        if result is None:

            return

        cost, quantities = result

        self.output_vars["Order Number"].set(
            str(self.order_number)
        )

        self.output_vars["Cost"].set(
            f"{cost:.2f}"
        )

        # Tax = 5%

        tax = cost * 0.05

        subtotal = cost

        total = subtotal + tax

        self.output_vars["Tax"].set(
            f"{tax:.2f}"
        )

        self.output_vars["Sub Total"].set(
            f"{subtotal:.2f}"
        )

        self.output_vars["Total"].set(
            f"{total:.2f}"
        )

        self.show_order_summary(
            quantities,
            cost,
            tax,
            total
        )

    # =========================================================
    # CALCULATE TOTAL
    # =========================================================

    def calculate_total(self):

        result = self.calculate_cost()

        if result is None:

            return

        cost, quantities = result

        tax = cost * 0.05

        subtotal = cost

        total = subtotal + tax

        self.output_vars["Order Number"].set(
            str(self.order_number)
        )

        self.output_vars["Cost"].set(
            f"{cost:.2f}"
        )

        self.output_vars["Tax"].set(
            f"{tax:.2f}"
        )

        self.output_vars["Sub Total"].set(
            f"{subtotal:.2f}"
        )

        self.output_vars["Total"].set(
            f"{total:.2f}"
        )

        self.show_order_summary(
            quantities,
            cost,
            tax,
            total
        )

        self.order_completed = True

        self.save_current_order()

    # =========================================================
    # ORDER SUMMARY
    # =========================================================

    def show_order_summary(
        self,
        quantities,
        cost,
        tax,
        total
    ):

        self.notes.delete(
            "1.0",
            tk.END
        )

        self.notes.insert(
            "1.0",
            "ORDER SUMMARY\n"
        )

        self.notes.insert(
            "end",
            "=" * 35 + "\n"
        )

        self.notes.insert(
            "end",
            f"Order Number: {self.order_number}\n\n"
        )

        for item, quantity in quantities.items():

            if quantity > 0:

                amount = (
                    quantity *
                    self.prices[item]
                )

                self.notes.insert(
                    "end",
                    f"{item}: {quantity} x ₹{self.prices[item]} = ₹{amount}\n"
                )

        self.notes.insert(
            "end",
            "\n"
        )

        self.notes.insert(
            "end",
            "-" * 35 + "\n"
        )

        self.notes.insert(
            "end",
            f"Cost: ₹{cost:.2f}\n"
        )

        self.notes.insert(
            "end",
            f"Tax: ₹{tax:.2f}\n"
        )

        self.notes.insert(
            "end",
            f"Sub Total: ₹{cost:.2f}\n"
        )

        self.notes.insert(
            "end",
            f"TOTAL: ₹{total:.2f}\n"
        )

        self.notes.insert(
            "end",
            "-" * 35 + "\n"
        )

        self.notes.insert(
            "end",
            "Thank you for visiting Taj Hotel!"
        )

    # =========================================================
    # SAVE CURRENT ORDER
    # =========================================================

    def save_current_order(self):

        result = self.calculate_cost()

        if result is None:

            return False

        cost, quantities = result

        has_items = any(
            quantity > 0
            for quantity in quantities.values()
        )

        if not has_items:

            return False

        tax = cost * 0.05

        total = cost + tax

        order_data = {
            "order_number": self.order_number,
            "quantities": quantities.copy(),
            "cost": cost,
            "tax": tax,
            "subtotal": cost,
            "total": total
        }

        # Avoid duplicate history

        for order in self.order_history:

            if (
                order["order_number"]
                == self.order_number
            ):

                return True

        self.order_history.append(
            order_data
        )

        return True

    # =========================================================
    # NEXT ORDER
    # =========================================================

    def new_order(self):

        result = self.calculate_cost()

        if result is not None:

            cost, quantities = result

            has_items = any(
                quantity > 0
                for quantity in quantities.values()
            )

            if has_items:

                answer = messagebox.askyesno(
                    "Next Order",
                    "Do you want to save the current order and start a new order?"
                )

                if not answer:

                    return

                self.save_current_order()

        # Increase order number

        self.order_number += 1

        # Clear current order

        self.clear_order_screen()

        self.order_completed = False

        self.output_vars["Order Number"].set(
            str(self.order_number)
        )

        self.history_index = -1

    # =========================================================
    # CLEAR ORDER SCREEN
    # =========================================================

    def clear_order_screen(self):

        for entry in self.entries.values():

            entry.delete(
                0,
                tk.END
            )

        self.output_vars["Cost"].set(
            "0.00"
        )

        self.output_vars["Tax"].set(
            "0.00"
        )

        self.output_vars["Sub Total"].set(
            "0.00"
        )

        self.output_vars["Total"].set(
            "0.00"
        )

        self.notes.delete(
            "1.0",
            tk.END
        )

        self.notes.insert(
            "1.0",
            "Enter food quantities and calculate the order."
        )

        self.clear_calculator()

    # =========================================================
    # RESET ORDER
    # =========================================================

    def reset_order(self):

        answer = messagebox.askyesno(
            "Reset Order",
            "Are you sure you want to reset the current order?"
        )

        if not answer:

            return

        self.clear_order_screen()

        self.output_vars["Order Number"].set(
            str(self.order_number)
        )

        self.order_completed = False

    # =========================================================
    # PREVIOUS ORDER
    # =========================================================

    def previous_order(self):

        if not self.order_history:

            messagebox.showinfo(
                "Previous Order",
                "No previous orders are available."
            )

            return

        if self.history_index == -1:

            self.history_index = (
                len(self.order_history) - 1
            )

        else:

            self.history_index -= 1

        if self.history_index < 0:

            self.history_index = 0

            messagebox.showinfo(
                "Previous Order",
                "This is the oldest saved order."
            )

        order = self.order_history[
            self.history_index
        ]

        self.load_order(
            order
        )

    # =========================================================
    # LOAD PREVIOUS ORDER
    # =========================================================

    def load_order(self, order):

        for entry in self.entries.values():

            entry.delete(
                0,
                tk.END
            )

        for item, quantity in order[
            "quantities"
        ].items():

            if quantity > 0:

                self.entries[item].insert(
                    0,
                    str(quantity)
                )

        self.output_vars["Order Number"].set(
            str(order["order_number"])
        )

        self.output_vars["Cost"].set(
            f"{order['cost']:.2f}"
        )

        self.output_vars["Tax"].set(
            f"{order['tax']:.2f}"
        )

        self.output_vars["Sub Total"].set(
            f"{order['subtotal']:.2f}"
        )

        self.output_vars["Total"].set(
            f"{order['total']:.2f}"
        )

        self.notes.delete(
            "1.0",
            tk.END
        )

        self.notes.insert(
            "1.0",
            "PREVIOUS ORDER\n"
        )

        self.notes.insert(
            "end",
            "=" * 35 + "\n"
        )

        self.notes.insert(
            "end",
            f"Order Number: {order['order_number']}\n\n"
        )

        for item, quantity in order[
            "quantities"
        ].items():

            if quantity > 0:

                amount = (
                    quantity *
                    self.prices[item]
                )

                self.notes.insert(
                    "end",
                    f"{item}: {quantity} x ₹{self.prices[item]} = ₹{amount}\n"
                )

        self.notes.insert(
            "end",
            "\n"
        )

        self.notes.insert(
            "end",
            "-" * 35 + "\n"
        )

        self.notes.insert(
            "end",
            f"Cost: ₹{order['cost']:.2f}\n"
        )

        self.notes.insert(
            "end",
            f"Tax: ₹{order['tax']:.2f}\n"
        )

        self.notes.insert(
            "end",
            f"Total: ₹{order['total']:.2f}\n"
        )

        self.notes.insert(
            "end",
            "\nThis is a previous order."
        )

    # =========================================================
    # ORDER HISTORY WINDOW
    # =========================================================

    def show_order_history(self):

        history_window = tk.Toplevel(
            self.root
        )

        history_window.title(
            "Order History"
        )

        history_window.geometry(
            "700x500"
        )

        history_window.configure(
            bg=self.colors["main_bg"]
        )

        title = tk.Label(
            history_window,
            text="ORDER HISTORY",
            font=("Arial", 20, "bold"),
            fg="#FFFFFF",
            bg=self.colors["header_bg"]
        )

        title.pack(
            fill="x",
            pady=(0, 15)
        )

        if not self.order_history:

            message = tk.Label(
                history_window,
                text="No orders have been completed yet.",
                font=("Arial", 13, "bold"),
                bg=self.colors["main_bg"]
            )

            message.pack(
                pady=50
            )

            return

        tree = ttk.Treeview(
            history_window,
            columns=(
                "order",
                "cost",
                "tax",
                "total"
            ),
            show="headings"
        )

        tree.heading(
            "order",
            text="ORDER NO."
        )

        tree.heading(
            "cost",
            text="COST"
        )

        tree.heading(
            "tax",
            text="TAX"
        )

        tree.heading(
            "total",
            text="TOTAL"
        )

        tree.column(
            "order",
            width=120,
            anchor="center"
        )

        tree.column(
            "cost",
            width=150,
            anchor="center"
        )

        tree.column(
            "tax",
            width=150,
            anchor="center"
        )

        tree.column(
            "total",
            width=150,
            anchor="center"
        )

        for order in self.order_history:

            tree.insert(
                "",
                tk.END,
                values=(
                    order["order_number"],
                    f"₹ {order['cost']:.2f}",
                    f"₹ {order['tax']:.2f}",
                    f"₹ {order['total']:.2f}"
                )
            )

        tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        close_button = tk.Button(
            history_window,
            text="Close",
            font=("Arial", 11, "bold"),
            bg=self.colors["red"],
            fg="#FFFFFF",
            width=12,
            command=history_window.destroy
        )

        close_button.pack(
            pady=15
        )

    # =========================================================
    # PRICE LIST
    # =========================================================

    def show_price_list(self):

        price_window = tk.Toplevel(
            self.root
        )

        price_window.title(
            "Price List"
        )

        price_window.geometry(
            "450x500"
        )

        price_window.configure(
            bg=self.colors["main_bg"]
        )

        title = tk.Label(
            price_window,
            text="PRICE LIST",
            font=("Arial", 20, "bold"),
            fg="#FFFFFF",
            bg=self.colors["header_bg"]
        )

        title.pack(
            fill="x",
            pady=(0, 15)
        )

        tree = ttk.Treeview(
            price_window,
            columns=(
                "item",
                "price"
            ),
            show="headings",
            height=12
        )

        tree.heading(
            "item",
            text="ITEM"
        )

        tree.heading(
            "price",
            text="PRICE"
        )

        tree.column(
            "item",
            width=260,
            anchor="center"
        )

        tree.column(
            "price",
            width=120,
            anchor="center"
        )

        for item, price in self.prices.items():

            tree.insert(
                "",
                tk.END,
                values=(
                    item,
                    f"₹ {price}"
                )
            )

        tree.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        close_button = tk.Button(
            price_window,
            text="Close",
            font=("Arial", 11, "bold"),
            bg=self.colors["red"],
            fg="#FFFFFF",
            width=10,
            command=price_window.destroy
        )

        close_button.pack(
            pady=15
        )

    # =========================================================
    # BOTTOM BUTTONS
    # =========================================================

    def create_bottom_buttons(self):

        bottom = tk.Frame(
            self.root,
            bg=self.colors["bottom_bg"],
            bd=5,
            relief="ridge"
        )

        bottom.pack(
            fill="x",
            padx=25,
            pady=(0, 12)
        )

        # -----------------------------
        # Price Button
        # -----------------------------

        price_button = tk.Button(
            bottom,
            text="Price",
            font=("Arial", 12, "bold"),
            bg=self.colors["button_bg"],
            fg=self.colors["button_fg"],
            width=9,
            command=self.calculate_price,
            relief="raised",
            bd=3
        )

        price_button.pack(
            side="left",
            padx=10,
            pady=8
        )

        # -----------------------------
        # Total Button
        # -----------------------------

        total_button = tk.Button(
            bottom,
            text="Total",
            font=("Arial", 12, "bold"),
            bg=self.colors["green"],
            fg="#FFFFFF",
            width=9,
            command=self.calculate_total,
            relief="raised",
            bd=3
        )

        total_button.pack(
            side="left",
            padx=10,
            pady=8
        )

        # -----------------------------
        # Previous Order Button
        # -----------------------------

        previous_button = tk.Button(
            bottom,
            text="Previous Order",
            font=("Arial", 12, "bold"),
            bg=self.colors["purple"],
            fg="#FFFFFF",
            width=15,
            command=self.previous_order,
            relief="raised",
            bd=3
        )

        previous_button.pack(
            side="left",
            padx=10,
            pady=8
        )

        # -----------------------------
        # Next Order Button
        # -----------------------------

        next_button = tk.Button(
            bottom,
            text="Next Order",
            font=("Arial", 12, "bold"),
            bg=self.colors["blue"],
            fg="#FFFFFF",
            width=12,
            command=self.new_order,
            relief="raised",
            bd=3
        )

        next_button.pack(
            side="left",
            padx=10,
            pady=8
        )

        # -----------------------------
        # History Button
        # -----------------------------

        history_button = tk.Button(
            bottom,
            text="History",
            font=("Arial", 12, "bold"),
            bg="#0891B2",
            fg="#FFFFFF",
            width=9,
            command=self.show_order_history,
            relief="raised",
            bd=3
        )

        history_button.pack(
            side="left",
            padx=10,
            pady=8
        )

        # -----------------------------
        # Reset Button
        # -----------------------------

        reset_button = tk.Button(
            bottom,
            text="Reset",
            font=("Arial", 12, "bold"),
            bg="#F97316",
            fg="#FFFFFF",
            width=9,
            command=self.reset_order,
            relief="raised",
            bd=3
        )

        reset_button.pack(
            side="left",
            padx=10,
            pady=8
        )

        # -----------------------------
        # Quit Button
        # -----------------------------

        quit_button = tk.Button(
            bottom,
            text="Quit",
            font=("Arial", 12, "bold"),
            bg=self.colors["red"],
            fg="#FFFFFF",
            width=9,
            command=self.quit_app,
            relief="raised",
            bd=3
        )

        quit_button.pack(
            side="left",
            padx=10,
            pady=8
        )

    # =========================================================
    # ABOUT
    # =========================================================

    def show_about(self):

        messagebox.showinfo(
            "About Taj Hotel",
            "Taj Hotel Management System\n\n"
            "Python Tkinter GUI Project\n\n"
            "Features:\n"
            "• Food quantity entry\n"
            "• Price calculation\n"
            "• 5% tax calculation\n"
            "• Total calculation\n"
            "• Next Order\n"
            "• Previous Order\n"
            "• Order History\n"
            "• Price List\n"
            "• Calculator\n"
            "• Digital Clock\n"
            "• No Service Charge"
        )

    # =========================================================
    # QUIT APPLICATION
    # =========================================================

    def quit_app(self):

        answer = messagebox.askyesno(
            "Quit",
            "Are you sure you want to close Taj Hotel?"
        )

        if answer:

            self.root.destroy()


# =============================================================
# PROGRAM START
# =============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = TajHotel(
        root
    )

    root.mainloop()