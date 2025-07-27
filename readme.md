### Env

### Create venv
```
python3 -m venv my_env_name
```

### Definir no interpreter do PyCharm como o env criado
> Settings > Project > Python Interpreter > Add Interpreter
> Select Existing > find folder my_env_name

### Habilitar o env no terminal
```bash
$ source .venv/bin/activate
```

### Instalar dependências somente no ENV selecionado
```
$ pip install -r requirements.txt
```

### Executar jupyter
```bash
jupyter notebook
```

### PyCharm Plot
- Para melhor visualizar os plots:
> Settings > Languages & Frameworks > Jupyter > (uncheck) Invert image outputs for dark themes


### Sair do env
```
$ deactivate
```

