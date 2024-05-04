provider "google" {
  project     = "fetch-421023"
  region      = "us-central1"
  # credentials = file("path/to/credentials.json")
}


resource "google_project_iam_custom_role" "etl_role" {
  role_id     = "locationsETLRole"  # Specify your custom role ID here
  project     = "fetch-421023" # Specify your project ID here

  title       = "Locations-ETL-Role"
  description = ""

  permissions = []
}


resource "google_container_cluster" "fetch_db" {
  name     = "example-cluster"
  location = "us-central1"

  node_pool {
    name       = "default-pool"
    machine_type = "n1-standard-1"
    disk_size_gb = 100
    disk_type = "pd-standard"
    min_count = 1
    max_count = 3
    autoscaling {
      min_node_count = 1
      max_node_count = 3
    }
  }
}