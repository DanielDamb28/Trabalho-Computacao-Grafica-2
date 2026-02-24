# Trabalho de Computação Gráfica 2 - Logística em Realidade Aumentada

Este projeto utiliza **Realidade Aumentada (AR)** para simular o processo de empilhamento de cargas em um ambiente logístico. A aplicação é capaz de detectar superfícies reais, posicionar um palete e realizar o empilhamento de objetos virtuais com validação de regras físicas e de volume.

## 🛠️ Tecnologias Utilizadas

* **Three.js**: Biblioteca principal para renderização da cena 3D e manipulação de objetos.
* **WebXR API**: Utilizada para integração com a câmera do dispositivo e detecção de superfícies (hit-test).
* **Python (http.server)**: Servidor back-end customizado para servir os arquivos estáticos e capturar telemetria (logs de posição e eventos) via requisições POST.
* **ngrok**: Ferramenta de tunelamento para expor o localhost via HTTPS, requisito obrigatório para o funcionamento da API de Realidade Aumentada em navegadores móveis.

---

## 💻 Como Rodar o Projeto

Como o projeto utiliza a API WebXR, é necessário que o acesso seja feito através de uma conexão segura (**HTTPS**).

### 1. Iniciar o Servidor Python
O arquivo `server.py` atua como servidor de arquivos e receptor de logs. No terminal, dentro da pasta do projeto, execute:

```bash
python server.py 8000
