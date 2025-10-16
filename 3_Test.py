from Operations import *
def run_tests():
    assert add_book("001", "OOP", "Smith", "Fiction", 2) == "Book added successfully."
    assert add_member("M001", "Alice", "alice@example.com") == "Member added successfully."
    assert borrow_book("M001", "001") == "Book borrowed successfully."
    assert borrow_book("M001", "001") == "Book borrowed successfully."
    assert borrow_book("M001", "001") == "No copies left."
    assert return_book("M001", "001") == "Book returned successfully."
    assert delete_book("001") == "Book deleted successfully."
    print("All tests passed successfully!")
if __name__ == "__main__":
    run_tests()
