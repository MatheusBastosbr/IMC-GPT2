 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/tests/test_imc.py b/tests/test_imc.py
new file mode 100644
index 0000000000000000000000000000000000000000..9f585ff91852864a5bd7cb88dd32ffe3a4c1a321
--- /dev/null
+++ b/tests/test_imc.py
@@ -0,0 +1,33 @@
+import pathlib
+import sys
+
+import pytest
+
+# Garante que o diretório raiz do projeto esteja no PYTHONPATH
+PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
+if str(PROJECT_ROOT) not in sys.path:
+    sys.path.insert(0, str(PROJECT_ROOT))
+
+from imc import ResultadoIMC, calcular_imc
+
+
+def test_calcular_imc_normal():
+    resultado = calcular_imc(70, 1.75)
+    assert resultado == ResultadoIMC(imc=22.86, categoria="Peso normal")
+
+
+def test_calcular_imc_sobrepeso():
+    resultado = calcular_imc(85, 1.75)
+    assert resultado == ResultadoIMC(imc=27.76, categoria="Sobrepeso")
+
+
+def test_calcular_imc_obesidade_grau_iii():
+    resultado = calcular_imc(130, 1.6)
+    assert resultado == ResultadoIMC(imc=50.78, categoria="Obesidade grau III")
+
+
+def test_calcular_imc_valores_invalidos():
+    with pytest.raises(ValueError):
+        calcular_imc(0, 1.7)
+    with pytest.raises(ValueError):
+        calcular_imc(70, 0)
 
EOF
)
