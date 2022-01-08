# Automatização de relatórios de fechamento mensal
## Sobre

Projeto pessoal para facilitar gerar relatórios mensais no trabalho.
___

## Começando
___

1. <b>Instalando as dependências:</b>
```bash
pip install -r requirements.txt
```

2. <b>Exporte a variável DSN de conexão com o banco em um arquivo .env:</b>
```
DSN="host=<ip> port=<porta> user=<usuario> password=<senha> dbname=<db>"
```

3. No módulo mmids passe uma lista de MMIDs a ser consultado.

4. <b>Execute o módulo exec_job definindo as seguintes configurações:</b>

```python
closing_config = {
    'version' : '1',
    'range_start_date' : '2021-12-01',
    'range_end_date' : '2021-12-31',
    'mmids' : list_mmids
}
```

Por fim um arquivo Excel é gerado com as cinco abas dos dados de fechamento dos customers.