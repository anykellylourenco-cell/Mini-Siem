# Mini SIEM

## Descrição

O Mini SIEM é uma ferramenta desenvolvida em Python para simular funcionalidades básicas de um Security Information and Event Management (SIEM).

O programa realiza a leitura de arquivos de log, identifica tentativas de login com falha, verifica indicadores de comprometimento (IOCs) por meio da comparação com uma lista de IPs e gera um relatório com os resultados da análise.

## Funcionalidades

* Leitura de arquivos de log.
* Detecção de tentativas de login com falha.
* Extração de endereços IPv4 dos logs.
* Comparação dos IPs encontrados com uma lista de IOCs.
* Geração automática de relatório.
* Estrutura modular para facilitar manutenção e expansão.

## Estrutura do Projeto

mini-siem/
│
├── main.py
├── logs.txt
├── malicious_ips.txt
├── reports/
│   └── report.txt
├── modules/
│   ├── __init__.py
│   ├── failed_login.py
│   ├── ioc_checker.py
│   ├── log_parser.py
│   └── report_generator.py
└── README.md

## Tecnologias Utilizadas

* Python 3
* pathlib
* re

## Próximas melhorias

* Detecção de brute force por janela de tempo.
* Detecção de port scanning.
* Leitura de arquivos JSON.
* Exportação de relatórios em CSV.
* Interface de linha de comando com argparse.
* Integração com APIs de Threat Intelligence.
* Geração de logs em formato estruturado.

# Autor

Any Kelly