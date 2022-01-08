# Automatização de relatórios de fechamento mensal
## Sobre

Projeto pessoal para facilitar gerar relatórios mensais no trabalho.

## Executando o projeto

1. Instalando as dependências
```bash
pip install -r requirements.txt
```

2. Exporte a variável DSN de conexão com o banco em um arquivo .env
```
DSN="host=<ip> port=<porta> user=<usuario> password=<senha> dbname=<db>"
```

3. No módulo mmids passe uma lista de MMIDs à ser consultado.

4. Execute o módulo exec_job definindo as seguintes configurações

```python
closing_config = {
    'version' : '1',
    'range_start_date' : '2021-12-01',
    'range_end_date' : '2021-12-31',
    'mmids' : list_mmids
}
```

Por fim um arquivo Excel é gerado com as cinco abas dos dados de fechamento mensal dos customers.