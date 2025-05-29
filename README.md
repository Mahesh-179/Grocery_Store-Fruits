# 🛒 Mahesh Lamsal Fruit Shop - Python Billing System

A terminal-based billing system for a fruit shop built using **Python**. The system allows users to view menus for fruits, juices, and cold drinks, purchase items by specifying quantity, and generates a detailed bill with timestamp and grand total.

---

## 🔧 Features

- 📦 Three categories: **Fruits**, **Juices**, and **Cold Drinks**
- 🧾 Real-time billing with **timestamped entries**
- 💰 Automatic price calculation based on quantity
- 📋 Neatly formatted **tabulated bill view** using `tabulate`
- 🧮 Displays **grand total** at checkout
- 🔁 Interactive loop for continuous shopping until exit

---

## 💡 Tech Stack

- Python 3
- `tabulate` for table formatting
- `datetime` for timestamps

---

## 📸 Sample Output

```bash
==================== MAHESH LAMSAL FRUIT SHOP ========================
1. Fruit
2. Juice
3. Coldrink
4. Bill & Payments
5. Exit
Enter your choice:- 1

+-----------+---------------+
| Item      | Price (NPR)   |
+-----------+---------------+
| Apple     | 350           |
| Banana    | 250           |
| Orange    | 200           |
| Watermelon| 100           |
| Grapes    | 270           |
+-----------+---------------+

Enter your Items to purchase:- apple
Enter the quantity of apple: 2

Item purchased successfully.
--------------- BILL --------------
+---------------------+----------+------------+---------------+
| Time                | Item     | Quantity   | Price (NPR)   |
+---------------------+----------+------------+---------------+
| 2025-05-28 14:45:02 | Apple    | 2          | 700           |
| 2025-05-28 14:47:13 | Coke     | 1          | 70            |
+---------------------+----------+------------+---------------+

--------------------------------------------------
Grand Total: NPR 770
