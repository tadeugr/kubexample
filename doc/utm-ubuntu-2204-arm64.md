# Setup UTM Ubuntu 22.04 ARM64

## Install UTM

Download and install UTM for Mac following the official website documentation: https://mac.getutm.app/

## Create the VM

Go to https://mac.getutm.app/gallery/ubuntu-20-04

Click on `Open in UTM` button, it should open a dialog window, click on `Open UTM`.

Follow the instructions on screen to start the VM.

Open a terminal and run `uname -a` command, you should see somehting like this:

```
Linux ubuntu 5.15.0-87-generic #97-Ubuntu SMP Tue Oct 3 09:52:42 UTC 2023 aarch64 aarch64 aarch64 GNU/Linux
```

## Setup Ubuntu

Open a terminal and run:

```bash
sudo apt update
```

### Install required packages

```bash
sudo apt install git python3-pip gunicorn tmux
```

### Install Docker

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo usermod -aG docker $USER
newgrp docker
```

### Install kind

```bash
# For ARM64
[ $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

### Install kubectl

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

### Install k9s

```bash
curl -sS https://webinstall.dev/k9s | bash
```

## Troubleshooting

### missing profile snap.firefox.firefox

If you try openning Firefox and see this error:

```
missing profile snap.firefox.firefox. Please make sure that the snapd.apparmor service is enabled and started
```

Run the following commands to fix it:

```bash
sudo apt install --reinstall snapd
snap refresh --channel=beta firefox
```

