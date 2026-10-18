from __future__ import annotations

from pathlib import Path

import pandas as pd


class Reportes:
	"""Genera un resumen textual de un DataFrame."""

	def generar_reportes(self, df: pd.DataFrame) -> str:
		"""Devuelve información general y estadísticas descriptivas."""
		resumen = [
			"Resumen del dataset",
			f"Filas: {df.shape[0]}",
			f"Columnas: {df.shape[1]}",
			"",
			"Tipos de datos:",
			df.dtypes.to_string(),
			"",
			"Valores nulos por columna:",
			df.isna().sum().to_string(),
			"",
			"Estadísticas descriptivas:",
			df.describe(include="all").to_string(),
		]
		return "\n".join(resumen)

	def guardar_reporte(self, df: pd.DataFrame, ruta: str | Path) -> str:
		"""Guarda el reporte en un archivo de texto y devuelve su ruta."""
		ruta_archivo = Path(ruta)
		ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
		ruta_archivo.write_text(self.generar_reportes(df), encoding="utf-8")
		return str(ruta_archivo)
