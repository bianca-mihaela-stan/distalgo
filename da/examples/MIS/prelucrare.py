#%%
import re
import math

luby_dir = "/home/bianca/licenta/distalgo/da/examples/MIS/lubys_stats"
ghaffari_dir = "/home/bianca/licenta/distalgo/da/examples/MIS/ghaffari_stats"

luby_time_results = luby_dir + "/node_time_results"
ghaffari_time_results = ghaffari_dir + "/node_time_results"
number_of_runs_per_graph = 3

sizes = [100]

luby_averages = {}
ghaffari_averages = {}
luby_rounds = {}
ghaffari_rounds = {}
for size in sizes:
    luby_averages[size] = []
    ghaffari_averages[size] = []
    for i in range(10):
        luby_documents = [luby_time_results + f"/{size}" + f"/graph{i}" + f"/run{x}_node_time_results.txt" for x in range(number_of_runs_per_graph)]
        luby_total_time_documents = []
        for document in luby_documents:
            start_time = math.inf    
            finish_time = -math.inf
            
            f = open(document)
            line = f.readline()
            while line:
                numbers = line.strip()
                numbers = [float(x) for x in re.split(r' |,|:', numbers) if x != '']
                numbers[0] = int(numbers[0])
                node = numbers[0]
                node_starts = numbers[1]
                node_finishes = numbers[2]
                total_node = numbers[3]
                rounds = numbers[4]
                
                start_time = min(start_time, node_starts)
                finish_time = max(finish_time, node_finishes)
                if math.isinf(-finish_time):
                    print(f"wtf is going on here {finish_time} {node_finishes}")
                line = f.readline()
                
            total_time = finish_time - start_time
            luby_total_time_documents.append(total_time)
        
        luby_average_time = sum(luby_total_time_documents)/len(luby_total_time_documents)
        
        luby_averages[size].append(luby_average_time)
        
        ghaffari_documents = [ghaffari_time_results + f"/{size}" + f"/graph{i}" + f"/run{x}_node_time_results.txt" for x in range(number_of_runs_per_graph)]
        ghaffari_total_time_documents = []
        for document in ghaffari_documents:
            start_time = math.inf    
            finish_time = -math.inf
            
            f = open(document)
            line = f.readline()
            while line:
                numbers = line.strip()
                numbers = [float(x) for x in re.split(r' |,|:', numbers) if x != '']
                numbers[0] = int(numbers[0])
                node = numbers[0]
                node_starts = numbers[1]
                node_finishes = numbers[2]
                total_node = numbers[3]
                
                start_time = min(start_time, node_starts)
                finish_time = max(finish_time, node_finishes)
                if math.isinf(-finish_time):
                    print(f"wtf is going on here {finish_time} {node_finishes}")
                line = f.readline()
                
            total_time = finish_time - start_time
            ghaffari_total_time_documents.append(total_time)
        
        ghaffari_average_time = sum(ghaffari_total_time_documents)/len(ghaffari_total_time_documents)
        
        ghaffari_averages[size].append(ghaffari_average_time)
        
        
        
print(luby_averages)
print(ghaffari_averages)

