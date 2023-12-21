import tkinter as tk
from tkinter import ttk

# Data
slahundred = ["Azure DNS"]
sla5nines = ["Cosmos DB", "Redis Cache"]
sla4nine5 = ["SQL Database"]
sla4nines = [
    "Event Hubs", "Virtual Machines", "Database for PostgreSQL", "Microsoft Entra ID",
    "API Management", "Azure Comms. Gateway", "Azure Front Door", "Azure Storage",
    "Apache Cassandra MI", "Azure AD EI", "Event Grid", "Private Link",
    "Azure NetApp Files", "Database for MySQL", "Azure Key Vault", "Azure Firewall",
    "Database for MariaDB", "DDoS Protection", "Load Balancer", "Traffic Manager"
]
sla3nine5 = [
    "Databricks", "Kubernetes Service", "Route Server", "Container Apps",
    "Azure Bastion", "App Service", "Application Gateway", "Azure Functions",
    "VPN Gateway", "Azure Red Hat OpenShift", "Virtual WAN", "Cloud Services",
    "ExpressRoute"
]
sla3nines = [
    "Azure AI Search", "Operator Insights", "Azure VMware Solution", "SQL Server Stretch DB",
    "Azure Chaos Studio", "Microsoft Entra DS", "Remote Rendering", "Service Bus",
    "Azure Arc", "Comm. Services", "Site Recovery", "VNet Manager", "Confidential Ledger",
    "Cognitive Services", "Azure Purview", "Container Instances", "Microsoft Dev Box",
    "Defender for Cloud", "Digital Twins", "Energy Data Manager", "Azure Monitor",
    "Media Services", "Network Watcher", "Data Share", "Applied AI Services",
    "Synapse Analytics", "Container Registry", "Load Testing", "Microsoft Sentinel",
    "Spatial Anchors", "Health Data Services", "Automation", "Azure CDN", "StorSimple",
    "Machine Learning", "Data Explorer", "Azure Batch", "Managed Grafana",
    "Information Protection", "IoT Central", "Web PubSub", "Azure Backup",
    "Data Lake Storage", "Bot Service", "Data Factory", "Azure DevOps", "Azure Maps",
    "Notification Hubs", "Microsoft Genomics", "Power BI Embedded", "Azure Spring Apps",
    "IoT Hub", "Logic Apps", "Analysis Services", "App Configuration", "Time Series Insights",
    "Data Lake Analytics", "Lab Services", "Data Catalog", "SignalR Service", "HDInsight",
    "Visual Studio App Center", "Stream Analytics"
]
slana = [
    "Open Datasets", "Microsoft Fabric", "Service Fabric", "DevTest Labs",
    "Dedicated HSM", "IoT Edge", "Azure Advisor", "Azure Migrate",
    "Virtual Network", "Managed Disks", "Project Bonsai", "HDInsight on AKS",
    "VM Scale Sets", "Deployment Environments", "Azure Sphere", "Azure Blueprints",
    "DB Migration Service", "Azure Orbital", "Avere vFXT", "CycleCloud",
    "Object Anchors", "Cost Management", "Data Box", "Internet Analyzer",
    "HPC Cache", "Virtual Desktop", "Defender for IoT", "Azure Policy",
    "Resource Mover", "Azure Elastic SAN", "Dedicated Host", "Managed Apps",
    "Managed Lustre", "Azure Quantum", "Cloud Shell", "Azure Portal",
    "Azure Lighthouse", "Azure Automanage", "Kubernetes Fleet Manager", "Copilot in Azure"
]

class SLAViewerApp:
    def __init__(self, master):
        self.master = master
        master.title("SLA Calculator - AZURE")

        self.selected_services = []
        self.selected_service = tk.StringVar()
        self.selected_service.set(slahundred[0])  # Set default value

        # Dropdown menu
        self.service_dropdown = ttk.Combobox(master, textvariable=self.selected_service, values=slahundred + sla5nines +
                                                                                 sla4nine5 + sla4nines +
                                                                                 sla3nine5 + sla3nines + slana)
        self.service_dropdown.grid(row=0, column=0, pady=10)

        # "+" button to add services to the group
        self.add_button = tk.Button(master, text="+", command=self.add_service)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        # Show SLA button
        self.show_sla_button = tk.Button(master, text="Show SLA", command=self.show_sla)
        self.show_sla_button.grid(row=1, column=0, pady=10)

        # SLA result label
        self.sla_label = tk.Label(master, text="")
        self.sla_label.grid(row=2, column=0, pady=10)

        # Services table
        self.services_table = ttk.Treeview(master, columns=("Service", "SLA"), show="headings", height=5)
        self.services_table.heading("Service", text="Service")
        self.services_table.heading("SLA", text="SLA")
        self.services_table.grid(row=3, column=0, pady=10, padx=10, columnspan=2)

    def add_service(self):
        service = self.selected_service.get()
        self.selected_services.append(service)
        self.service_dropdown.set("")  # Clear the selection
        self.update_services_table()

    def show_sla(self):
        if not self.selected_services:
            self.sla_label.config(text="No services selected.")
            return

        collective_sla = 1
        for selected_service in self.selected_services:
            collective_sla *= self.get_sla_value(selected_service)

        # Display collective SLA result
        self.sla_label.config(text=f"Collective SLA for below services = {collective_sla} %")

    def get_sla_value(self, service):
        # Determine SLA category
        if service in slahundred:
            return 100
        elif service in sla5nines:
            return 99.999
        elif service in sla4nine5:
            return 99.995
        elif service in sla4nines:
            return 99.99
        elif service in sla3nine5:
            return 99.95
        elif service in sla3nines:
            return 99.9
        elif service in slana:
            return 1
        else:
            return 0  # Handle the case when the service is not found

    def update_services_table(self):
        # Clear previous entries
        for row in self.services_table.get_children():
            self.services_table.delete(row)

        # Insert new entries
        for service in self.selected_services:
            sla_value = self.get_sla_value(service)
            self.services_table.insert("", "end", values=(service, sla_value))

if __name__ == "__main__":
    root = tk.Tk()
    app = SLAViewerApp(root)
    root.mainloop()
