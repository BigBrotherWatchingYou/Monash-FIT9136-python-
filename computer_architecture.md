# OS 
- File mangement
- memory management
### process management
when something is in the memonry ( for example look at your task manager , those which occupate your cpu)
-  what is a process? it is a programm in management

## Cpu
memory in Cpu is called " register"
- context 

## FIFO- fast in and fast out
- who came first who execute first


## LRU - least recently used
- only need to check the input, dontchare about what's already there

## non-pre-emptive scheduling algorithms:
- e.g.First-in first-out, Shortest job first, Priority
scheduling

### Round-robin scheduling


## Deadlock
- when two processors want to use a shared resources
------check     


## Hard link
it still workd even the file does not exist 
## soft link
shortcut

# command
## touch 
create a file-- touch aaa.txt
## pico
edit a file -- pico touch aaa.txt
after finisthed editing, press ctrl+x , and press Enter to quit

## search
ls -l *.txt
search for files ended with .txt

## softlink
ln -s original.txt original_softlink.txt

# i
ls -i *.txt
ls -il *.txt


# encapsulation 
# decapsulation
# multiplexing 
# Demultiplexing

# logical connecton
# physical connection
# MAC address(48 bit)
Hex: 10:FA:5F:F0:01

# IP address
- 139.108.111.95
## IP address V4( IPV4)
32 bit

# Port ID-(16 bit)
- on layer4
# URL
- URL belongs to server, and is only for the server
e.g. my.monash.edu

![1723443383903](image/computer_architecture/1723443383903.png)

![1723443394787](image/computer_architecture/1723443394787.png)

# data passing process
![1723445006223](image/computer_architecture/1723445006223.png)
![1723445011307](image/computer_architecture/1723445011307.png)
![1723445149955](image/computer_architecture/1723445149955.png)
# multiplexiv


# demultiplexiv

# Message Encapsulation (all layers)
## Application 
Protocol Data: message
address: Names
 ---HTTP www.youtube.com
## Transport 
Protocol Data: Segment/User datagram
address: port numbers
---TCP
## Network 
Protocol Data: Packet
packet names: datagram
address: 
--IP 
## Data Link
Protocol Data: Frame
--Eternet
## Physical
Protocol Data: Bit
-- Encoded binary bits ....01010..

# encap/decap process
to both sender and receiver
![1723707684726](image/computer_architecture/1723707684726.png)
![1723707701613](image/computer_architecture/1723707701613.png)

# Multiplexing and De-mltiplexing
to both sender and receiver
![1723707805582](image/computer_architecture/1723707805582.png)


# commands
## www.xxx.com
- https, application layer
## nslookup www.monash.edu
- it returns:
Name: www.google.com
Address: 172.217.167.68
## ifconfig -a
shows all hardware-address , networkaddress.etc
( in modern computer ther's no collisions)
## ping www.monash.edu
--ping -i 0.3 -w 1
## traceroute www.onlyfans.com
----traceroute -l ---resolve-hostnames

## unzip xxxx.zip

### Total FRAME size :
eternet header+ ip header+ TCP header+ Http header


# Repeaters
repeaters regenerate signals
which allows communications across greater distance

# Hube
-are simply multi-port repeaters
- facilitates scaling communication between additional hosts
- everyone receives everyone else's data

# Bridge 
sit between hub-connected hosts
bridges only have two ports
Bridges learn which hosts are on each side