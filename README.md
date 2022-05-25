# Modbus-API
Utilizando o microframework Flask mais a biblioteca ModbusTCP para criar uma API de consultas diretamente com o CLP.

Exemplo de aplicação para coletar dados de um CLP via Modbus ou escrever nas variávies. As requisições são executadas pelo cliente e devolvidas em formato JSON.;

Realiza a leitura de 3 endereços Modbus a partir do endereço 40001 ou escrita a aprtir do endereço 40004 de acordo com a requisição solicitada;

Para o exemplo, foi utilizado o Python 3.8.1; Bibliotecas: Modbus TCP - pyModbusTCP 0.1.10 Flask;

O CLP Utilizado foi o Codesys versão 3.5, a configuração está disponível neste repositório.

Utilizando o mesmo conceito que outras aplicações com Modbus, porém com a biblioteca Flask criando uma API para consulta ou escrita no CLP.
Instalar o Insomnia para testar as requisições.

Autor: Douglas Silva.
