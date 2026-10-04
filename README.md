# 🤖 Banco de Prompts · INEM

Repositorio colaborativo para aprender a usar la inteligencia artificial como apoyo en programación, creación digital, análisis de datos y proyectos escolares.

La idea no es copiar respuestas. La idea es aprender a **preguntar mejor, probar, comparar, verificar y compartir lo que funciona**.

## 🎯 ¿Para qué sirve?

Este repositorio permite a los estudiantes:

- reutilizar prompts probados por otros compañeros;
- adaptar instrucciones a sus propios proyectos;
- aprender Git y GitHub en una situación real;
- documentar descubrimientos, errores y buenas prácticas;
- proponer nuevos prompts mediante Fork, rama, commit, push y Pull Request.

## 🗂️ Categorías

| Categoría | Para qué puede servir |
|---|---|
| [🧠 Aprendizaje](prompts/aprendizaje/) | Comprender conceptos, estudiar y practicar |
| [🐍 Programación](prompts/programacion/) | Crear, revisar y mejorar código |
| [🕵️ Depuración](prompts/depuracion/) | Entender errores y encontrar soluciones |
| [🚀 Proyectos](prompts/proyectos/) | Planear y desarrollar proyectos completos |
| [🌿 Git y GitHub](prompts/git-github/) | Trabajar con versiones, ramas y colaboración |
| [📷 Fotografía](prompts/fotografia/) | Composición, iluminación, análisis y planeación de fotos |
| [🎬 Videos](prompts/videos/) | Guion, storyboard, planos y producción |
| [🎞️ Animación](prompts/animacion/) | Secuencias, keyframes, motion y animaciones educativas |
| [🗄️ Bases de datos](prompts/bases-de-datos/) | Modelado, SQL y revisión de consultas |
| [🔎 Análisis de datos](prompts/analisis-de-datos/) | Limpieza, exploración e interpretación |
| [📊 Visualización de datos](prompts/visualizacion-de-datos/) | Gráficos, dashboards y comunicación visual |
| [💡 Tips genéricos](prompts/tips-genericos/) | Técnicas útiles para mejorar cualquier prompt |

Consulta el [índice completo de prompts](prompts/README.md).

## 🧩 Cómo usar un prompt

1. **Elige** un prompt relacionado con tu problema.
2. **Adáptalo**: cambia los campos entre corchetes por tu información.
3. **Pruébalo** con un caso real.
4. **Revisa** la respuesta de la IA. No asumas que todo es correcto.
5. **Mejóralo** si la respuesta fue confusa, incompleta o demasiado extensa.
6. **Documenta** lo que aprendiste.

Un buen prompt no reemplaza tu pensamiento. Te ayuda a organizarlo.

## 🤝 Cómo aportar

La forma recomendada es trabajar desde tu propio Fork.

~~~bash
# 1. Clona TU fork
git clone https://github.com/TU-USUARIO/Banco-de-prompts.git
cd Banco-de-prompts

# 2. Conecta el repositorio oficial
git remote add upstream https://github.com/ljarias/Banco-de-prompts.git

# 3. Actualiza main
git switch main
git pull upstream main
git push origin main

# 4. Crea una rama para tu aporte
git switch -c aporte/nombre-corto

# 5. Después de crear o modificar archivos
git status
git add .
git commit -m "Agrega prompt para ..."
git push -u origin aporte/nombre-corto
~~~

Después del push, abre un **Pull Request** desde tu Fork hacia este repositorio.

📘 Lee primero [CONTRIBUTING.md](CONTRIBUTING.md).

## ✅ Antes de proponer un prompt

Tu aporte debería responder estas preguntas:

- ¿Qué problema ayuda a resolver?
- ¿A quién le puede servir?
- ¿Qué debe cambiar el usuario antes de usarlo?
- ¿Fue probado con un caso real?
- ¿Qué aprendiste al probarlo?
- ¿La respuesta obtenida necesitó correcciones?

## 🧪 Regla del banco: probar antes de publicar

No queremos una colección de prompts generados automáticamente que nadie haya usado.

Queremos prompts que hayan pasado por este proceso:

**problema real → primer prompt → prueba → ajuste → nueva prueba → aprendizaje → aporte**

## 🔐 Uso responsable

- No publiques contraseñas, datos personales, documentos privados ni información sensible.
- Verifica datos, código, cálculos y referencias antes de usarlos.
- No presentes como propio un trabajo generado completamente por IA.
- Explica qué cambiaste y qué aprendiste.
- Si un prompt produce una respuesta incorrecta, eso también puede convertirse en un buen tip para el banco.

## 📁 Estructura

~~~text
Banco-de-prompts/
├── README.md
├── CONTRIBUTING.md
├── .github/
│   └── pull_request_template.md
├── plantillas/
│   └── nuevo-prompt.md
└── prompts/
    ├── aprendizaje/
    ├── programacion/
    ├── depuracion/
    ├── proyectos/
    ├── git-github/
    ├── fotografia/
    ├── videos/
    ├── animacion/
    ├── bases-de-datos/
    ├── analisis-de-datos/
    ├── visualizacion-de-datos/
    └── tips-genericos/
~~~

## 🌱 Este repositorio debe crecer con el curso

Cada aporte aceptado mejora el material para los compañeros actuales y para los estudiantes que vengan después.

**Usa. Prueba. Mejora. Comparte.**
