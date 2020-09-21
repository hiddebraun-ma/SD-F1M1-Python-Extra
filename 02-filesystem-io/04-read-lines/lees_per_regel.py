# Bestand in read-only (r) mode openen (wel zo veilig, wegaan niets schrijven)
bestand = open("klasgenoten.txt", "r")

# Een tekst naar het bestand schrijven
regel1 = bestand.readline()
print(regel1)

regel2 = bestand.readline()
print(regel2)

regel3 = bestand.readline()
print(regel3)

# Enzovoorts
