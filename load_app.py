#! /usr/bin/env python3
#
#
# WARNING: This program will only work on newer Linux distributions that have an /etc/os-release file in the correct format,
# if your distro is unsupported, please open an Issue or a Pull Request
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi

import math
import sys
import subprocess as sub

import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk

import icon_rc

class SystemInfo(QtWidgets.QMainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)
    loadUi("main_layout.ui", self)
    self.ui = loadUi("main_layout.ui", self)

    self.updateOSInfo()
    self.updateVersionID()
    self.updateProductInfo()
    self.updateCPUInfo()
    self.updateMemInfo()
    self.updateDiskInfo()
    self.updateGPUInfo()
    self.updateSerialNumber()
    self.updateIcon()

  def updateOSInfo(self):
    os_name = self.ui.OSName.text() # read the contents of the OSName widget, so it can be replaced with the os name and codename

    release_file = open('/etc/os-release').read().split('\n') # read the /etc/os-release file and split it by line
    ## release_file = open('/home/squirrel/temp/os-release').read().split('\n') # read the /etc/os-release file and split it by line
    release_info = dict() # create a new, empty dictionary

    #parse the contents of the file and add it to said dictionary

    for x in release_file:
      release_line = x.split('=', 2) #gets the key and value from the release file

      if len(release_line) == 2: # if there's a blank line at the end of the file, or some other annoyingness, drop anything that isn't valid
        release_info[release_line[0]] = release_line[1].replace('"','') # sets value at "key" to "value"

    #adjust the OS Name and release text depending on whether the OS has numbered releases, or if it's rolling release like Arch and a few others (i use arch btw)

    try: # if the OS has a codename, display it here, if it doesn't, it'll throw an error and run the other thing, meant to differentiate between rolling release distros, and not rolling release
      codename = release_info['VERSION_CODENAME'].lower().capitalize() #gets the version codename, error happens here
      self.version_id = release_info['VERSION_ID']
      os_name = os_name.replace('$osName', release_info['NAME'].replace('GNU/Linux', '')) # sets OS name to the OS name, strips out the GNU/Linux part for debian because it takes up a lot of space
      os_name = os_name.replace('$releaseName', codename) # shows the codename

    except Exception as e: # only runs if an exception is raised in the above code, basically this is rolling release land
      ## print(e) # debugging

      try: #in case there is only one word in the OS name
        os_name = os_name.replace('$osName', release_info['NAME'].split(' ',2)[0]) #shows the first word of the distro name
        os_name = os_name.replace('$releaseName', release_info['NAME'].split(' ',2)[1]) #shows all the following words if they exist

      except: # we honestly don't care about that, if there's one word, there's one word
        os_name = os_name.replace('$releaseName', '') #if there's 1 word, just remove the $releaseName thing cuz it's only a placeholder
        pass # let the error slide

    self.ui.OSName.setText(os_name) # update the OS name and codename UI element
  
  def updateVersionID(self):

    version = self.ui.Version.text() # read the contents of the Version label, so it can be replaced with the system version (or the kernel version)

    try:
      version_id = self.version_id # probably bad practice but it will tell us if the OS uses versions or if we need to grab the kernel version
    
    except Exception as fail:
      print(fail)
      version_id = sub.run(['uname', '-r'], capture_output=True, text=True).stdout

    version = version.replace('$versionNum', version_id)

    self.ui.Version.setText(version)

  def updateProductInfo(self):
    
    product_info = self.ui.HostType.text() # read the contents of the Version label, so it can be replaced with the product information

    product_name = open('/sys/devices/virtual/dmi/id/product_name').read().strip() # reads the product name from the dmi directory and strips off whitespace

    product_info = product_info.replace('$productName', product_name) # updates the product name

    def getPrimaryScreenSize():
      # Code taken from here: https://askubuntu.com/questions/736113/how-can-i-get-my-laptops-monitor-size

      dsp = Gdk.Display.get_default()
      n_mons = dsp.get_n_monitors
      
      try:
        mon = dsp.get_monitor(1)
      except:
        mon = dsp.get_monitor(0)
      w = mon.get_width_mm()/25.4
      h = mon.get_height_mm()/25.4
      
      screen_size = math.floor(((w**2)+(h**2))**(0.5))

      return screen_size
      
    
    screen_size = str(getPrimaryScreenSize())
    screen_size += '-inch'

    product_info = product_info.replace('$screenSize', screen_size) # updates the screen size

    bios_date = open('/sys/devices/virtual/dmi/id/bios_date').read().strip() # gets the bios install date from the bios to approximate the manufacture date, this method is pretty much useless as it shows when you last upgraded BIOS, if you know a better way, make a PR

    date_array = bios_date.split('/') # gets individual values for month, day and year

    month = date_array[0] # for some strange reason, the month appears in the first column, you should not do this as this is completely illogical :)

    if month[0] == '0':
      month = month[1]
    
    month = int(month)
    
    season = '' # declares the season variable (shows whether the PC is early, mid or late of the year it was made)

    if month <= 0 or month > 12:
      raise Exception('Something seems to be wrong with your BIOS date...') # because something is wrong with it, it doesn't follow the american convention which we are following here

    if month > 0 and month < 5:
      season = 'Early'
    elif month > 4 and month < 9:
      season = 'Mid'
    else:
      season = 'Late'

    year = date_array[2] # at least the year is in the right place

    date = season + ' ' + year # combines the season with the year (i.e. Early 2017 or Late 2020)

    product_info = product_info.replace('$productionYear', date) # replaces the variable with the real value

    self.ui.HostType.setText(product_info) # updates the UI element with the replaced info

  def updateCPUInfo(self):
    
    cpu_text = self.ui.CPUInfo.text() # gets the value of the CPUInfo element which can and will be replaced

    cpu_cmd = sub.run('lscpu', capture_output=True, text=True).stdout.strip().split('\n') # captures the output of the lscpu and turns it into an array, also strips output

    cpu_info = dict() # declares an empty dictionary for cpu info

    for x in cpu_cmd:
      cpu_line = x.split(':', 2) # splits the array so it can be converted to the dictionary
      cpu_line[1] = cpu_line[1].strip() # strips the very annoying whitespace

      if len(cpu_line) == 2:
        cpu_info[cpu_line[0].lower().replace(' ', '_')] = cpu_line[1] # add to dictionary and make the keys conform to a standard (lowercase with underscores)

    # here we start calculating the frequency and other stuff

    cpu_freq = float(cpu_info['cpu_max_mhz'])/1000 # converts frequency to a floating point number so we can turn it into GHz, because MHz is irrelevant
    
    cpu_freq = str(cpu_freq) + ' GHz' # now it converts it to a nice string

    # now for the fun part, converting physical core count to a human readable format...

    cpu_cores = int(cpu_info['core(s)_per_socket'])*int(cpu_info['socket(s)']) # gets the core count from the total number of cores per socket * socket count

    core_text = '' # empty var

    # numbers to text basically

    if cpu_cores == 1:
      core_text = 'Single-Core'
    elif cpu_cores == 2:
      core_text = 'Dual-Core'
    elif cpu_cores == 3:
      core_text = 'Triple-Core'
    elif cpu_cores == 4:
      core_text = 'Quad-Core'
    elif cpu_cores == 6:
      core_text = 'Hex-Core'
    elif cpu_cores == 8:
      core_text = 'Octa-Core'
    else:
      core_text = str(cpu_cores) + '-Core' # if it's non-standard, we just use the number

    cpu_name = cpu_info['model_name'].replace('(R)','').replace('(TM)','').replace('(r)','').replace('(tm)','').split('-')[0].split(' CPU ')[0] # removes trademark symbol mess and gets rid of the exact model number for Intel CPUs, may not work for AMD

    cpu_final = cpu_freq + ' ' + core_text + ' ' + cpu_name # adds all the values into a nice final variable

    cpu_text = cpu_text.replace('$cpuInfo', cpu_final) # replace the placeholder with real values

    self.ui.CPUInfo.setText(cpu_text) # update the UI element

  def updateMemInfo(self):
    # WARNING: Some parts of this module may not work without root/sudo access (DMI table access if you're interested, which you should be as you are letting this program run as root!)

    mem_text = self.ui.MemInfo.text() # gets text from MemInfo UI element

    mem_info = sub.run('lsmem', capture_output=True, text=True).stdout.strip().split('\n') # runs lsmem to get memory capacity

    for x in mem_info:
      if 'Total online memory:' in x:
        mem_capacity = x.replace('Total online memory:','').strip() # once we have the line we need, delete the key and strip whitespace

    mem_unit = mem_capacity[-1] + 'B'

    mem_capacity = mem_capacity[:-1] + ' ' + mem_unit

    mem_speed = 0 # defaults
    mem_type = 'Unknown' # defaults

    # CAREFUL: here be dragons, and also root access is required, if you don't have it, the dialog will just display "16 GB Unknown" instead of "16 GB 2133 MHz DDR4" (for example) next to the Memory info line

    try: # if we get some sort of permissions error, we will read some files, if they don't exist, just display 'Unknown'
      dmi_info = sub.run(['dmidecode','--type', '17'], capture_output=True, text=True).stdout.strip().split('\n') # reads the RAM info from the DMI tables

      if len(dmi_info) <= 5: # the output will be very long if it is correct, so if it's 5 lines or less, something obviously failed
        raise Exception('Insufficient privileges to read DMI tables')

      # OK so if this code is running, we're good to go
      # ASSUMPTION: this program assumes that all RAM slots have the same generation and speed of RAM in them (i.e. if the first one is DDR4 2133MHz, the rest are also), if they aren't, it'll be too messy to display in the program :\
      for x in dmi_info:

        if "Type:" in x and mem_speed == 0:
          mem_speed = x.strip().split(':',2)[1].strip()

        elif "Speed:" in x and mem_type == 'Unknown':
          mem_type = x.strip().split(':',2)[1].strip().replace('T/s','Hz')
      
      # ok, now we are saving the info in a user-readable file so the script doesn't have to be run as root EVERY. SINGLE. TIME.
      try:
        mem_file = open('/var/cache/qtfetch', 'w').close() # clear the file first

      finally:
        mem_file = open('/var/cache/qtfetch', 'w')# now we open the file
        mem_file.write(mem_type + '\n')
        mem_file.write(str(mem_speed) + '\n')
        mem_file.close()
    
    except Exception as e: # so the user doesn't have root privileges, not the end of the world

      print(e, '- Trying alternative route')

      try:
        print('Attempting to read cached data...')
        mem_file = open('/var/cache/qtfetch', 'r').read().strip().split('\n')
        mem_speed = mem_file[0]
        mem_type = mem_file[1]

        print('Successfully read memory info from cached data')
      
      except Exception as e:
        print('Reading cached data failed:', e) # ok, if this runs, that means we don't have it cached either, please follow the instructions you idiot!!!

        mem_speed = ''
        mem_type = 'Unknown'
    
    mem_final = mem_capacity + ' ' + mem_speed + ' ' + mem_type

    mem_text = mem_text.replace('$memInfo', mem_final)

    self.ui.MemInfo.setText(mem_text)
      
  def updateDiskInfo(self):
    # This function was not painful to write like all the other ones, which gave me a f***ing migraine

    disk_text = self.ui.Disk.text() # get UI ekement

    mount_file = open('/proc/mounts', 'r').read().strip().split('\n') # read system mounts

    disk = 'Unknown' # default value is unknown

    for mount in mount_file: # iterates disks to see what's mounted at /
      if mount.split(' ')[1] == '/':
        disk = mount.split(' ')[0] # get the block device name, I might convert this to disk label at some point in the future
        break # and of course there can only be one disk at /

    disk_text = disk_text.replace('$diskName',disk) # replace placeholder

    self.ui.Disk.setText(disk_text) # update UI element

  def updateGPUInfo(self):

    gpu_text = self.ui.GPUInfo.text() # get UI element

    pci_command = sub.run('lspci', capture_output=True, text=True).stdout.strip().split('\n') # runs lspci to get PCI devices and then filter out the GPU

    for device in pci_command: # iterate through PCI devices
      if 'VGA' in device: # if its the GPU
        gpu = device.split(' ', 1)[1].split(':',2)[1].split('(')[0].strip().replace('Corporation','') # get the GPU name and remove the irrelevant bits
        break # we only accept 1 GPU
    
    gpu_text = gpu_text.replace('$gpuInfo', gpu)

    self.ui.GPUInfo.setText(gpu_text)

  def updateSerialNumber(self):
    # yayyy! another function that requires root privileges, and/or cache-ing
    serial_text = self.ui.Serial.text()

    try:
      serial = open('/sys/devices/virtual/dmi/id/product_serial', 'r').read().strip() # Note: this requires root or sudo
      # and now the error should happen instantly because we are opening the file using native methods
      # so that means we can cache the serial number because yes
      cache = open('/var/cache/qtfetch', 'r+')

      if len(cache.read().strip().split('\n')) == 2:
        cache.write(serial + '\n') # add the serial to cache

      elif len(cache.read().strip().split('\n')) == 3:
        contents = cache.read().strip().split('\n') # read the file
        open('/var/cache/qtfetch', 'w').close() # clear it
        cache.write(contents[0] + '\n') # rewrite line 1
        cache.write(contents[1] + '\n') # rewrite line 2
        cache.write(serial + '\n') # update serial number
    except Exception as e:
      print(e, '- attempting to fetch value from cached data')
      try:
        cache = open('/var/cache/qtfetch', 'r').read().strip().split('\n')
        serial = cache[2]

      except Exception as e:
        print(e)
        serial = 'Unknown'
    
    serial_text = serial_text.replace('$serialNumber', serial)

    self.ui.Serial.setText(serial_text)

  def updateIcon(self):
    
    icon_text = self.ui.OSIcon.text()

    icon_text = icon_text.replace('big_sur', 'catalina')

    self.ui.OSIcon.setText(icon_text)
    




def main():
  app = QApplication(sys.argv)
  form = SystemInfo()
  form.show()
  app.exec_()

if __name__ == '__main__':
  main()
