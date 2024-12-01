# Calculator

Ce dépôt a été créé à des fins pédagogiques. Il permet de s'entraîner à l'utilisation de git-flow tout comme à s'initier à la programmation orientée objet.

## Comment débuter l'évaluation

* "Clone" le dépôt à l'aide de PyCharm.
* Exécuter-le pour valider que le programme actuel fonctionne bien sur votre environnement.
* Activer git flow pour créer la branche "develop".

```
  git flow init
```

## TODO

Objectifs:

Appliquer les concepts git-flow et POO à notre projet "Calculator".

### Tâche 01 - Identifier les futurs objets

Prenez le temps de bien comprendre l'exemple de code livré dans la théorie (vehicle and driver) et tentez d'identifier les objets dont nous aurions besoin pour modéliser correctement la calculatrice.

### Tâche 02 - Dessiner le diagramme de classe

Etat de l'architecture avant la modification

//add commit

Etat de l'architecture pour l'implémentation d'une classe "MathRequest"

![classDiagramWithMathRequest](docs/class_diagram.png)

## Tâche 03 - Récupérer/Préparer votre projet

Avant de partir la "tête la première", il est important d'avoir une bonne stratégie de branche et d'enrichir petit à petit votre code.
Vous pouvez soit partir du code actuel, soit partir de ce dépôt:

* Soit vous décider de "re-forcker-cloner" ce dépôt, et initaliser git-flow.
* Soit vous pouvez continuer sur votre code. Prenez bien soin de détecter les éventuelles différences que vous avez avec cette version du projet.

Comme vous pouvez le voir, la modification de l'architecture (le diagramme de classe) a été réalisé sur la branche develop. Il est important d'être sur cette branche avant de continuer le travail.

## Tâche 04 - Ouvrez la branche dédiée au développement de "MathRequest"

Il s'agit maintenant d'implémenter cette modification sur la branche du nom de "feature/MathRequest".

```
   git flow feature start MathRequest
```

Regardez l'architecture imposée et tentez de réussir à faire fonctionner votre calculatrice, avec l'implémentation de MathRequest.

