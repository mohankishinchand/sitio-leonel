#!/bin/bash
# ============================================================
# Descarga todas las imágenes y el video del sitio desde el
# CDN de GoHighLevel y las guarda localmente.
# Correr UNA VEZ desde la carpeta raíz del sitio:
#   bash descargar-assets.sh
# Requiere: curl (viene incluido en Mac y en Git Bash de Windows)
# ============================================================
set -e
CDN1="https://assets.cdn.filesafe.space/rRtgGSsJXTkcGHrebAXM/media"
CDN2="https://assets.cdn.filesafe.space/ydtHJvMNnqFEtgYbdrvr/media"
mkdir -p assets/img assets/video

dl () { echo "Descargando $2 ..."; curl -fsSL "$1" -o "$2"; }

# Logo e identidad
dl "$CDN1/69f8186e086be1f079ee4063.png"  assets/img/logo.png
dl "$CDN1/69e7243fc56ad27908612676.png"  assets/img/leonel.png
dl "$CDN1/69e6eeb4c56ad2790856257a.jpg"  assets/img/leonel-2.jpg

# Video de portada
dl "$CDN1/69e733153ea93d9dd209276a.mp4"  assets/video/hero.mp4

# Imágenes de secciones
dl "$CDN1/69e7ca2b6fc69286f3ab0fe6.png"  assets/img/hero-landing.png
dl "$CDN1/69e6fbd15e482c379b8773a7.png"  assets/img/home-1.png
dl "$CDN1/69e7d4a0b0e5e2bb7f934ff3.png"  assets/img/security.png
dl "$CDN1/69e7d51f6fc69286f3ae2b32.png"  assets/img/north.png
dl "$CDN1/69e7d7ae03c24196d2497043.png"  assets/img/lifestyle.png

# Propiedades
dl "$CDN1/69f2ba86590487fe57e97bd3.jpg"  assets/img/prop-provincia.jpg
dl "$CDN1/69f2bc77590487fe57e9f732.jpg"  assets/img/prop-navela.jpg
dl "$CDN1/69f81322dd67e758c0066fc0.jpeg" assets/img/prop-celestun.jpeg
dl "$CDN1/69e7d40d6fc69286f3ade0ef.png"  assets/img/prop-ycc.png
dl "$CDN1/69e7d5e5da11eeea68eb264a.png"  assets/img/prop-kanha.png

# Logos de aliados/certificaciones (footer)
dl "$CDN2/684554318c81194c426e0438.png"  assets/img/partner-1.png
dl "$CDN2/684c0652107fb0734db501b6.png"  assets/img/partner-2.png

echo ""
echo "✅ Listo. Todos los assets quedaron en assets/img y assets/video."
echo "Ahora el sitio ya no depende de GoHighLevel para nada."
