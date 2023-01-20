import json


def list_unique_combinations(file_name):
  # Open the file and read the json data
    with open(file_name, "r") as f:
      data = f.read()
    # parse json data
    data_dict = json.loads(data)
    # create a set to store unique combinations
    unique_combinations = set()

    # iterate over products
    for product in data_dict["products"]:
        # iterate over batches
        for batch in product["batches"]:
            coated = batch.get("coated", "")
            if coated:
              coated = "Ct"+coated
            lot = "/".join(batch.get("lot", ""))
            # add the combination to the set
            unique_combinations.add((product["product"], batch["batch"], lot, coated))
    return unique_combinations


file_name = "/Users/matbook/PyLMS/Clipboard GPT/LMScodes.json"
for combination in list_unique_combinations(file_name):
    print(combination)
# print(list_unique_combinations(file_name))