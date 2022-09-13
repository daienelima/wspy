produtos = ["Notebook", "Smartphone", "Teste"]

with open("produtos.txt", "w") as writer:
    for produtos in produtos:
        writer.write(produtos + '\n')