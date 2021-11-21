import time as t
from datetime import datetime, time



host_path= 'C:\\Windows\\System32\\drivers\\etc\\'
# host_path= ''
redirect = "127.0.0.1"
black_list = ["www.facebook.com",
              "facebook.com",
              "9gag.com",
              "www.9gag.com",
              "korrespondent.net",
              "www.korrespondent.net",
              "www.pravda.com.ua",
              "pravda.com.ua",
              "www.reddit.com",
              "reddit.com"]

def get_block_line(redirect, host):
    return redirect+" "+host

def is_host_blocking(black_list):
    with open(host_path+"hosts", "r") as f:
        lines = f.readlines()
        for host in black_list:
            block_line = get_block_line(redirect, host)
            blocking_host = False
            for line in lines:
                if line.find(block_line)!=-1:
                    blocking_host = True
            if not blocking_host:
                return False
    return True

def clear_block():
    file_lines=[]
    new_lines=[]
    with open(host_path+"hosts", "r") as f:
        file_lines = f.readlines()
        f.close()
    for line in file_lines:
        site_found = False
        for host in black_list:
            block_line = redirect + " " + host
            if line.find(block_line) != -1:
                site_found = True
        if not site_found:
            new_lines.append(line)
    with open(host_path + "hosts", "w") as f:
        f.writelines(new_lines)
        f.close()

def block_bl():
    clear_block()
    bl_lines=[]
    for site in black_list:
        bl_lines.append(redirect+" "+site+"\n")
    with open(host_path + "hosts", "a") as f:
        f.writelines(bl_lines)
        f.close()

while True:
    t.sleep(600)
    start_time = time(7,0)
    # print(type(start_time))
    # print(start_time)
    end_time= time(18,0)
    current_time = datetime.now().time()
    # check if  host file blocks sites
    block_active = is_host_blocking(black_list)
    # check time
    if current_time >= start_time and current_time <= end_time:
        if not block_active:
            print("blocking...")
            block_bl()
    else:
        if block_active:
            print("unblocking...")
            clear_block()



