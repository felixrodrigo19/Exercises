# A partir da listagem dos alunos matriculados em duas disciplinas, determine quais são os alunos matriculados nas duas disciplinas ao mesmo tempo.

curso_1 = {
  "joão",
  "Medestein",
  "Schwinterschlfels",
  "Seleystadt",
  "Generuck",
  "Elior",
  "Valondek",
  "Forlinde",
  "Linione",
  "diablo"
  }

curso_2 = {
  "Seleystadt",
  "Karningion",
  "Hellarest",
  "Mithlonde",
  "Valondek",
  "Forlinde",
  "Linione",
  "Brodon",
  "Wehill"
}


for x in curso_1:
  for y in curso_2:
    if x in y:
      nome = [x]
      print(nome)
 
