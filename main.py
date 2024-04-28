from PIL import Image, ImageDraw, ImageFont
import os


def cargar_imagen(ruta):
    try: 
        imagen = Image.open(ruta)
        return imagen
    except IOError:
        print("No se pudo abrir la imagen, Perdon!")
        return None
    
def agregar_texto(imagen, texto, posicion, color=(255,255,255), size=40, fuente="arial.ttf"):
    draw = ImageDraw.Draw(imagen)
    font = ImageFont.truetype(fuente, size)
    draw.text(posicion, texto, fill=color, font=font)
    return imagen

def guardar_meme(imagen, nombre_salida):
    try: 
        imagen.save(nombre_salida)
        print("Meme guardado como: ", nombre_salida)
        
    except Exception as e:
        print("Error al guardar el meme: ", e)

def main():
    print("Bienvenido al Generador de Memes")

    ruta_imagen = input("Ingrese la ruta de la imagen: ")
    imagen_base = cargar_imagen(ruta_imagen)

    if imagen_base is None:
        return
    
    imagen_base.show()

    texto = input("Ingrese el texto para el meme: ")
    posicion_texto = tuple(map(int, input("Ingrese la posición del texto (x, y): ").split(",")))
    color_texto = tuple(map(int, input("Ingrese el color del texto (R, G, B): ").split(",")))

    imagen_con_texto = agregar_texto(imagen_base,texto, posicion_texto, color_texto)

    imagen_con_texto.show()

    nombre_salida = input("Ingrese el nombre final del meme: ")
    guardar_meme(imagen_con_texto, nombre_salida)

if __name__ == "__main__":
    main()
