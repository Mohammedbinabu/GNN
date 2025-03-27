import sqlite3
import torch

class DatabaseConnection:
    def __init__(self, db_path="employee_management0.db"):
        self.db_name = db_path
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.schema = {}
        self.edges = []
        self.edges_weights = []
        self.sc = self.get_schema()
        self.ed = self.get_edges()
        print("Connection established successfully.")

    def get_schema(self):
        """Extracts schema details from the database."""
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in self.cursor.fetchall()]
        for table in tables:
            self.cursor.execute(f"PRAGMA table_info({table})")
            columns = [row[1] for row in self.cursor.fetchall()]
            self.schema[table] = columns        
        return self.schema 

    def get_edges(self):
        """Extracts foreign key relationships and assigns edge weights."""
        if not self.schema:  # Ensure schema is loaded first
            self.get_schema()

        table_indices = {table: idx for idx, table in enumerate(self.schema)}

        for table in self.schema:
            self.cursor.execute(f"PRAGMA foreign_key_list({table})")
            fks = self.cursor.fetchall()
            
            if fks:  # Ensure foreign keys exist
                for fk in fks:
                    ref_table = fk[2]  # The referenced table
                    if ref_table in table_indices:
                        self.edges.append((table_indices[table], table_indices[ref_table]))  # Directed edge
                        self.edges.append((table_indices[ref_table], table_indices[table]))  # Bidirectional edge
                        self.edges_weights.extend([2.0, 2.0])  # Assign weights
                        # 0 edges
                        # 1 edges_weights
        return self.edges, self.edges_weights


class embedding(DatabaseConnection):
    s
