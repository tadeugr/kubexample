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

### Install git

```bash
sudo apt install git
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

