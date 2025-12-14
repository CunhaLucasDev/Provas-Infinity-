"""tabela_clientes.py"""
#Criei a tabela e trabalhei ela um pouco mais para integrar os conhecimentos de python e sqlite3,
#focando em operações básicas de CRUD (Create, Read, Update, Delete).
# Pedi um pouco de ajuda ao Github para deixar mais moderna e com as boas práticas atuais.

from pathlib import Path
import sqlite3
from typing import List, Dict, Optional


DB_NAME = Path(__file__).parent / "data.db"


def _get_conn(db_path: Optional[Path] = None):
	db = Path(db_path) if db_path else DB_NAME
	conn = sqlite3.connect(db)
	conn.row_factory = sqlite3.Row
	return conn


def init_db(db_path: Optional[Path] = None) -> None:
	"""Create the Clientes table if it doesn't exist."""
	conn = _get_conn(db_path)
	cur = conn.cursor()
	cur.execute(
		"""
		CREATE TABLE IF NOT EXISTS Clientes (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			Nome TEXT NOT NULL,
			Idade INTEGER,
			Cidade TEXT
		)
		"""
	)
	conn.commit()
	conn.close()


def add_cliente(nome: str, idade: Optional[int], cidade: Optional[str], db_path: Optional[Path] = None) -> int:
	"""Insert a new cliente and return its ID."""
	conn = _get_conn(db_path)
	cur = conn.cursor()
	cur.execute(
		"INSERT INTO Clientes (Nome, Idade, Cidade) VALUES (?, ?, ?)",
		(nome, idade, cidade),
	)
	conn.commit()
	inserted_id = cur.lastrowid
	conn.close()
	return inserted_id


def get_clientes(db_path: Optional[Path] = None) -> List[Dict]:
	"""Return all clientes as list of dicts."""
	conn = _get_conn(db_path)
	cur = conn.cursor()
	cur.execute("SELECT ID, Nome, Idade, Cidade FROM Clientes ORDER BY ID")
	rows = cur.fetchall()
	conn.close()
	return [dict(row) for row in rows]


def update_cliente(id: int, nome: Optional[str] = None, idade: Optional[int] = None, cidade: Optional[str] = None, db_path: Optional[Path] = None) -> bool:
	"""Update provided fields for a cliente. Returns True if a row was changed."""
	fields = []
	params = []
	if nome is not None:
		fields.append("Nome = ?")
		params.append(nome)
	if idade is not None:
		fields.append("Idade = ?")
		params.append(idade)
	if cidade is not None:
		fields.append("Cidade = ?")
		params.append(cidade)
	if not fields:
		return False
	params.append(id)
	sql = f"UPDATE Clientes SET {', '.join(fields)} WHERE ID = ?"
	conn = _get_conn(db_path)
	cur = conn.cursor()
	cur.execute(sql, params)
	conn.commit()
	changed = cur.rowcount > 0
	conn.close()
	return changed


def delete_cliente(id: int, db_path: Optional[Path] = None) -> bool:
	"""Delete cliente by ID. Returns True if a row was deleted."""
	conn = _get_conn(db_path)
	cur = conn.cursor()
	cur.execute("DELETE FROM Clientes WHERE ID = ?", (id,))
	conn.commit()
	deleted = cur.rowcount > 0
	conn.close()
	return deleted


if __name__ == "__main__":
	# quick demo: create DB, add two clients, print them
	init_db()
	print(f"Database created/verified at: {DB_NAME}")
	a = add_cliente("Ana Silva", 30, "São Paulo")
	b = add_cliente("João Pereira", 42, "Rio de Janeiro")
	print(f"Inserted IDs: {a}, {b}")
	rows = get_clientes()
	print("Clientes in DB:")
	for r in rows:
		print(r)

