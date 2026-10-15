# Registro de Ponto em Python

Aplicação de terminal para registrar nome e data/hora e consultar marcações em arquivo de texto.

## Recursos

Menu de registro e visualização; persistência em ponto.txt no diretório de execução.

## Tecnologias

Python 3 e biblioteca padrão.

## Executar localmente

Instale Python 3 e corrija a condição de inicialização descrita abaixo. Depois:

```sh
git clone https://github.com/Felipegaldinos/ponto-eletronico.git
cd ponto-eletronico
python ponto.py
```

## Onde começar no código

- `ponto.py` — ponto de entrada para entender o projeto.

## Estado atual

Há um erro de inicialização no arquivo atual: if _name_ == "_main_": deve ser if __name__ == "__main__":. Corrija essa linha para usar o menu. O programa não diferencia entrada de saída e não calcula jornada. A alteração deste PR é somente documentação.

## Autoria

[Felipe Galdino](https://github.com/Felipegaldinos). Consulte os arquivos do repositório para os termos de licença aplicáveis.
