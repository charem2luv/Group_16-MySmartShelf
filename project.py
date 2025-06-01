book_collection = {
    "to_read": set("Atomic Habits,Confession,HTML".split(",")),
    "read": set("Rich dad Poor dad,Go pro,python for beginners".split(","))
}

def add_book(title):
    if title in book_collection["to_read"] or title in book_collection["read"]:
        print(f"'{title}' is already in your list.")
    else:
        book_collection["to_read"].add(title)
        print(f"'{title}' added to your reading list.")

def edit_book(old_title, new_title):
    if old_title in book_collection["to_read"]:
        book_collection["to_read"].remove(old_title)
        book_collection["to_read"].add(new_title)
        print(f"Updated '{old_title}' to '{new_title}' in 'to_read' list.")
    elif old_title in book_collection["read"]:
        book_collection["read"].remove(old_title)
        book_collection["read"].add(new_title)
print(f"Updated '{old_title}' to '{new_title}' in 'read' list.")
