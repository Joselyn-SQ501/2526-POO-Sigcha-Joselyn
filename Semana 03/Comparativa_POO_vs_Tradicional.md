# 📊 Comparación entre Programación Tradicional y Programación Orientada a Objetos (POO)

## 📌 Introducción

En el ámbito del desarrollo de software, los paradigmas de programación constituyen modelos fundamentales para estructurar y resolver problemas computacionales. Entre los paradigmas más utilizados se encuentran la Programación Tradicional (o estructurada) y la Programación Orientada a Objetos (POO), los cuales difieren principalmente en la forma en que organizan el código, gestionan los datos y permiten la escalabilidad de los sistemas.

La programación tradicional se basa en una ejecución secuencial de instrucciones y en la división del programa en funciones que realizan tareas específicas. Este enfoque prioriza la claridad del flujo lógico y es comúnmente utilizado en problemas simples o de tamaño reducido (Python Software Foundation, 2023). Por otro lado, la Programación Orientada a Objetos propone una forma más abstracta y modular de desarrollo, en la cual los problemas se modelan a partir de objetos que integran datos y comportamientos (Salinas et al., 2025).

En esta tarea práctica se implementan ambos enfoques utilizando el lenguaje Python para resolver un mismo problema: el cálculo del promedio semanal del clima. Esto permite realizar una comparación directa entre ambos paradigmas y analizar sus ventajas y desventajas desde una perspectiva práctica.

## 🎯 Objetivo

Desarrollar habilidades prácticas en la Programación Tradicional y la Programación Orientada a Objetos (POO) mediante la implementación de un programa en Python para determinar el promedio semanal del clima.

## 🧩 Descripción de la tarea

Un programa que solicita al usuario el ingreso de las temperaturas correspondientes a los siete días de la semana y calcula el promedio semanal del clima. El mismo es resuelto aplicando dos paradigmas de programación distintos para facilitar su comparación.

## 🧠 Desarrollo

### 🔹 Programación Tradicional

En el programa basado en programación tradicional, el programa se divide en funciones independientes que permiten ingresar las temperaturas diarias y calcular el promedio semanal. Los datos se almacenan en estructuras simples como listas y se procesan mediante un flujo de ejecución secuencial.

Este enfoque se caracteriza por su simplicidad y facilidad de comprensión, lo que lo convierte en una alternativa adecuada para programas pequeños. Según la documentación oficial de Python (Python Software Foundation, 2023), la programación estructurada sigue siendo una base importante para comprender la lógica computacional antes de abordar paradigmas más complejos.

### 🔹 Programación Orientada a Objetos (POO)

En la versión orientada a objetos, el programa se estructura mediante una clase que representa la información de la temperatura semanal. Esta clase encapsula las temperaturas y los métodos necesarios para su ingreso y cálculo de promedio, aplicando principios fundamentales de la POO como el encapsulamiento y la abstracción.

Este paradigma permite modelar el problema de una forma más cercana a la realidad, facilitando la extensión del programa y la reutilización del código. De acuerdo con Salinas et al. (2025), la POO resulta especialmente eficaz en sistemas que requieren mantenimiento continuo o crecimiento progresivo.

## 📊 Análisis Comparativo

Desde el punto de vista de la organización del código, la programación tradicional presenta una estructura funcional y directa. Sin embargo, a medida que el programa aumenta su tamaño, esta organización puede volverse difícil de mantener, ya que las funciones y variables tienden a dispersarse. En contraste, la Programación Orientada a Objetos agrupa los datos y comportamientos relacionados dentro de clases, lo que mejora la legibilidad y el orden del código (Salinas et al., 2025).

En relación con la reutilización del código, la programación tradicional ofrece opciones limitadas, puesto que las funciones suelen estar diseñadas para contextos específicos. En cambio, la POO facilita la reutilización mediante la creación de clases que pueden ser instanciadas o extendidas en otros programas, reduciendo la duplicación de código (Phillips, 2021).

Respecto a la escalabilidad, la programación tradicional es adecuada para aplicaciones pequeñas, pero presenta dificultades al intentar añadir nuevas funcionalidades. La POO, por su parte, permite una expansión más controlada del sistema, ya que nuevas características pueden incorporarse sin afectar significativamente la estructura existente (Python Software Foundation, 2023).

Finalmente, en cuanto a la facilidad de aprendizaje, la programación tradicional resulta más accesible para principiantes debido a su menor nivel de abstracción. No obstante, aunque la POO requiere un mayor esfuerzo inicial, su dominio permite desarrollar aplicaciones más robustas y mantenibles a largo plazo.

## ✅ Ventajas y Desventajas

La Programación Tradicional destaca por su simplicidad y claridad, lo que facilita su comprensión y aplicación en problemas sencillos. Sin embargo, su principal limitación radica en la dificultad para mantener y escalar el código cuando los proyectos crecen en tamaño y complejidad.

Por otro lado, la programación Orientada a Objetos ofrece una estructura más organizada y modular, favoreciendo la reutilización y el mantenimiento del software. Aunque su curva de aprendizaje es mayor, este paradigma resulta más adecuado para proyectos medianos y grandes, donde la extensibilidad y la claridad del diseño son fundamentales (Phillips, 2021).

Estas diferencias ilustran cómo cada paradigma ofrece ventajas según el tipo de problema: la programación tradicional o funcional puede ofrecer mayor predictibilidad y facilidad de prueba, mientras que la POO facilita la abstracción y la organización en aplicaciones con estructuras ricas de datos (Powell, 2024).

## 🧩 Conclusiones

La comparación realizada demuestra que ambos paradigmas permiten resolver correctamente el problema del cálculo del promedio semanal del clima. No obstante, la Programación Orientada a Objetos ofrece ventajas significativas en términos de organización, reutilización y escalabilidad, lo que la convierte en una opción más adecuada para desarrollos complejos.

La Programación Tradicional continúa siendo una herramienta valiosa para problemas simples y para la enseñanza de los fundamentos de la programación. En conclusión, la elección del paradigma dependerá del contexto del proyecto y de los objetivos del desarrollo del software.

## 📚 Bibliografía

Powell, R. (16 de abril de 2024). *Programación funcional vs programación orientada a objetos (POO)*. circleci. https://circleci.com/blog/functional-vs-object-oriented-programming/

Phillips, D. y Lott, S. (2021). *Python 3 object-oriented programming* (4th ed.). Packt Publishing. https://www.oreilly.com/library/view/python-object-oriented-programming/9781801077262/

Python Software Foundation. (2023). *Python documentation*. [https://docs.python.org/3/](https://docs.python.org/3/)

Salinas Copo, A. M., Tarquino Vinueza Rodríguez, L., Valdiviezo Rodríguez, J. G., Villa López, R. O., Guevara Aulestia, D. L., Urquizo Alvarez, C. E., Moya Ibarra, D. E., y Espín Mendoza, I. V. (2025). *Fundamentos de programación orientada a objetos (POO)*. CIDE Editorial. https://repositorio.cidecuador.org/bitstream/123456789/3182/3/LIBRO%20DE%20PROGRAMACI%C3%93N%20ORIENTADA%20A%20OBJETOS.pdf







