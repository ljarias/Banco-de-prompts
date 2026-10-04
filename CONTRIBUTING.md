# 🤝 Cómo contribuir al Banco de Prompts

Gracias por querer mejorar este repositorio.

La meta es aprender dos cosas al mismo tiempo: **usar mejor la IA** y **colaborar con Git y GitHub**.

## 1. Qué puedes aportar

Puedes proponer:

- un prompt nuevo;
- una mejora a un prompt existente;
- un ejemplo de uso;
- un tip descubierto durante una práctica;
- una advertencia sobre un error frecuente;
- una técnica para verificar respuestas de IA;
- una nueva categoría, si hace falta.

## 2. Condición principal

Antes de proponer un prompt, **debes probarlo**.

No aceptamos como aporte final un prompt creado por una IA y copiado sin evaluación.

Tu contribución debe explicar qué ocurrió cuando lo usaste.

## 3. Usa un Fork

1. Abre el repositorio Banco-de-prompts.
2. Pulsa **Fork**.
3. Clona tu copia.

~~~bash
git clone https://github.com/TU-USUARIO/Banco-de-prompts.git
cd Banco-de-prompts
~~~

Agrega el repositorio oficial:

~~~bash
git remote add upstream https://github.com/ljarias/Banco-de-prompts.git
~~~

Comprueba:

~~~bash
git remote -v
~~~

## 4. Actualiza antes de trabajar

~~~bash
git switch main
git pull upstream main
git push origin main
~~~

## 5. Crea una rama

No hagas tu aporte directamente en main.

~~~bash
git switch -c aporte/prompt-listas
git switch -c aporte/tip-git-status
git switch -c aporte/fotografia-nocturna
~~~

## 6. Dónde guardar el aporte

Elige la categoría que más se ajuste:

- prompts/aprendizaje/
- prompts/programacion/
- prompts/depuracion/
- prompts/proyectos/
- prompts/git-github/
- prompts/fotografia/
- prompts/videos/
- prompts/animacion/
- prompts/bases-de-datos/
- prompts/analisis-de-datos/
- prompts/visualizacion-de-datos/
- prompts/tips-genericos/

Usa nombres de archivo simples, en minúsculas y separados por guiones.

Ejemplo:

~~~text
prompts/bases-de-datos/normalizar-tablas.md
~~~

Puedes copiar la plantilla disponible en [plantillas/nuevo-prompt.md](plantillas/nuevo-prompt.md).

## 7. Revisa antes del commit

~~~bash
git status
git diff
git add .
git commit -m "Agrega prompt para normalizar tablas"
~~~

Un buen mensaje de commit explica qué cambió.

✅ Bueno: Agrega prompt para revisar consultas SQL

❌ Poco útil: cambios, tarea, actualización

## 8. Envía tu rama

~~~bash
git push -u origin aporte/nombre-corto
~~~

En los siguientes cambios de esa misma rama bastará:

~~~bash
git push
~~~

## 9. Abre el Pull Request

En GitHub abre un Pull Request desde tu rama hacia:

~~~text
ljarias/Banco-de-prompts → main
~~~

Describe qué agregaste, qué problema resuelve, cómo lo probaste y qué debería revisar quien lo use.

## 10. Si te piden cambios

No abras otro Pull Request. Ajusta la misma rama:

~~~bash
git add .
git commit -m "Mejora ejemplo del prompt"
git push
~~~

El Pull Request se actualizará automáticamente.

## 11. Criterios de calidad

Un aporte está listo cuando:

- tiene un propósito claro;
- puede reutilizarlo otra persona;
- indica qué partes deben personalizarse;
- fue probado;
- no incluye información sensible;
- no promete que la IA siempre tendrá razón;
- usa lenguaje claro;
- evita pedir que la IA haga todo el trabajo sin explicar;
- ayuda a aprender, comprobar o crear algo mejor.

## 12. Si aparece un conflicto

No borres archivos ni uses comandos destructivos por ensayo y error.

Primero revisa:

~~~bash
git status
git log --oneline --graph --all -10
~~~

Resolver un conflicto también es parte del aprendizaje.
