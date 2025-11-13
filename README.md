# Validador de Identificadores - Teste de Software

## Descrição do Problema

O programa deve determinar se um identificador é válido ou não.

### Um identificador válido:
- Deve começar com uma letra (a-z ou A-Z);
- Pode conter apenas letras ou dígitos;
- Deve ter de 1 a 6 caracteres de comprimento (inclusive).

_A função deve retornar um valor booleano ou uma mensagem indicando se o identificador é válido._

---

## Análise de Classes de Equivalência

### Metodologia: Particionamento em Classes de Equivalência

O particionamento em classes de equivalência divide o domínio de entrada em grupos onde todos os valores de uma mesma classe devem produzir o mesmo comportamento. Isso permite reduzir o número de testes mantendo boa cobertura.

### 1. Classes de Equivalência para **Comprimento**

| Classe        | Descrição             | Tipo      | Exemplos                       |
| ------------- | ----------------------- | --------- | ------------------------------ |
| **CE1** | Comprimento = 0 (vazio) | Inválida | ""                             |
| **CE2** | Comprimento = 1         | Válida   | "A"                            |
| **CE3** | Comprimento entre 2 e 5 | Válida   | "AB", "A1B", "AB12C"           |
| **CE4** | Comprimento = 6         | Válida   | "A12345"                       |
| **CE5** | Comprimento > 6         | Inválida | "A123456", "stringmuitogrande" |

### 2. Classes de Equivalência para **Caractere Inicial**

| Classe        | Descrição                       | Tipo      | Exemplos      |
| ------------- | --------------------------------- | --------- | ------------- |
| **CE6** | Inicia com letra maiúscula (A-Z) | Válida   | "A", "Z123"   |
| **CE7** | Inicia com letra minúscula (a-z) | Válida   | "a", "z123"   |
| **CE8** | Inicia com dígito (0-9)          | Inválida | "1", "9abc"   |
| **CE9** | Inicia com caractere especial     | Inválida | "@abc", "_id" |

### 3. Classes de Equivalência para **Composição de Caracteres**

| Classe         | Descrição                  | Tipo      | Exemplos         |
| -------------- | ---------------------------- | --------- | ---------------- |
| **CE10** | Contém apenas letras        | Válida   | "ABC", "abc"     |
| **CE11** | Contém letras e dígitos    | Válida   | "A1B2", "abc123" |
| **CE12** | Contém caracteres especiais | Inválida | "A@B", "a-b"     |

---

## Análise de Valor Limite

### Metodologia: Valores Limite

A análise de valor limite foca nos valores nas fronteiras das classes de equivalência, pois erros tendem a ocorrer nesses pontos críticos.

### Valores Limite Identificados

#### Para o **Comprimento**:

- **Limite inferior**:

  - `0` caracteres (inválido - abaixo do mínimo)
  - `1` caractere (válido - mínimo aceito)
  - `2` caracteres (válido - logo acima do mínimo)
- **Limite superior**:

  - `5` caracteres (válido - logo abaixo do máximo)
  - `6` caracteres (válido - máximo aceito)
  - `7` caracteres (inválido - acima do máximo)

#### Para o **Caractere Inicial**:

- Fronteira alfabética:
  - `A` (primeira letra maiúscula)
  - `Z` (última letra maiúscula)
  - `a` (primeira letra minúscula)
  - `z` (última letra minúscula)
  - `@` (caractere antes de 'A' na tabela ASCII)
  - `[` (caractere depois de 'Z' na tabela ASCII)
  - `0`, `9` (dígitos nas extremidades)

---

## Tabela Completa de Casos de Teste

| ID             | Entrada                 | Classes de Equivalência | Valor Limite                     | Resultado Esperado | Justificativa                                    |
| -------------- | ----------------------- | ------------------------ | -------------------------------- | ------------------ | ------------------------------------------------ |
| **CT01** | `""`          | CE1                      | Comprimento = 0                  | Inválido       | Comprimento abaixo do mínimo                    |
| **CT02** | `"A"`                 | CE2, CE6, CE10           | Comprimento = 1, Letra inicial A | Válido         | Comprimento mínimo válido, inicia com letra    |
| **CT03** | `"AB"`                | CE3, CE6, CE10           | Comprimento = 2                  | Válido         | Logo acima do mínimo                            |
| **CT04** | `"ABC12"`             | CE3, CE6, CE11           | -                                | Válido         | Comprimento médio, letras + dígitos            |
| **CT05** | `"ABCDE"`             | CE3, CE6, CE10           | Comprimento = 5                  | Válido         | Logo abaixo do máximo                           |
| **CT06** | `"A12345"`            | CE4, CE6, CE11           | Comprimento = 6                  | Válido         | Comprimento máximo válido                      |
| **CT07** | `"A123456"`           | CE5, CE6, CE11           | Comprimento = 7                  | Inválido       | Comprimento acima do máximo                     |
| **CT08** | `"stringmuitogrande"` | CE5, CE7, CE10           | Comprimento >> 6                 | Inválido       | Muito acima do máximo                           |
| **CT09** | `"z"`                 | CE2, CE7, CE10           | Letra inicial z                  | Válido         | Limite alfabético minúsculo                    |
| **CT10** | `"Z123"`              | CE3, CE6, CE11           | Letra inicial Z                  | Válido         | Limite alfabético maiúsculo                    |
| **CT11** | `"1"`                 | CE2, CE8                 | Comprimento = 1, Dígito inicial | Inválido       | Não inicia com letra                            |
| **CT12** | `"123456"`            | CE4, CE8                 | Comprimento = 6, Dígito inicial | Inválido       | Não inicia com letra, mesmo com tamanho válido |
| **CT13** | `"@abc"`              | CE3, CE9                 | Caractere especial inicial       | Inválido       | Não inicia com letra                            |
| **CT14** | `"A@B"`               | CE3, CE6, CE12           | -                                | Inválido       | Contém caractere especial                       |
| **CT15** | `"A-B"`               | CE3, CE6, CE12           | -                                | Inválido       | Contém caractere especial (hífen)              |
| **CT16** | `"a1"`                | CE3, CE7, CE11           | Minúscula + dígito             | Válido         | Letra minúscula válida                         |
| **CT17** | `"abc123"`            | CE4, CE7, CE11           | Comprimento = 6, minúscula      | Válido         | Máximo com minúscula                           |
| **CT18** | `"A "` (com espaço)  | CE3, CE6, CE12           | -                                | Inválido       | Espaço é caractere especial                    |

---

## Como Executar os Testes Localmente

### Pré-requisitos

- Python 3.6 ou superior instalado
- pytest (para executar a suíte de testes automatizada)

### Instalação do pytest

```powershell
pip install pytest
```

### Executar os Testes

#### Com pytest (recomendado):
```powershell
pytest test_identifier.py -v
```

#### Manualmente (exemplos):
```powershell
# Teste válido
python identifier.py "A12345"

# Teste inválido
python identifier.py "123456"
```
