 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/imc.py b/imc.py
new file mode 100644
index 0000000000000000000000000000000000000000..21a889e1d6cce874b02cc9ec1e29c3a7016c2aaf
--- /dev/null
+++ b/imc.py
@@ -0,0 +1,84 @@
+"""Aplicativo simples de linha de comando para cálculo do IMC.
+
+Uso básico:
+    python imc.py --peso 70 --altura 1.75
+"""
+
+from __future__ import annotations
+
+import argparse
+from dataclasses import dataclass
+from typing import Tuple
+
+
+@dataclass(frozen=True)
+class ResultadoIMC:
+    imc: float
+    categoria: str
+
+
+CATEGORIAS: Tuple[Tuple[float, float, str], ...] = (
+    (0, 18.5, "Abaixo do peso"),
+    (18.5, 25, "Peso normal"),
+    (25, 30, "Sobrepeso"),
+    (30, 35, "Obesidade grau I"),
+    (35, 40, "Obesidade grau II"),
+    (40, float("inf"), "Obesidade grau III"),
+)
+
+
+def calcular_imc(peso: float, altura: float) -> ResultadoIMC:
+    """Calcula o IMC e retorna o valor e a categoria.
+
+    Args:
+        peso: Peso em quilogramas.
+        altura: Altura em metros.
+
+    Returns:
+        ResultadoIMC com o valor arredondado para 2 casas decimais e categoria correspondente.
+
+    Raises:
+        ValueError: Se peso ou altura forem menores ou iguais a zero.
+    """
+
+    if peso <= 0:
+        raise ValueError("Peso deve ser maior que zero.")
+    if altura <= 0:
+        raise ValueError("Altura deve ser maior que zero.")
+
+    imc = peso / (altura ** 2)
+
+    for limite_inferior, limite_superior, categoria in CATEGORIAS:
+        if limite_inferior <= imc < limite_superior:
+            return ResultadoIMC(imc=round(imc, 2), categoria=categoria)
+
+    # Como usamos infinito positivo no último intervalo, teoricamente nunca chegaremos aqui.
+    raise RuntimeError("Não foi possível classificar o IMC calculado.")
+
+
+def _parse_args() -> argparse.Namespace:
+    parser = argparse.ArgumentParser(description="Calculadora de IMC")
+    parser.add_argument(
+        "--peso",
+        type=float,
+        required=True,
+        help="Peso em quilogramas (ex: 70.5)",
+    )
+    parser.add_argument(
+        "--altura",
+        type=float,
+        required=True,
+        help="Altura em metros (ex: 1.75)",
+    )
+    return parser.parse_args()
+
+
+def main() -> None:
+    args = _parse_args()
+    resultado = calcular_imc(args.peso, args.altura)
+    print(f"IMC: {resultado.imc:.2f}")
+    print(f"Categoria: {resultado.categoria}")
+
+
+if __name__ == "__main__":
+    main()
 
EOF
)
