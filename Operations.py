books = {}
members = []
genres = ("Fiction", "Non-Fiction", "Sci-Fi")

def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        return "Book already exists."
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {"title": title, "author": author, "genre": genre, "total_copies": total_copies}
    return "Book added successfully."

def add_member(member_id, name, email):
    for member in members:
        if member["member_id"] == member_id:
            return "Member ID already exists."
    members.append({"member_id": member_id, "name": name, "email": email, "borrowed_books": []})
    return "Member added successfully."

def search_books(keyword):
    results = [book for book in books.values() if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]
    return results

def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        return "Book not found."
    if genre and genre not in genres:
        return "Invalid genre."
    if title: books[isbn]["title"] = title
    if author: books[isbn]["author"] = author
    if genre: books[isbn]["genre"] = genre
    if total_copies is not None: books[isbn]["total_copies"] = total_copies
    return "Book updated successfully."

def delete_book(isbn):
    if isbn not in books:
        return "Book not found."
    del books[isbn]
    return "Book deleted successfully."

def borrow_book(member_id, isbn):
    for member in members:
        if member["member_id"] == member_id:
            if isbn not in books:
                return "Book not found."
            if books[isbn]["total_copies"] <= 0:
                return "No copies left."
            if len(member["borrowed_books"]) >= 3:
                return "Borrow limit reached (3 books)."
            books[isbn]["total_copies"] -= 1
            member["borrowed_books"].append(isbn)
            return "Book borrowed successfully."
    return "Member not found."

def return_book(member_id, isbn):
    for member in members:
        if member["member_id"] == member_id:
            if isbn in member["borrowed_books"]:
                member["borrowed_books"].remove(isbn)
                books[isbn]["total_copies"] += 1
                return "Book returned successfully."
            return "This book was not borrowed by the member."
    return "Member not found."