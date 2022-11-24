from mcstatus import JavaServer
import multiprocessing
from concurrent.futures import TimeoutError




file = open("resultips.txt", 'r')
lines = file.readlines()
sublists = []

start = 0;
end = len(lines)
step = 688;


def task(list, i):
    servers = []
    for l in list:
        try:
            server = JavaServer.lookup(l + ":25565")
            print("Testing "  + l)
            status = server.status();
            #if "1.19.2" in status.version.name: 
            s = "ip: " + l.replace("\n","") + " ver: " + status.version.name + "  desc: " + status.description + "  players: " + str(status.players.online)# + " favicon: " + status.favicon 
            servers.append(s);
        except TimeoutError: 
            print("Timed out")
        except Exception as e:
            print(e)

    with open('servers' + str(i) + '.txt', 'w') as f:
        for line in servers:
            try:
                f.write("%s\n" % line)
            except:
                print("encoding error")

if __name__ == '__main__':
    
    for i in range(start, end, step):
        x = i
        sublists.append((lines[x:x+step]))
    
    processes = [multiprocessing.Process(target=task, args=[list, sublists.index(list)]) 
                for list in sublists]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
    for i in range(0, 10):
        sublists.append(lines[i:i+1])
    
   #task(sublists[0])
    
   #for l in servers:
    #    print(l)

   
        
        
