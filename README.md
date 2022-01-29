### How to save Windows 10 Spotlight Images and Find Their Location

##### We show you how to save Windows 10 Spotlight Images by finding their location manually or using an app for automatic download.


**Location** **:**
```
%LocalAppData%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
```
**Run** **:**
```
python3 spotlight.py
```

landscape for desktop
![landscape](/landscape.png "landscape")

portrait for mobile 
![portrait](/portrait.png "portrait")


### Auto Py to Exe

```cmd
pyinstaller --noconfirm --onefile --console --icon "./spotlight.ico"  "./spotlight.py"
```