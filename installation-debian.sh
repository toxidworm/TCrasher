#!/bin/sh

installation()
{
    sudo apt install figlet
    sudo apt install lolcat
    sudo apt install python3
    sudo apt install python3-pip
    pip install -r requirements.txt
    clear
    figlet Installation complete! | lolcat
    echo "Have a nice time destroying servers ૮ ˶ᵔ ᵕ ᵔ˶ ა"
    echo "Coded by ToxidWorm"
}

clear
echo "This script will install requirements to ToxidWorm's Discord crasher"
read -p "Do you want to start installation? (y/n)?" choice
case "$choice" in 
  y|Y ) installation;;
  n|N ) echo "Operation canceled by user" && exit;;
  * ) echo "Invalid command." && exit;;
esac