x = [x for x in range (0,10)]
print(x)
# %%
sizes = [1000]
for size in sizes:
    luby_averages[size] = []
    ghaffari_averages[size] = []
    for i in range(10):
        luby_documents = [luby_time_results + f"/{size}" + f"/graph{i}" + f"/run{x}_node_time_results.txt" for x in range(number_of_runs_per_graph)]
        luby_total_time_documents = []
        for document in luby_documents:
            start_time = math.inf    
            finish_time = -math.inf
            
            f = open(document)
            line = f.readline()
            while line:
                numbers = line.strip()
                numbers = [float(x) for x in re.split(r' |,|:', numbers) if x != '']
                numbers[0] = int(numbers[0])
                node = numbers[0]
                node_starts = numbers[1]
                node_finishes = numbers[2]
                total_node = numbers[3]
                
                start_time = min(start_time, node_starts)
                finish_time = max(finish_time, node_finishes)
                if math.isinf(-finish_time):
                    print(f"wtf is going on here {finish_time} {node_finishes}")
                line = f.readline()
                
            total_time = finish_time - start_time
            luby_total_time_documents.append(total_time)
        
        luby_average_time = sum(luby_total_time_documents)/len(luby_total_time_documents)
        
        luby_averages[size].append(luby_average_time)
        
        ghaffari_documents = [ghaffari_time_results + f"/{size}" + f"/graph{i}" + f"/run{x}_node_time_results.txt" for x in range(number_of_runs_per_graph)]
        ghaffari_total_time_documents = []
        for document in ghaffari_documents:
            start_time = math.inf    
            finish_time = -math.inf
            
            f = open(document)
            line = f.readline()
            while line:
                numbers = line.strip()
                numbers = [float(x) for x in re.split(r' |,|:', numbers) if x != '']
                numbers[0] = int(numbers[0])
                node = numbers[0]
                node_starts = numbers[1]
                node_finishes = numbers[2]
                total_node = numbers[3]
                rounds = numbers[4]
                
                start_time = min(start_time, node_starts)
                finish_time = max(finish_time, node_finishes)
                if math.isinf(-finish_time):
                    print(f"wtf is going on here {finish_time} {node_finishes}")
                line = f.readline()
                
            print(f"start time {start_time}")
            print(f"finish time {finish_time}")
                
            total_time = finish_time - start_time
            ghaffari_total_time_documents.append(total_time)
        
        ghaffari_average_time = sum(ghaffari_total_time_documents)/len(ghaffari_total_time_documents)
        
        ghaffari_averages[size].append(ghaffari_average_time)
        
        
print(ghaffari_averages[1000])
# %%
import matplotlib.pyplot as plt
#%%

x = [f"G{x}" for x in range (0,10)]
print(x)
plt.plot(x, luby_averages[100], label = "Luby", color = "green", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "blue", markersize= 7)
plt.plot(x, ghaffari_averages[100], label = "Ghaffari", color = "pink", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "red", markersize= 7)

plt.xlabel("Graful")
plt.ylabel("Timpul de rulare (s)")
plt.title("Compararea timpului de rulare al celor doi algoritmi")

plt.legend()
plt.show()

# %%
x = [f"G{x}" for x in range (0,10)]
print(x)
plt.plot(x, luby_averages[1000], label = "Luby", color = "green", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "blue", markersize= 7)
plt.plot(x, ghaffari_averages[1000], label = "Ghaffari", color = "pink", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "red", markersize= 7)

plt.xlabel("Graful")
plt.ylabel("Timpul de rulare (s)")
plt.title("Compararea timpului de rulare al celor doi algoritmi")

plt.legend()
plt.show()

#%%
sizes = [1000, 100]
luby_rounds = {}
ghaffari_rounds = {}
luby_averages_rounds = {}
ghaffari_averages_rounds = {}
for size in sizes:
    luby_averages_rounds[size] = []
    ghaffari_averages_rounds[size] = []
    ghaffari_averages[size] = []
    for i in range(10):
        luby_documents = [luby_time_results + f"/{size}" + f"/graph{i}" + f"/run{x}_node_time_results.txt" for x in range(number_of_runs_per_graph)]
        rounds_documents = []
        for document in luby_documents:
            max_rounds = -math.inf
            
            f = open(document)
            line = f.readline()
            while line:
                numbers = line.strip()
                numbers = [float(x) for x in re.split(r' |,|:', numbers) if x != '']
                rounds = numbers[4]
                
                max_rounds = max(max_rounds, rounds)
                line = f.readline()
                
            
            rounds_documents.append(max_rounds)
        
        luby_average_rounds = sum(rounds_documents)/len(rounds_documents)
        
        luby_averages_rounds[size].append(luby_average_rounds)
        
        ghaffari_documents = [ghaffari_time_results + f"/{size}" + f"/graph{i}" + f"/run{x}_node_time_results.txt" for x in range(number_of_runs_per_graph)]
        rounds_documents = []
        for document in ghaffari_documents:
            max_rounds = -math.inf
            
            f = open(document)
            line = f.readline()
            while line:
                numbers = line.strip()
                numbers = [float(x) for x in re.split(r' |,|:', numbers) if x != '']
                rounds = numbers[4]
                
                max_rounds = max(max_rounds, rounds)
                line = f.readline()
                
            
            rounds_documents.append(max_rounds)
        
        ghaffari_average_rounds = sum(rounds_documents)/len(rounds_documents)
        
        ghaffari_averages_rounds[size].append(ghaffari_average_rounds)
        
        
