import cv2
import numpy as np
from matplotlib import pyplot as plt

def create_band_reject_filter(shape, r_in, r_out):
    """
    Cria uma máscara de filtro rejeita-banda ideal (formato de anel).

    Args:
        shape (tuple): A forma da imagem (altura, largura).
        r_in (int): O raio interno do anel de rejeição.
        r_out (int): O raio externo do anel de rejeição.

    Returns:
        numpy.ndarray: A máscara do filtro.
    """
    rows, cols = shape
    center_row, center_col = rows // 2, cols // 2

    # Cria uma grade de coordenadas a partir do centro
    y, x = np.ogrid[-center_row:rows-center_row, -center_col:cols-center_col]
    
    # Calcula a distância de cada ponto ao centro
    dist_from_center = np.sqrt(x**2 + y**2)

    # Cria a máscara: 1 em todos os lugares, exceto no anel
    # Onde a distância está entre r_in e r_out, o valor é 0.
    mask = (dist_from_center < r_in) | (dist_from_center > r_out)
    
    return mask.astype(float)


def create_band_pass_filter(shape, r_in, r_out):
    """
    Cria uma máscara de filtro passa-banda ideal (formato de anel).

    Args:
        shape (tuple): A forma da imagem (altura, largura).
        r_in (int): O raio interno do anel de passagem.
        r_out (int): O raio externo do anel de passagem.

    Returns:
        numpy.ndarray: A máscara do filtro.
    """
    # Um filtro passa-banda é simplesmente o inverso de um rejeita-banda.
    return 1 - create_band_reject_filter(shape, r_in, r_out)


def apply_frequency_filter(image, filter_mask):
    """
    Aplica uma máscara de filtro a uma imagem no domínio da frequência.

    Args:
        image (numpy.ndarray): A imagem de entrada (escala de cinza).
        filter_mask (numpy.ndarray): A máscara de filtro a ser aplicada.

    Returns:
        numpy.ndarray: A imagem filtrada.
    """
    # 1. Transformada de Fourier e centralização do espectro
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # 2. Aplicar a máscara (multiplicação elemento a elemento)
    # A máscara precisa ser de 2 canais para multiplicar a parte real e imaginária
    mask_2ch = np.stack([filter_mask, filter_mask], axis=-1)
    f_shift_filtered = dft_shift * mask_2ch
    
    # 3. Desfazer a centralização
    f_ishift = np.fft.ifftshift(f_shift_filtered)
    
    # 4. Transformada Inversa de Fourier para voltar ao domínio espacial
    img_back = cv2.idft(f_ishift)
    
    # 5. Obter a magnitude e normalizar para visualização
    img_filtered = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    cv2.normalize(img_filtered, img_filtered, 0, 255, cv2.NORM_MINMAX)
    
    return img_filtered.astype(np.uint8)


# --- SCRIPT PRINCIPAL ---
if __name__ == "__main__":
    # Lista de imagens a serem processadas
    # SUBSTITUA PELOS NOMES CORRETOS DOS SEUS ARQUIVOS
    image_files = ["teste.tif", "img_aluno.png"]

    # ATENÇÃO: Se você não tiver as imagens, o código abaixo criará
    # imagens de exemplo para que o script possa ser executado.
    # Comente ou apague este bloco se você já tiver suas imagens na pasta.
    try:
        # Tenta ler a primeira imagem para ver se ela existe
        cv2.imread(image_files[0], cv2.IMREAD_GRAYSCALE)
    except:
        print("Aviso: Imagens não encontradas. Criando imagens de exemplo 'teste.tif' e 'img_aluno.png'.")
        # Cria uma imagem de teste com ruído periódico (linhas)
        img_teste = np.zeros((512, 512), dtype=np.uint8)
        for i in range(0, 512, 10):
            cv2.line(img_teste, (0, i), (512, i), 128, 1)
        cv2.putText(img_teste, 'Teste', (180, 256), cv2.FONT_HERSHEY_SIMPLEX, 2, 255, 3)
        cv2.imwrite("teste.tif", img_teste)

        # Cria uma segunda imagem de exemplo
        img_aluno = np.zeros((512, 512), dtype=np.uint8)
        cv2.circle(img_aluno, (256, 256), 100, 255, -1)
        # Adiciona um padrão de ruído em forma de grade
        for i in range(0, 512, 20):
            cv2.line(img_aluno, (i, 0), (i, 512), 64, 1)
            cv2.line(img_aluno, (0, i), (512, i), 64, 1)
        cv2.imwrite("img_aluno.png", img_aluno)
    # Fim do bloco de criação de imagens de exemplo.

    # Parâmetros dos filtros (EXPERIMENTE MUDAR ESSES VALORES!)
    # Raio interno e externo do anel
    inner_radius = 40
    outer_radius = 80

    # Processa cada imagem da lista
    for filename in image_files:
        # Carrega a imagem em escala de cinza
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        
        if img is None:
            print(f"Erro: Não foi possível carregar a imagem '{filename}'. Pulando.")
            continue

        # --- Geração e Aplicação dos Filtros ---
        
        # Filtro Rejeita-Banda
        reject_mask = create_band_reject_filter(img.shape, inner_radius, outer_radius)
        img_rejected = apply_frequency_filter(img, reject_mask)

        # Filtro Passa-Banda
        pass_mask = create_band_pass_filter(img.shape, inner_radius, outer_radius)
        img_passed = apply_frequency_filter(img, pass_mask)
        
        # --- Visualização dos Resultados ---
        plt.figure(figsize=(18, 10))
        plt.suptitle(f'Filtragem em Frequência: {filename}', fontsize=16)

        # Original
        plt.subplot(2, 3, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Imagem Original')
        plt.axis('off')

        # Filtro Rejeita-Banda
        plt.subplot(2, 3, 2)
        plt.imshow(reject_mask, cmap='gray')
        plt.title(f'Máscara Rejeita-Banda\n(r_in={inner_radius}, r_out={outer_radius})')
        plt.axis('off')

        plt.subplot(2, 3, 3)
        plt.imshow(img_rejected, cmap='gray')
        plt.title('Resultado Rejeita-Banda')
        plt.axis('off')

        # Espectro de Fourier da imagem original para referência
        dft_original = np.fft.fftshift(cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT))
        magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_original[:, :, 0], dft_original[:, :, 1]) + 1)
        plt.subplot(2, 3, 4)
        plt.imshow(magnitude_spectrum, cmap='gray')
        plt.title('Espectro de Frequência Original')
        plt.axis('off')
        
        # Filtro Passa-Banda
        plt.subplot(2, 3, 5)
        plt.imshow(pass_mask, cmap='gray')
        plt.title(f'Máscara Passa-Banda\n(r_in={inner_radius}, r_out={outer_radius})')
        plt.axis('off')

        plt.subplot(2, 3, 6)
        plt.imshow(img_passed, cmap='gray')
        plt.title('Resultado Passa-Banda')
        plt.axis('off')

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig('3.png') 

        plt.show()
