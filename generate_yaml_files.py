import os
import random
import string

def generate_random_string(length=8):
    """Generate a random string of specified length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def create_yaml_file(file_path, name, identifier, project_identifier, org_identifier):
    """Create a project-specific YAML file with the specified name and identifier."""
    # Create YAML content. The projectIdentifier will match the random directory name.
    yaml_content = f"""service:
  name: {name}
  identifier: {identifier}
  projectIdentifier: {project_identifier}
  orgIdentifier: {org_identifier}
  serviceDefinition:
    spec: {{}}
    type: Kubernetes
"""
    
    # Ensure the directory exists before writing the file
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the YAML file
    with open(file_path, 'w') as f:
        f.write(yaml_content)

def main():
    """Generate 520 YAML files, grouped into random directories."""
    org_identifier = "default"
    num_files_to_generate = 520
    files_generated_count = 0

    print(f"Generating {num_files_to_generate} YAML files in groups of 5-10 per random directory...")

    # Loop until we've generated the desired number of files
    while files_generated_count < num_files_to_generate:
        # --- CHANGE: Create a new random directory name for a group of files ---
        # This directory will be created in the current working path.
        random_dir_name = generate_random_string(12)
        current_directory_path = os.path.join(os.getcwd(), random_dir_name)
        
        # Decide how many files to create in this new directory
        num_files_in_this_group = random.randint(5, 10)
        
        print(f"\nCreating new directory '{random_dir_name}' for {num_files_in_this_group} files...")

        # --- CHANGE: Inner loop to create a group of files in the same directory ---
        for i in range(num_files_in_this_group):
            # Stop if we have reached the total file limit
            if files_generated_count >= num_files_to_generate:
                break

            files_generated_count += 1
            
            # Generate a random name for the YAML file
            file_name = f"{generate_random_string(6)}_{files_generated_count}.yaml"
            file_path = os.path.join(current_directory_path, 'services', file_name)
            
            # Generate random name and identifier for the service content
            service_name = generate_random_string(8)
            service_identifier = service_name
            
            # Create the YAML file. The random directory name is used as the projectIdentifier.
            create_yaml_file(file_path, service_name, service_identifier, random_dir_name, org_identifier)
        
        print(f"Generated {files_generated_count}/{num_files_to_generate} files so far.")

    print(f"\nSuccessfully generated a total of {files_generated_count} YAML files.")

if __name__ == "__main__":
    main()