print(luby_averages_rounds)
print(ghaffari_averages_rounds)
# %%
x = [f"G{x}" for x in range (0,10)]
print(x)
plt.plot(x, luby_averages_rounds[100], label = "Luby", color = "green", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "blue", markersize= 7)
plt.plot(x, ghaffari_averages_rounds[100], label = "Ghaffari", color = "pink", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "red", markersize= 7)

plt.xlabel("Graful")
plt.ylabel("Numarul de runde")
plt.title("Compararea numarului de runde")

plt.legend()
plt.show()

#%%
x = [f"G{x}" for x in range (0,10)]
print(x)
plt.plot(x, luby_averages_rounds[1000], label = "Luby", color = "green", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "blue", markersize= 7)
plt.plot(x, ghaffari_averages_rounds[1000], label = "Ghaffari", color = "pink", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "red", markersize= 7)

plt.xlabel("Graful")
plt.ylabel("Numarul de runde")
plt.title("Compararea numarului de runde")

plt.legend()
plt.show()
# %%
sizes = [1000, 100]
luby_size_rounds = {}
ghaffari_size_rounds = {}
for size in sizes:
    luby_size_rounds[size] = {}
    ghaffari_size_rounds[size] = {}
    i = 0
    luby_documents = [luby_time_results + f"/{size}" + f"/graph{i}" + f"/run{x}_node_time_results.txt" for x in range(number_of_runs_per_graph)]
    document = luby_documents[0]
    f = open(document)
    line = f.readline()
    while line:
        numbers = line.strip()
        numbers = [float(x) for x in re.split(r' |,|:', numbers) if x != '']
        index = numbers[0]
        rounds = int(numbers[4])
        
        if rounds in luby_size_rounds[size]:
            luby_size_rounds[size][rounds] += 1
        else:
            luby_size_rounds[size][rounds] = 1
        line = f.readline()
    
    ghaffari_documents = [ghaffari_time_results + f"/{size}" + f"/graph{i}" + f"/run{x}_node_time_results.txt" for x in range(number_of_runs_per_graph)]
    document = ghaffari_documents[0]
    f = open(document)
    line = f.readline()
    while line:
        numbers = line.strip()
        numbers = [float(x) for x in re.split(r' |,|:', numbers) if x != '']
        index = numbers[0]
        rounds = int(numbers[4])
        
        if rounds in ghaffari_size_rounds[size]:
            ghaffari_size_rounds[size][rounds] += 1
        else:
            ghaffari_size_rounds[size][rounds] = 1
        line = f.readline()
        
print(luby_size_rounds)
print(ghaffari_size_rounds)
# %%
x_luby = [x[0] for x in luby_size_rounds[1000].items()]
y_luby = [x[1] for x in luby_size_rounds[1000].items()]

x_ghaffari = [x[0] for x in ghaffari_size_rounds[1000].items()]
y_ghaffari = [x[1] for x in ghaffari_size_rounds[1000].items()]

x_ghaffari, y_ghaffari = (list(t) for t in zip(*sorted(zip(x_ghaffari, y_ghaffari))))

while len(x_ghaffari) > len(x_luby):
    x_luby.append(x_luby[-1] + 1)
    
while len(y_ghaffari) > len(y_luby):
    y_luby.append(0)

plt.plot(x_luby, y_luby, label = "Luby", color = "green", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "blue", markersize= 7)
plt.plot(x_ghaffari, y_ghaffari, label = "Ghaffari", color = "pink", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "red", markersize= 7)

plt.xlabel("Runda")
plt.ylabel("Numarul de noduri")
plt.title("Performanta locala")

plt.legend()
plt.show()
# %%
# %%
