#!/usr/bin/env python3
import os
import random
import string

def generate_random_string(length=8):
    """Generate a random string of specified length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def create_yaml_file(file_path, name, identifier, project_identifier, org_identifier):
    """Create a project-specific YAML file with the specified name and identifier."""
    # Create YAML content with project and org identifiers
    yaml_content = f"""service:
  name: {name}
  identifier: {identifier}
  projectIdentifier: {project_identifier}
  orgIdentifier: {org_identifier}
  serviceDefinition:
    spec: {{}}
    type: Kubernetes
"""
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write YAML file
    with open(file_path, 'w') as f:
        f.write(yaml_content)

def main():
    """Generate 520 project-specific YAML files with random names and identifiers."""
    # Define your organization and project identifiers
    org_identifier = "default"
    project_identifier = "anishtest" # You can change this to your project's ID

    # Create the correct directory structure for project-level services
    harness_dir = os.path.join(os.getcwd(), f'.harness/orgs/{org_identifier}/projects/{project_identifier}/services')
    os.makedirs(harness_dir, exist_ok=True)
    
    num_files_to_generate = 520
    print(f"Generating {num_files_to_generate} YAML files in {harness_dir}...")
    
    # Generate files
    for i in range(1, num_files_to_generate + 1):
        # Generate random name for the file
        file_name = f"{generate_random_string(6)}_{i}.yaml"
        file_path = os.path.join(harness_dir, file_name)
        
        # Generate random name and identifier for the content
        service_name = generate_random_string(8)
        service_identifier = service_name
        
        # Create the YAML file, passing the project and org identifiers
        create_yaml_file(file_path, service_name, service_identifier, project_identifier, org_identifier)
        
        # Print progress every 50 files
        if i % 50 == 0:
            print(f"Generated {i} files...")
    
    print(f"Successfully generated {num_files_to_generate} YAML files in {harness_dir}")

if __name__ == "__main__":
    main()