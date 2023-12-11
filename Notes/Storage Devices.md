# Storage Devices

## Magnetic Hard Disk

* **Disk block** is a logical unit for storage allocation and retrieval
  * 4 to 16 kilobytes typically
    * Smaller blocks: more transfers from disk
    * Larger blocks: more space wasted due to partially filled blocks
* **Sequential access pattern**
  * Successive requests are for successive disk blocks
  * Disk seek required only for first block
* **Random access pattern**
  * Successive requests are for blocks that can be anywhere on disk
  * Each access requires a seek
  * Transfer rates are low since a lot of time is wasted in seeks
* **I/O operations per second (IOPS)**
  * Number of random block reads that a disk can support per second
  * 50 to 200 IOPS on current generation magnetic disks







### Example

* Consider the following numbers
  * Seek time = 7 ms
  * Rotational Latency = 5ms
  * Data transfer rate = 50 MB per second      (megabye)

* Reading one 4KB block
  * Time = $\frac{4K}{50M}= 0.078125 ms $(1/100 times of seek/rotation)
* So $reading\  one\  block = 7 + 5 + 0.078125ms = 12.078125ms$
* Reading 10 consecutive blocks same track $= 7 + 5 + 10 \times 0.078125 = 12.78125ms$
* Reading 10 blocks on different tracks = $10 \times (7 + 5 + 0.078125) = 120.78125ms$

> And you'd by say every microsecond car. If you are not doing fine carefully here, if you give me this number yourself, this you are dead. 





### Implication

* Data that are accessed together should be store “adjacent”

  * Within the same track at the minimum

  * Usually means that each table is to be stored in a file
    * Operating Systems has tools to “defragment” the files

* Data that is accessed often should be put into memory

  * Buffering

> Now these are all done behind the scene and an automatic, more important data need to be buffer and data need to be buffer correctly.
>
> So how to manage those buffers become a big, big deal in database systems.



### **Mean time to failure (MTTF)** 

**Mean time to failure (MTTF)** :the average time the disk is expected to run continuously without any failure.

> That means how long do you think your hot this will run before it crash

* Typically 3 to 5 years
* Probability of failure of new disks is quite low, corresponding to a
   “theoretical MTTF” of 500,000 to 1,200,000 hours for a new disk
  * E.g., an MTTF of 1,200,000 hours for a new disk means that given 1000 relatively new disks, on an average one will fail every 1200 hours

* MTTF decreases as disk ages





## Flash Storage

* Non-volatile storage
* Evolved from EPROM/EEPROM
* Each unit is a ==“gate”==
* Storage can be set (to 1) by passing electricity to form a second gate in the structure – that is stable
* Applying electricity in different way can “erase” the bit and allow it to be rewritten again
  * Erase first, than rewrite
* Two types of flash – ==NAND== and NOR (based on the logic used to set the bit)
* NAND bit are cheaper and more scalable as mass storage
  * However, slower but **have to be erased in blocks**
  * **Each time a block need to be erased before** 



## NAND-based storage

* NAND flash 
  * used widely for storage, cheaper than NOR flash
  * requires page-at-a-time read (page: 512 bytes to 4 KB)
    * 20 to 100 microseconds for a page read
    * Not much difference between sequential and random read
    * Slower than RAM, but faster than the hard disk
  * Page can only be written once
    * Must be erased to allow rewrite
  * Solid state disks 
    * Use standard block-oriented disk interfaces, but store data on multiple flash storage devices internally
    * Transfer rate of up to 500 MB/sec using SATA, and 
       up to 3 GB/sec using NVMe PCIe