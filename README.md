Trabalho de Computação Gráfica 2 - Logística em Realidade Aumentada
Este projeto utiliza Realidade Aumentada (AR) para simular o processo de empilhamento de cargas em um ambiente logístico. A aplicação é capaz de detectar superfícies reais, posicionar um palete e realizar o empilhamento de objetos virtuais com validação de regras físicas e de volume.

🛠️ Tecnologias Utilizadas
Three.js: Biblioteca principal para renderização da cena 3D e manipulação de objetos.

WebXR API: Utilizada para integração com a câmera do dispositivo e detecção de superfícies (hit-test).

Python (http.server): Servidor back-end simples para servir os arquivos e capturar telemetria (logs) via requisições POST.

ngrok: Ferramenta de tunelamento para expor o localhost via HTTPS, requisito obrigatório para o uso de AR no navegador do celular.

💻 Como Rodar o Projeto
Como o projeto utiliza a API de Realidade Aumentada, é necessário que o acesso seja feito através de uma conexão segura (HTTPS).

1. Iniciar o Servidor
O arquivo server.py atua como servidor de arquivos estáticos e receptor de logs. Execute o comando no terminal dentro da pasta do projeto:

Bash
python server.py 8000
2. Configurar o Túnel HTTPS (ngrok)
Para que o navegador do celular reconheça as permissões de AR, você deve transformar o link local em um link seguro:

Bash
ngrok http 8000
O ngrok gerará um endereço (ex: https://seulink.ngrok.io).

3. Acesso e Operação
Abra a URL gerada pelo ngrok no navegador do celular (Chrome para Android).

Clique em "START AR".

Fase 1: Mova o celular para detectar o chão (uma mira redonda verde aparecerá). Clique para posicionar o palete.

Fase 2: Após o palete, a mira se tornará quadrada (ajustada ao tamanho da carga sorteada). Posicione as cargas sobre o palete respeitando as regras de empilhamento.

📂 Estrutura do Projeto
index.html: Contém toda a aplicação, incluindo a lógica 3D (Three.js), os estilos (CSS) e os shaders de Realidade Aumentada.

server.py: Script não obrigatório para a renderização, mas essencial para capturar as coordenadas e logs do navegador do celular diretamente no terminal do PC.
