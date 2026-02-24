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
```

O servidor ficará ouvindo a porta 8000 e imprimirá no console todos os logs enviados pelo celular.

### 2. Configurar o Túnel HTTPS (ngrok)
Abra um segundo terminal e utilize o ngrok para gerar uma URL segura que aponte para o seu servidor local:

```bash
ngrok http 8000
```
O ngrok fornecerá um endereço semelhante a https://abcd-123.ngrok.io.

### 3. Acesso e Operação no Dispositivo
Acesse a URL gerada pelo ngrok no navegador do celular (recomenda-se o Chrome no Android).

Clique no botão "START AR" na parte inferior da tela.

Fase 1 (Círculo Verde): Mova o celular para escanear o ambiente. Quando um círculo verde aparecer no chão, clique na tela para posicionar o Palete.

Fase 2 (Quadrado Rosa/Vermelho): Após o palete, a mira se tornará um quadrado que reflete o tamanho da carga sorteada.

Rosa: Posição válida para empilhar.

Vermelho: Posição inválida (espaço ocupado ou violação da regra de cores).

###  📂 Estrutura do Projeto
index.html: Contém toda a aplicação, incluindo o motor de renderização 3D, a lógica de hit-test, as regras de empilhamento e a interface de usuário.

server.py: Script responsável por servir o projeto e permitir que os logs de depuração do navegador do celular sejam visualizados em tempo real no terminal do computador através da rota /log.
