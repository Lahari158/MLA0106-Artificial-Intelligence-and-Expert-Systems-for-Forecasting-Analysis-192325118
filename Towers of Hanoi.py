def hanoi(n, source, aux, dest):
    if n == 1:
        print(f"Move disk 1 from {source} to {dest}")
        return
    hanoi(n-1, source, dest, aux)
    print(f"Move disk {n} from {source} to {dest}")
    hanoi(n-1, aux, source, dest)

n = 3
hanoi(n, 'A', 'B', 'C')
