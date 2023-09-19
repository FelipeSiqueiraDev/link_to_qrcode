import qrcode
from PIL import Image, ImageDraw

def generate_QRCode(dados, nome_arquivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(dados)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#000")

    # Converter para RGBA para lidar com a transparência
    img = img.convert("RGBA")

    # Criar um fundo transparente
    img_with_transparent_bg = Image.new("RGBA", img.size, (255, 255, 255, 0))
    img_with_transparent_bg.paste(img, (0, 0), img)

    img_with_transparent_bg.save(nome_arquivo, format="PNG")

if __name__ == "__main__":
    link = input("Digite o link que você deseja transformar em QRCode: ")
    nome_arquivo = input("Digite o nome do arquivo de saída (por exemplo, qrcode.png): ")

    generate_QRCode(link, nome_arquivo)
    print(f"O QRCode foi salvo como '{nome_arquivo}'.")
