 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
index 5fb7d7ed39ff8fc5d944b119c6b78904910b47d7..85beba6d6b932c029381029be5676dd2d06d6429 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,32 @@
-# IMC-GPT2
\ No newline at end of file
+# IMC-GPT2
+
+Aplicativo simples de linha de comando para calcular o Índice de Massa Corporal (IMC) e exibir a categoria correspondente.
+
+## Requisitos
+
+- Python 3.8 ou superior.
+
+## Uso
+
+1. Instale as dependências (nenhuma biblioteca externa é necessária além da distribuição padrão do Python).
+2. Execute o comando abaixo substituindo os valores de exemplo pelo seu peso (kg) e altura (m):
+
+```bash
+python imc.py --peso 70 --altura 1.75
+```
+
+Saída esperada:
+
+```
+IMC: 22.86
+Categoria: Peso normal
+```
+
+## Categorias adotadas
+
+- Abaixo do peso: IMC < 18.5
+- Peso normal: 18.5 <= IMC < 25
+- Sobrepeso: 25 <= IMC < 30
+- Obesidade grau I: 30 <= IMC < 35
+- Obesidade grau II: 35 <= IMC < 40
+- Obesidade grau III: IMC >= 40
 
EOF
)
