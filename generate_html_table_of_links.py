
with open("output.txt", "w") as f:
    for n in range(1, 1043):
        line = f'<li><a href="https://collections.slsa.sa.gov.au/collection/Acre+{n}+Collection">Acre {n} Collection</a></li>'
        f.write(f"        {line}\n")