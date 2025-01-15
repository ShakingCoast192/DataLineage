import service

def main_menu():
    while True:
        print("\nData Lineage Management")
        print("\n1. Search for a Data Lineage")
        print("2. Add New SLE")
        print("3. Add Service to Existing SLE")
        print("4. Delete SLE or Service")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == "1":
            search_choice = input("Search by (1) SLE name or (2) Service name: ")
            if search_choice == "1":
                SLE_name = input("Enter SLE name to search for: ")
                service.search_SLE(SLE_name)
                break
            elif search_choice == "2":
                service_name = input("Enter service name to search for: ")
                service.search_service(service_name)
                break
            else:
                print("Invalid choice! Please select 1 or 2.")
        elif choice == "2":
            service.add_SLE()
        elif choice == "3":
            service.add_service()
        elif choice == "4":
            delete_choice = input("Delete (1) SLE or (2) Service: ")
            if delete_choice == "1":
                SLE_name = input("Enter SLE name to delete: ")
                service.delete_SLE(SLE_name)
            elif delete_choice == "2":
                service_name = input("Enter service name to delete: ")
                service.delete_service(service_name)
            else:
                print("Invalid choice! Please select 1 or 2.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main_menu()