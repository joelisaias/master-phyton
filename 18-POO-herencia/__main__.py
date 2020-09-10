import clases

persona=clases.Persona()
persona.setNombres("Joel")
persona.setApellidos("Alvarado")
persona.setEdad(31)
persona.setAltura("175cm")

print(f"La persona es {persona.getNombres()} {persona.getApellidos()}")
informatico=clases.Informatico()
informatico.setNombres("Isaias")
informatico.setApellidos("Torres")
informatico.setEdad(30)
informatico.setAltura("175cm")

print(f"La informatico es {informatico.getNombres()} {informatico.getApellidos()}")
print(f"La informatico sabe {informatico.getLenguajes()}")
print(informatico.programar())
print(informatico.hablar())
print(informatico.dormir())