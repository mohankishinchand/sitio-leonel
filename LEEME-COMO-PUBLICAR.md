# Cómo publicar tu sitio en GitHub Pages (gratis)

Tu sitio ya está construido. Solo faltan 3 pasos que haces una sola vez.

## Estructura del sitio

```
/                  → detecta el idioma del visitante y lo manda a /es/ o /en/
/es/               → Inicio (español)
/es/propiedades/   → Propiedades
/es/exclusivas/    → Propiedades exclusivas (antes oculta, ahora en el menú)
/es/sobre-mi/      → Sobre mí
/es/contacto/      → Contacto
/en/               → Home (inglés)
/en/properties/    → Properties
/en/exclusive/     → Luxury homes (antes oculta, ahora en el menú)
/en/about/         → About me
/en/contact/       → Contact
```

Cada página tiene un botón **EN / ES** en el menú para cambiar de idioma.

---

## Paso 1 — Descargar las imágenes y el video (5 min)

Las imágenes todavía viven en el servidor de GoHighLevel. Para que el sitio
sea 100% tuyo, descárgalas una vez:

1. Abre una terminal en la carpeta del sitio
   (Mac: Terminal · Windows: Git Bash, viene con Git)
2. Corre:

```bash
bash descargar-assets.sh
```

Eso llena las carpetas `assets/img` y `assets/video` con todo.
**Hazlo antes de cancelar tu cuenta de GHL**, porque el script descarga desde su CDN.

Para ver el sitio en tu compu antes de publicarlo:

```bash
python3 -m http.server 8000
```

y abre http://localhost:8000

---

## Paso 2 — Subir a GitHub (10 min)

1. Crea una cuenta gratis en https://github.com si no tienes
2. Crea un repositorio nuevo → nómbralo por ejemplo `sitio-leonel` → público
3. En la página del repo, usa **"uploading an existing file"** y arrastra
   TODO el contenido de esta carpeta (incluyendo las carpetas es/, en/, assets/)
   - Ojo: el video hero.mp4 puede pesar varios MB; GitHub acepta archivos de hasta 100 MB, así que no hay problema
4. Clic en **Commit changes**
5. Ve a **Settings → Pages** → en "Branch" selecciona `main` y carpeta `/ (root)` → **Save**

En 1-2 minutos tu sitio estará en `https://tuusuario.github.io/sitio-leonel/`

---

## Paso 3 — Conectar tu dominio (10 min + espera de DNS)

El archivo `CNAME` ya está incluido con `leonelespinosaworldclass.com`, así que
GitHub lo reconocerá solo. Falta apuntar el dominio:

1. Entra al panel donde compraste el dominio (GoDaddy, Namecheap, etc.)
2. **Borra** los registros DNS actuales que apuntan a GoHighLevel
3. Crea estos registros:

| Tipo  | Nombre | Valor                    |
|-------|--------|--------------------------|
| A     | @      | 185.199.108.153          |
| A     | @      | 185.199.109.153          |
| A     | @      | 185.199.110.153          |
| A     | @      | 185.199.111.153          |
| CNAME | www    | tuusuario.github.io      |

4. En GitHub: **Settings → Pages → Custom domain** → escribe
   `leonelespinosaworldclass.com` → Save
5. Espera a que aparezca la palomita verde de verificación (minutos a unas horas)
6. Marca la casilla **Enforce HTTPS**

Listo: tu sitio queda en https://leonelespinosaworldclass.com, gratis y sin GHL.

---

## Pendientes para ti (2 detalles)

1. **TikTok**: no pude ver la URL de tu perfil desde el sitio original. En el
   footer de cada página busca `https://www.tiktok.com/` y cámbiala por tu
   perfil real (es la misma línea en los 10 archivos, o dime la URL y lo hago yo).
2. **Copyright**: el sitio original decía "© Chuy Gastelum Coach" en las páginas
   en español (parece un sobrante de plantilla). Lo corregí a
   "© 2026 Leonel Espinosa | World Class Realty" en todo el sitio. Si eso estaba
   ahí a propósito, avísame.

## Cómo editar el sitio después

Cada página es un archivo `index.html` sencillo. Para cambiar un texto, precio
o foto, edita el archivo directamente en GitHub (icono de lápiz) y guarda:
el sitio se actualiza solo en ~1 minuto. También me puedes pedir los cambios
a mí y te regreso el archivo actualizado.
