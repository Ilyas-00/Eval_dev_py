class Disk:
    def __init__(self, total, used):
        self.total = total
        self.used = used
    
    
    @property
    def free(self):
        return self.total - self.used


    @property
    def used_perc(self):
        return self.used / self.total

    
    def __repr__(self):
        return f"Disk[total: {self.total} Gb, used: {self.used} Gb]"

   
    def __lt__(self, other):
        return self.used_perc < other.used_perc


if __name__ == '__main__':
    disk1 = Disk(total=50, used=10)
    disk2 = Disk(total=100, used=30)
    disk3 = Disk(total=200, used=50)
    disk4 = Disk(total=80, used=20)

    print(disk1.free)  
    print(disk2.free)  
    print(disk3.free)  
    print(disk4.free) 

    print(disk1.used_perc)  
    print(disk2.used_perc)  
    print(disk3.used_perc) 
    print(disk4.used_perc)  

    disks = [disk1, disk2, disk3, disk4]

   
    disks_sorted = sorted(disks)
    print(disks_sorted)  
