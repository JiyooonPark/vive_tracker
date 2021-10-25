[![Link to a video of this project in action.](https://img.youtube.com/vi/fvbSUXGViSY/0.jpg)](https://youtu.be/fvbSUXGViSY)

Tested on **_ROS Melodic + Ubuntu 18.04_**

#### Note: This depends on SteamVR on Ubuntu. Be advised that SteamVR is not fully supported on Ubuntu and may not install properly with your version of Ubuntu/graphics drivers/hardware. I recommend you try to get SteamVR installed on your computer before considering this node for your project. 

## Prerequisites

Up to date graphics drivers

x86 architecture

SteamVR requires >4GB disk space


## Installation Instructions
#### 1. [Install the latest VulkanSDK.](https://vulkan.lunarg.com/sdk/home#linux)

Or follow the commands below
Upgrade your system to be current on package updates:

```bash
sudo apt update
sudo apt upgrade
```

```bash
wget -qO - http://packages.lunarg.com/lunarg-signing-key-pub.asc | sudo apt-key add -
sudo wget -qO /etc/apt/sources.list.d/lunarg-vulkan-bionic.list http://packages.lunarg.com/vulkan/lunarg-vulkan-bionic.list
sudo apt update
sudo apt install vulkan-sdk
```


#### 2. Install Steam [link](http://store.steampowered.com/)

```bash
 sudo apt-get install libsdl2-dev libudev-dev libssl-dev zlib1g-dev python-pip
 sudo add-apt-repository multiverse
 sudo apt install steam
 sudo apt install steam-devices
 sudo apt install libvulkan1
```

   1. Open steam with `steam` command, or through the Ubuntu menu. Make a Steam account & Log in.
   
   1. Enable the Steam beta through the Steam Menu -> Settings -> Account -> Beta Participation. [See the video here to see how to enable the beta.](https://www.youtube.com/watch?v=7AFUcj3HpvE)
   
   1. (Recommended) Save your credentials while logging in, and once you do log in open the `Steam` Menu item in the top left corner and select `Go Offline`. This prevents Steam from updating every time you use the Vive Tracker. 

   1. _refer to troubleshoot for uninstalling steam_

#### 3. Install SteamVR. 

   1. Click Library

   1. Click VR

   1. On the left you should now see SteamVR. Select it and click the the blue Install button.

   1. (Optional) Make a Symbolic Link from libudev.so.0 to libudev.so.1 for SteamVR to use. 
      
      `sudo ln -s /lib/x86_64-linux-gnu/libudev.so.1 /lib/x86_64-linux-gnu/libudev.so.0`



#### 4. Install pyopenvr

```angular2html
 pip install openvr==1.3.2201
```
If you have already installed openvr, then reinstalling the old version does not overwrite yout original version. If you already have it installed you should replace your `__init__.py` in /usr/local/lib/python2.7/dist-packages/openvr to the [`__init__.py`](https://github.com/jiyoonpark0207/vive_tracker/blob/master/__init__.py) in this repository. 



#### ~~5. Vive equipment settings (this part does not seem to be valid anymore)~~
   1. Disable the headset requirement and enable a null (simulated) headset:
   
      ```bash
      gedit ~/.steam/steam/steamapps/common/SteamVR/resources/settings/default.vrsettings
      ```
   
      1. Change the third line from `"requireHmd" : true,` to `"requireHmd" : false,`
   
      2. Add `"activateMultipleDrivers" : true`, and add the line `"forcedDriver": "null"` beneath it.
      
   1. Open `default.vrsettings`
   
      ```bash
      gedit ~/.steam/steam/steamapps/common/SteamVR/drivers/null/resources/settings/default.vrsettings
      ```
   
      1. Set `enable` (line 3) to `true` in null driver to enable it.
   
  [Source](https://www.reddit.com/r/Vive/comments/6uo053/how_to_use_steamvr_tracked_devices_without_a_hmd/) 
  


#### 6. Install this project in your catkin workspace.

```bash
cd ~/catkin_ws/src/
git clone https://github.com/moon-wreckers/vive_tracker.git
cd ~/catkin_ws
catkin_make
```


## Usage
1. Start SteamVR from the Steam Library (If you encounter `VRClientDLLNotFound`, make sure all of the dependencies are installed properly, especially VulkanSDK, and delete and recreate the symbolic link described above).

2. Turn on the tracker with its button, and make sure that its wireless USB dongle is plugged in to your computer. If the tracker shows up in the SteamVR overlay skip to step 4.

3. Sync the tracker. Hold the button on the tracker until the light blinks. On the SteamVR overlay click the "SteamVR" dropdown menu. Click Devices->Pair Controller. The Tracker should then pair with the computer, and a green outline of the tracker should appear on the SteamVR overlay. If this doesn't work try unplugging the wireless USB dongle, plugging it back in, and restarting SteamVR. Restarting your computer wouldn't hurt either.

4. Ensure the Lighthouse base stations are turned on, facing each other, have green lights showing on them Place the tracker in view of the Base Stations. The SteamVR overlay should now show two green square Base Stations and a solid green Tracker hexagon. The tracker is now working. 

     1. If you're only using 1 Base Station, make sure it's set to mode A.
     
     2. If you're using 2 Base Stations without a sync cable, ensure they're set to modes B and C.
     
     3. If you're using 2 Base Stations with a sync cable, ensure they're set to modes A and B.

5. Run this ROS node. 

```angular2html
source ~/catkin_ws/devel/setup.bash
roslaunch vive_tracker vive_tracker.launch
``` 
1. Now open another terminal and run `rostopic echo /vive/LHR_BD4ED973_odom` to view the x y z roll pitch yaw output from the tracker.

1. (Optional) Start RViz in another terminal with `rviz`

1. (Optional) In the lower left corner of RViz click on `Add`, and scroll down the Add menu to add a `TF`. If all went well you should now be able to see the tracker moving in RViz. 

1. If for some reason it isn't working, check to ensure that the Tracker is turned on, SteamVR is still running, the tracker icon is green, and the vive_tracker ros node is still running.


## Command Line

Here's a handy command, run this in the command line to start SteamVR with the command `steamvr`

`alias steamvr='LD_LIBRARY_PATH=~/.steam/bin32/ ~/.steam/bin32/steam-runtime/run.sh ~/.steam/steam/steamapps/common/SteamVR/bin/vrstartup.sh' >> ~/.bashrc && source ~/.bashrc`

This will start the server in another process, so you're free to keyboard interrupt (Ctrl+C) the terminal once the server starts. 

To kill the SteamVR process:

`sudo pkill -9 vr*`

## Trouble Shoot

Error | Solution
------- | ---------
bluetooth not available | reboot your computer until it connects correctly
Initializing looking for your VR hardware | reboot your computer until it connects correctly
OSError: openvr_api_64: cannot open shared object file: No such file or directory | reinstall openvr
Import openvr related errors | you have the wrong openvr version. Refer to the [Install openvr] section of the README.md
error 307 | neglectable

- How to remove steam form ubuntu 
```angular2html
sudo apt-get remove steam steam-launcher
sudo apt-get purge steam steam-launcher
rm -rf ~/.local/share/Steam && rm -rf ~/.steam
```

Also delete desktop shortcut if you made one

## Links

This is based off of Triad Semiconductor's awesome tutorial found here:

http://help.triadsemi.com/steamvr-tracking/steamvr-tracking-without-an-hmd/

Also thanks to Christopher Bruns for his work on pyopenvr.

https://github.com/cmbruns/pyopenvr
