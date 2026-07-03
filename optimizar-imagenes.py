# -*- coding: utf-8 -*-
# ============================================================
# Optimiza todas las imágenes del sitio para web:
#  - Redimensiona a máximo 1920px de ancho
#  - Convierte fotos PNG pesadas a JPEG calidad 82
#  - Conserva PNG solo donde hay transparencia (logo, etc.)
#  - Actualiza las referencias en todos los .html si cambia
#    la extensión de algún archivo
#
# Cómo usarlo (una sola vez, desde la carpeta raíz del sitio):
#   pip3 install pillow
#   python3 optimizar-imagenes.py
# ============================================================
import os, glob
from PIL import Image

IMG_DIR = "assets/img"
MAX_W = 1920
QUALITY = 82
SKIP = {"partner-1.png", "partner-2.png"}  # logos chicos del footer, se quedan igual

renombres = {}  # nombre_viejo -> nombre_nuevo (solo si cambia extensión)

def tiene_transparencia(img):
    if img.mode in ("RGBA", "LA"):
        alpha = img.getchannel("A")
        return alpha.getextrema()[0] < 255
    return "transparency" in img.info

for path in sorted(glob.glob(os.path.join(IMG_DIR, "*"))):
    nombre = os.path.basename(path)
    if nombre in SKIP:
        continue
    kb_antes = os.path.getsize(path) / 1024
    if kb_antes < 300:  # ya es liviana, no la tocamos
        continue

    img = Image.open(path)
    if img.width > MAX_W:
        img = img.resize((MAX_W, round(img.height * MAX_W / img.width)), Image.LANCZOS)

    base, ext = os.path.splitext(nombre)
    if tiene_transparencia(img):
        # conserva PNG (ej. el logo) pero optimizado
        img.save(path, "PNG", optimize=True)
        nuevo = nombre
    else:
        nuevo = base + ".jpg"
        nuevo_path = os.path.join(IMG_DIR, nuevo)
        img.convert("RGB").save(nuevo_path, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        if nuevo != nombre:
            os.remove(path)
            renombres[nombre] = nuevo

    kb_despues = os.path.getsize(os.path.join(IMG_DIR, nuevo)) / 1024
    print(f"✓ {nombre:24s} {kb_antes/1024:5.1f} MB → {kb_despues:6.0f} KB  ({nuevo})")

# Actualizar referencias en los HTML
if renombres:
    print("\nActualizando referencias en los archivos HTML...")
    for html_path in glob.glob("**/*.html", recursive=True):
        with open(html_path, encoding="utf-8") as f:
            contenido = f.read()
        original = contenido
        for viejo, nuevo in renombres.items():
            contenido = contenido.replace(f"/assets/img/{viejo}", f"/assets/img/{nuevo}")
        if contenido != original:
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(contenido)
            print(f"  ✓ {html_path}")

print("\n✅ Listo. Revisa el nuevo peso con:  du -sh assets")
print("Ahora sí, sube toda la carpeta a GitHub sin problema.")
