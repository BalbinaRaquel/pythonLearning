idade: int
salario: float
nome: str
sexo: str

print()

idade = 32
salario = 23900.0
nome = "Balbina Raquel Correia"
sexo = "F"

print(f"A funcionaria {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")
print()

print("A funcionaria {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos".format(nome, sexo, salario, idade))

