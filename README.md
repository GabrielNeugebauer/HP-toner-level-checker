# Monitor de Impressoras

Este projeto exibe graficamente o status de toner e unidade de imagem de impressoras HP em rede, utilizando um servidor Flask como backend e uma interface web como frontend.

## 📁 Estrutura do Projeto

* `Servidor.py`: Backend Flask que coleta os dados das impressoras via cURL e expõe uma API REST.
* `frontend.html`: Página web que consome a API e exibe gráficos circulares com os níveis de toner e unidade de imagem.

## 🚀 Como Executar

1. **Instale as dependências:**

   ```bash
   pip install flask flask-cors
   ```

2. **Execute o servidor:**

   ```bash
   python Servidor.py
   ```

3. **Abra o frontend:**

   * Dê um duplo clique em `frontend.html` ou abra no navegador.
   * Certifique-se de que o backend está rodando em `http://localhost:5000`.

## ⚙️ Funcionalidades

* Consulta automática dos níveis de suprimentos de impressoras.
* Interface amigável com gráficos de pizza desenhados em `<canvas>`.
* Atualização dinâmica dos dados ao carregar a página.

## 🛡️ Observações

* É necessário que as impressoras estejam acessíveis via HTTPS e forneçam os dados em `/sws/app/information/supplies/supplies.json`, caminho padrão para impressoras HP.
* O frontend usa `fetch` com `http://localhost:5000/status`. Certifique-se de que não há bloqueio por CORS.
