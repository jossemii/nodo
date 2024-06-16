#!/bin/bash

set -e

handle_update_errors() {
    exit_code=$?
    echo "Failed to update package lists. Exit code: $exit_code"

    case $exit_code in
        100)
            echo "Lock file exists, maybe another package manager is running. Retrying..."
            sudo rm /var/lib/apt/lists/lock
            sudo apt-get update || handle_update_errors
            ;;
        200)
            echo "Authentication error. Verify if GPG keys are properly added."
            ;;
        *)
            echo "Unknown error occurred during package update."
            ;;
    esac
}

echo "Updating package lists..."
sudo apt-get -o Acquire::AllowInsecureRepositories=true -o Acquire::Check-Valid-Until=false update > /dev/null 2>&1 || handle_update_errors

echo "Installing required build dependencies..."
sudo apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev \
                        libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev > /dev/null

echo "Adding Python 3.11 repository..."
sudo add-apt-repository ppa:deadsnakes/ppa -y > /dev/null
sudo apt-get -y update > /dev/null

echo "Installing Python 3.11 and pip..."
sudo apt-get -y install python3.11 python3.11-venv python3.11-distutils > /dev/null

echo "Installing pip for Python 3.11..."
wget -q https://bootstrap.pypa.io/get-pip.py -O get-pip.py
sudo python3.11 get-pip.py > /dev/null
rm get-pip.py

echo "Creating and activating Python virtual environment..."
python3.11 -m venv venv
source venv/bin/activate

echo "Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt > /dev/null

echo "Installing required system packages for Docker..."
sudo apt-get -y install ca-certificates curl gnupg lsb-release > /dev/null

echo "Adding Docker GPG key and repository..."
if [ ! -f /usr/share/keyrings/docker-archive-keyring.gpg ]; then
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg > /dev/null
fi
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "Updating package lists again..."
sudo apt-get -y update > /dev/null

echo "Installing Docker..."
sudo apt-get -y install docker-ce docker-ce-cli containerd.io > /dev/null

echo "Installing QEMU and binfmt-support for multi-architecture support..."
sudo apt-get -y install qemu binfmt-support qemu-user-static > /dev/null
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes > /dev/null

echo "Installing Rust (Cargo)..."
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y > /dev/null

echo "Sourcing the Rust environment..."
source $HOME/.cargo/env

echo "Executing initialization script for x86..."
sh ./bash/init_x86.sh > /dev/null

echo "Running migrations for Python application..."
python3.11 nodo.py migrate > /dev/null

echo "All steps completed."
