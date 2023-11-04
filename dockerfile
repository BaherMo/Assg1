# Use the Ubuntu base image
FROM ubuntu

# Update package lists and install necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Python libraries using pip (Python package manager)
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Set the default command to start bash
CMD ["/bin/bash"]