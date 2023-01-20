import json
import tk
import os

def show_editboxes():
    # Load the values from the codes.json file
    with open("codes.json", "r") as f:
        codes = json.load(f)

    # Create the main window
    root = tk.Tk()
    root.title("Edit Boxes")

    # Create the "product" edit box and set its value
    product_label = tk.Label(root, text="Product:")
    product_label.pack()
    product_edit = tk.Entry(root)
    product_edit.pack()
    product_edit.insert(0, codes.get("product", ""))

    # Create the "batch" edit box and set its value
    batch_label = tk.Label(root, text="Batch:")
    batch_label.pack()
    batch_edit = tk.Entry(root)
    batch_edit.pack()
    batch_edit.insert(0, codes.get("batch", ""))

    # Run the GUI
    root.mainloop()

show_editboxes()
