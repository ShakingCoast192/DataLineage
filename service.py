import pickle
import os

PICKLE_FILE = "data.pkl"

def load_data():
    """Load data from the pickle file."""
    if os.path.exists(PICKLE_FILE) and os.path.getsize(PICKLE_FILE) > 0:
        with open(PICKLE_FILE, "rb") as file:
            return pickle.load(file)
    return []  # Return an empty list if the file doesn't exist or is empty

def save_data(data):
    """Save data to the pickle file."""
    with open(PICKLE_FILE, "wb") as file:
        pickle.dump(data, file)

def add_SLE():
    """Add a new SLE with its services."""
    data = load_data()

    SLE_name = input("Enter the name of the new SLE: ")
    if SLE_name in data:
        print(f"SLE '{SLE_name}' already exists!")
        return

    services = []
    while True:
        service_id = input("Enter service ID (or 'done' to finish): ")
        if service_id.lower() == 'done':
            break
        service_name = input("Enter service name: ")
        services.append({"service_id": service_id, "service_name": service_name})

    data[SLE_name] = services
    save_data(data)
    print(f"SLE '{SLE_name}' with its services added successfully!")

def add_service():
    """Add a service to an existing SLE."""
    data = load_data()

    if not data:
        print("No SLEs found! Add an SLE first.")
        return

    print("Available SLEs:")
    for SLE in data.keys():
        print(f"- {SLE}")

    SLE_name = input("Enter the name of the SLE to update: ")
    if SLE_name not in data:
        print(f"SLE '{SLE_name}' does not exist!")
        return

    service_id = input("Enter service ID: ")
    service_name = input("Enter service name: ")
    data[SLE_name].append({"service_id": service_id, "service_name": service_name})
    save_data(data)
    print(f"Service '{service_name}' added to SLE '{SLE_name}'.")

def delete_SLE(SLE_name):
    """Delete an SLE."""
    data = load_data()

    if SLE_name in data:
        del data[SLE_name]
        save_data(data)
        print(f"SLE '{SLE_name}' deleted successfully.")
    else:
        print(f"SLE '{SLE_name}' does not exist.")

def delete_service(service_name):
    """Delete a service from all SLEs."""
    data = load_data()

    service_found = False
    for SLE, services in data.items():
        service_to_delete = None
        for service in services:
            if service['service_name'] == service_name:
                service_to_delete = service
                break
        if service_to_delete:
            services.remove(service_to_delete)
            service_found = True
            save_data(data)
            print(f"Service '{service_name}' deleted from SLE '{SLE}'.")
            break

    if not service_found:
        print(f"Service '{service_name}' not found in any SLE.")
    
def display_data():
    """Display the current data lineage."""
    data = load_data()
    if not data:
        print("No data lineage found!")
        return

    print("Data Lineage:")
    for SLE, services in data.items():
        service_chain = "->".join([f"{service['service_id']}({service['service_name']})" for service in services])
        print(f"SLE: {SLE} -> {service_chain}")

def search_SLE(SLE_name):
    """Search and display the data lineage for a specific SLE."""
    data = load_data()
    if not data:
        print("No data lineage found!")
        return

    found = False
    print(f"Data Lineage for SLE '{SLE_name}':")
    if SLE_name in data:
        service_chain = "->".join([f"{service['service_id']}({service['service_name']})" for service in data[SLE_name]])
        print(f"SLE: {SLE_name} -> {service_chain}")
        found = True

    if not found:
        print(f"No data lineage found for SLE '{SLE_name}'.")

def search_service(service_name):
    """Search and display all data lineages containing the specific service."""
    data = load_data()
    if not data:
        print("No data lineage found!")
        return

    found = False
    print(f"Data Lineages containing service '{service_name}':")
    for SLE, services in data.items():
        service_chain = "->".join([f"{service['service_id']}({service['service_name']})" for service in services])
        if service_name in [service['service_name'] for service in services]:
            print(f"SLE: {SLE} -> {service_chain}")
            found = True
    
    if not found:
        print(f"No lineages found containing service '{service_name}'.")